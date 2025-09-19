<h1 class="heading"><span class="name">APL Application as a Service</span></h1>

## Introduction

Dyalog APL provides a mechanism for users to register and manage an application workspace as a Windows service. The application workspace must implement an interface to handle messages from the Windows Service Control Manager (SCM) in addition to the code required to drive the application.

Windows Services run as background tasks controlled by the SCM. When the computer is started, Windows Services are run before a user logs on to the system and do not normally interact with the desktop. A Dyalog service is run under the auspices of *Local System*.

## Installing and Uninstalling a Dyalog Service

To install a Dyalog service it is necessary to run `dyalog.exe` from the command line with administrator privileges, specifying the application workspace and the following parameters, where *service_name* is a name of your choice.

- **APL_ServiceInstall=service_name**

The command must specify the full pathname to `dyalog.exe` and to the application workspace. A slightly modified version of this  command line will be stored by the SCM and re-executed whenever the service is started.

Dyalog installs the service with a *Startup Type* of *Automatic*. This means that it will be started automatically whenever the computer is restarted. However, it is necessary to start it manually (using the SCM) the first time after it is installed.

The same command must be used to uninstall the service, but with:

- **APL_ServiceUninstall=service_name**

The following table summarises the parameters that can be specified by the user. Other parameters will appear on the command line in the SCM, but should not be specified by the user.

|Parameter               |Description                                                                                                                                          |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|**APL_ServiceInstall**  |Causes Dyalog to register the named service, using the current command line, but with **APL_ServiceRun** replacing **APL_ServiceInstall** in the SCM.|
|**APL_ServiceUninstall**|Causes Dyalog to uninstall the named service.                                                                                                        |

## The Application Workspace

The application workspace must be designed to handle and respond (in a timely manner) to notification messages from the SCM as well as to provide the application logic. SCM notifications  include instructions to start, stop, pause and resume.

SCM notification messages generate a ServiceNotification event on the Root object. To handle these messages, it is necessary to attach a callback function to this event, and to invoke the Wait method or `⎕DQ'.'` to process them. This must be executed in thread 0.

If the application is designed to be driven from events such as Timer or TCPSocket or user-defined events, it too may be implemented via callbacks in thread 0 under the control of the same Wait method or `⎕DQ'.'`. If the application uses Conga it is recommended that it runs in a separate thread.

The workspace `ws\aplservice.dws` is included in the APL release. Its start-up function is as follows:
```apl
     ⎕LX←'Start'

     ∇ Start;ServiceState;ServiceControl
[1]    :If 'W'≠3⊃#.⎕WG'APLVersion'
[2]        ⎕←'This workspace only works using Dyalog APL for
              Windows version 14.0 or later'
[3]        :Return
[4]    :EndIf
[5]    :If 0∊⍴2 ⎕NQ'.' 'GetEnvironment' 'RunAsService'
[6]        Describe
[7]        :Return
[8]    :EndIf
[9]    ⍝ Define SCM constants
[10]   HashDefine
[11]   ⍝ Set up callback to handle SCM notifications
[12]   '.'⎕WS'Event' 'ServiceNotification' 'ServiceHandler'
[13]   ⍝ Global variable defines current state of the service
[14]   ServiceState←SERVICE_RUNNING
[15]   ⍝ Global variable defines last SCM notification to the
         service
[16]   ServiceControl←0
[17]   ⍝ Application code runs in a separate thread
[18]   Main&0
[19]   ⎕DQ'.'
[20]   ⎕OFF
     ∇

```

### Handling ServiceNotification Events

To give the workspace (which may be busy) time to respond to SCM notifications, Dyalog responds immediately to confirm that the service has entered the appropriate pending state. For example, if the notification is SERVICE_CONTROL_STOP, Dyalog informs the SCM that the service state is SERVICE_STOP_PENDING. It is then up to the callback function to confirm that the state has reached SERVICE_STOPPED.

The following sample function is provided in `aplservice.dws`.

### ServiceHandler Callback Function
```apl
     ∇ r←ServiceHandler(obj event action state);sink
[1]   ⍝ Callback to handle notifications from the SCM
[2]
[3]   ⍝ Note that the interpreter has already responded
[4]   ⍝ automatically to the SCM with the corresponding
[5]   ⍝ "_PENDING" message prior to this callback being reached
[6]
[7]   ⍝ This callback uses the SetServiceState Method to confirm
[8]   ⍝ to the SCM that the requested state has been reached
[9]
[10]   r←0  ⍝  so returns a 0 result (the event has been handled,
[11]        ⍝ no further action required)
[12]
[13]  ⍝ It stores the desired state in global ServiceState to
[14]  ⍝ notify the application code which must take appropriate
[15]  ⍝ action. In particular, it must respond to a "STOP or
[16]  ⍝ "SHUTDOWN" by terminating the APL session
[17]
[18]   :Select ServiceControl←action
[19]   :CaseList SERVICE_CONTROL_STOP SERVICE_CONTROL_SHUTDOWN
[20]       ServiceState←SERVICE_STOPPED
[21]       state[4 5 6 7]←0
[22]
[23]   :Case SERVICE_CONTROL_PAUSE
[24]       ServiceState←SERVICE_PAUSED
[25]
[26]   :Case SERVICE_CONTROL_CONTINUE
[27]       ServiceState←SERVICE_RUNNING
[28]   :Else
[29]       :If state[2]=SERVICE_START_PENDING
[30]           ServiceState←SERVICE_RUNNING
[31]       :EndIf
[32]   :EndSelect
[33]   state[2]←ServiceState
[34]   sink←2 ⎕NQ'.' 'SetServiceState'state
     ∇
```

### The Application Code

The following function illustrates how the application code for the service might be structured. It is merely an illustration, but however it is done, it is important that the code handles the instructions to pause, continue and stop in an appropriate manner. In this example, the function `Main` creates a log file and writes to it when the state of the service changes.
```apl
     ∇ Main arg;nid;log;LogFile
[1]    ⎕NUNTIE ⎕NNUMS
[2]    log←{((⍕⎕TS),' ',⍵,⎕UCS 13 10)⎕NAPPEND ⍺}
[3]    LogFile←'c:\ProgramData\TEMP\APLServiceLog.txt'
[4]    :Trap 22
[5]        nid←LogFile ⎕NCREATE 0
[6]    :Else
[7]        :Trap 22
[8]            nid←LogFile ⎕NTIE 0
[9]            0 ⎕NRESIZE nid
[10]       :Else
[11]           ⎕←'Unable to tie or create logfile'
[12]       :EndTrap
[13]   :EndTrap
[14]   nid log'Starting'
[15]   :While ServiceState≠SERVICE_STOPPED
[16]       :If ServiceControl≠0 ⋄
               nid log'ServiceControl=',⍕ServiceControl ⋄ :EndIf
[17]       :If ServiceState=SERVICE_RUNNING
[18]           nid log'Running'
[19]       :ElseIf ServiceState=SERVICE_PAUSED
[20]           ⍝  Pause application
[21]       :EndIf
[22]       ServiceControl←0 ⍝ Reset (we only want to log changes)
[23]       ⎕DL 10 ⍝ Just to prevent busy loop
[24]   :EndWhile
[25]   ⎕NUNTIE nid
[26]   ⎕OFF 0
     ∇

```

### Debugging Dyalog Services

Services are run in the background under the auspices of *Local System*, and not associated with an interactive user. Neither the APL Session nor any GUI components that it creates will be visible on the desktop. This prevents the normal editing and debugging tools from being available.

However, the Dyalog APL Remote Integrated Development environment (Ride) may be connected to any APL session, including one running as a Windows Service, and provide a debugging environment. For more information, see the [Ride User Guide](https://dyalog.github.io/ride). Note however that the Conga DLLs/shared libraries must be available - usually they should reside in the same directory as the interpreter. In previous versions of Dyalog separate Ride DLLs/shared libraries were supplied; these have been subsumed into the Conga libraries in 16.0.

### Event Logging

When a service is installed or removed, Dyalog APL records events in the Dyalog APL section of the *Applications and Services Logs* which can be viewed using the Windows system *Event Viewer*.
