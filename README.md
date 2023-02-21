CCNA Planner

This Python script is a simple CCNA (Cisco Certified Network Associate) planner application built using the tkinter library. It helps you plan your progress on either the "Jeremy's IT Lab" or "Flack Box" CCNA study programs, by calculating how much content you should get done each day.

To use the application, you will need to enter your test date (year, month, day), the program you are studying (1 for Jeremy's IT Lab or 2 for Flack Box), and the day/section of the program you are currently on. The program will then calculate how much content you should aim to get done each day for the remaining duration of your program, based on a 7-day and a 5-day study week.

The script uses the datetime module to calculate the difference between the current date and the test date, and the tkinter library to create a GUI for the user to enter their inputs and display the results.

How to use
  To use this script, you need to have Python 3 installed on your system. Once you have Python installed, follow these steps:

1. Save the code to a file with a .py extension (e.g., ccna_planner.py).
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the command python ccna_planner.py to launch the application.
4. Enter your test date, program type, and current day/section into the GUI.
5. Click the "Calculate" button to get the recommended study schedule.

The recommended study schedule will be displayed in the GUI.

Note: You may need to install the tkinter library if it's not already installed on your system.

Dependencies:

This script requires the following modules:

'datetime'
'tkinter'
