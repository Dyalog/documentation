# Shared Members

Certain .NET classes provide methods, fields and properties that can be called directly without the need to create an instance of the class first. These members are known as shared, because they have the same definition for the class and for any instance of the class.

The methods Now and IsLeapYear exported by System.DateTime fall into this category.

Example
```apl
     ⎕USING←,⊂'System'
			 
     DateTime.Now
18/03/2020 11:14:05
			 
     DateTime.IsLeapYear 2000
1
```
