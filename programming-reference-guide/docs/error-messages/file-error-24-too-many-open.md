

# FILE ERROR 24 Too many open

This report is given when the task limit on the number of open files is exceeded.  It may occur when an APL session is started or when a shell command is issued to start an external process through the system command `⎕SH`.  It is necessary to reduce the number of open files.  It may be necessary to increase the limit on the number of open files to overcome the problem.
