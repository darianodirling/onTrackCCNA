# Import the datetime module and tkinter library
import datetime
import tkinter as tk

# Function to calculate the study plan
def calculate_plan():
    # Get today's date
    today = datetime.date.today()
    
    # Get the year, month, and day from user input
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())
    
    # Calculate the future date based on user input
    future = datetime.date(year, month, day)
    
    # Calculate the difference in days between future and today's date
    diff = future - today
    
    # Calculate the number of weeks left until the test date
    weeks = diff.days / 7
    
    # Get the program type and current day/section from user input
    program = int(program_entry.get())
    cday = int(cday_entry.get())
    
    # Calculate the study plan based on program type
    if program == 1:
        # Jeremy's IT Lab program
        # Calculate the number of days left until the test
        daysLeft = 63 - cday
        
        # Calculate the content budget per week
        contentBudget = round((daysLeft / weeks),2)
        
        # Calculate the daily study goal for a 7-day track
        dailyGoal = round((contentBudget / 7),2)
        
        # Calculate the daily study goal for a 5-day track
        dailyGoalWork = round((contentBudget / 5),2)
        
        # Display the study plan results
        result_label.config(text="This week you should get {} days of content done meaning:\n\n{} days of content a day on a 7 day track\n\n{} days of content on a 5 day track".format(contentBudget, dailyGoal, dailyGoalWork))
    elif program == 2:
        # Flack Box program
        # Calculate the number of days left until the test
        daysLeft = 39 - cday
        
        # Calculate the content budget per week
        contentBudget = round((daysLeft / weeks),2)
        
        # Calculate the daily study goal for a 7-day track
        dailyGoal = round((contentBudget / 7),2)
        
        # Calculate the daily study goal for a 5-day track
        dailyGoalWork = round((contentBudget / 5),2)
        
        # Display the study plan results
        result_label.config(text="This week you should get {} days of content done meaning:\n\n{} days of content a day on a 7 day track\n\n{} days of content on a 5 day track".format(contentBudget, dailyGoal, dailyGoalWork))
    else:
        # Invalid program type entered
        result_label.config(text="Invalid input")

# Create a Tkinter window
root = tk.Tk()
root.title("CCNA Planner")

# Create input fields and labels for user input
year_label = tk.Label(root, text="Enter your test year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

month_label = tk.Label(root, text="Enter your test month:")
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

day_label = tk.Label(root, text="Enter your test day:")
day_label.pack()
day_entry = tk.Entry(root)
day_entry.pack()

program_label = tk.Label(root, text="Type 1 for Jeremy's IT Lab and 2 for Flack Box")
program_label.pack()
program_entry = tk.Entry(root)
program_entry.pack()

cday_label = tk.Label(root, text="Enter the day/section you are on")
cday_label.pack()
cday_entry = tk.Entry
