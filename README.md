# Overall System (Suns, planets) Temperature Monitor - E.D.
Very useful for explorers in Elite Dangerous - a monitor for the sum of temperatures of all stars in the currently visited system. 1 - Download both files. 2 - Place both files on your desktop. 3 - In the startup .bat file, adjust the path to YOUR desktop. 4 - Click: start.bat = a window will appear showing sum star temperatures. 5 - window has a "over other windows" function and you can move it wherever you want and change its size - for example to second monitor. It accurately measures the sum of temperatures of all stars after the second manual click on the FSS with the mouse. Thats all!

  The following are required on Windows:
- Python (e.g., Python 3.x) must be installed, as the script uses built-in libraries:
os, json, glob, time, tkinter (part of the standard Python installation).
- Threading (built into Python).
-Watchdog: This is an additional library that needs to be installed using the command in CMD: "pip install watchdog"

=================
Readme - dependence:
To run the two files as a program on Windows 10, especially when using .NET 8.0, you’ll need a few dependencies:

1. .NET 8.0 Runtime:
Required: This is essential for running .NET applications. It includes necessary libraries and frameworks.
Download from the official .NET site.
Installation: Choose .NET Runtime (for running apps) and .NET SDK (for building apps).
2. Visual C++ Redistributable:
Possible Requirement: Some .NET apps may need Visual C++ libraries for system-level functions.
Download from Microsoft Visual C++ Redistributable.
Install the version matching your system (x86 or x64).
3. Windows Updates:
Recommended: Make sure Windows 10 is up to date to avoid compatibility issues.
Go to Settings > Update & Security > Windows Update to check for updates.
4. GUI Libraries (Windows Forms/WPF):
Built into .NET 8.0, needed if your app uses a graphical user interface (GUI).
Ensure .NET SDK is properly installed to support these libraries.
5. Access to Log Files (Elite Dangerous):
File Access: Ensure the app has permission to access the Elite Dangerous log directory. Run as administrator if needed.
Path to Logs: Verify that the log path in the code matches your log file location.
6. JSON Handling (Built-in in .NET 8.0):
Use System.Text.Json for parsing JSON files. No extra libraries are needed, just use the appropriate deserialization methods.
Summary:
.NET 8.0 Runtime and SDK
Visual C++ Redistributable (optional)
Windows Updates
Administrator Access (for log files)
With these dependencies, your application should run smoothly on Windows 10.
