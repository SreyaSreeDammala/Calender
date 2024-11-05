import tkinter as tk
from tkinter import messagebox

# Function to calculate the odd days for the last 2 digits of a year
def odd_count(year):
    if year == 0:
        return 0
    year -= 1
    odd = year % 7
    leap_years = year // 4
    odd_days = (odd + leap_years) % 7
    return odd_days

# Function to calculate the odd days for the first 2 digits of a year
def odd_year(yr):
    if yr % 4 == 0:
        return 0
    elif yr % 4 == 1:
        return 5
    elif yr % 4 == 2:
        return 3
    elif yr % 4 == 3:
        return 1

# Function for the first two digits of a year when it's less than 1000
def under_thousand(year):
    year = year // 100
    return odd_year(year)

# Function to calculate the odd days for a full year
def year_code(num):
    if num >= 1000:
        first_part = num // 100
        second_part = num % 100
        century_code = odd_year(first_part)
        num_code = odd_count(second_part)
        yr_code = (century_code + num_code) % 7
        return yr_code
    else:
        second_part = num % 100
        century_code = under_thousand(num)
        num_code = odd_count(second_part)
        yr_code = (century_code + num_code) % 7
        return yr_code

# Function to calculate the odd day for a particular date
def date_code(date):
    return date % 7

# Function to calculate the odd days for a particular month
def month_code(mnt_num):
    mnt_code = {1:0, 2:3, 3:3, 4:6, 5:1, 6:4, 7:6, 8:2, 9:5, 10:0, 11:3, 12:5}
    return mnt_code[mnt_num]

# Function to get the weekday for a given number
def week_day(num):
    week_days = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday',
                 5:'Friday', 6:'Saturday'}
    return week_days[num]

# Function to check the weekday for a given date, month, and year
def check_week_day(date, month, year):
    day = (date_code(date) + month_code(month) + year_code(year)) % 7
    if month > 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        day = (day + 1) % 7
    return week_day(day)

# Function to validate the date input
def is_valid_date(day, month, year):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False, "Year, month, or day is out of range. Please check your input."
    
    # Days per month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Leap year check (February has 29 days in a leap year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    
    if day > days_in_month[month - 1]:
        return False, f"Invalid day for month {month}. This month only has {days_in_month[month - 1]} days."
    
    return True, ""

# Function to calculate and display the result on the GUI
def calculate_weekday():
    try:
        # Get user inputs from the entry fields
        date = int(entry_date.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        
        # Validate the input date
        valid, error_message = is_valid_date(date, month, year)
        if not valid:
            messagebox.showerror("Invalid Date", error_message)
            return
        
        # Calculate the weekday
        result = check_week_day(date, month, year)
        label_result.config(text=f"The day for {date}/{month}/{year} is: {result}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for date, month, and year.")

# Function to reset the input fields and result
def reset_fields():
    entry_date.delete(0, tk.END)
    entry_month.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    label_result.config(text="")

# Setting up the Tkinter window (GUI)
window = tk.Tk()
window.title("Weekday Calculator")
window.geometry("400x350")
window.config(bg="#f0f0f0")

# Title label
label_title = tk.Label(window, text="Weekday Calculator", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

# Date input fields
label_date = tk.Label(window, text="Enter Date (1-31):", bg="#f0f0f0")
label_date.pack()
entry_date = tk.Entry(window, font=("Arial", 12), width=20)
entry_date.pack()

label_month = tk.Label(window, text="Enter Month (1-12):", bg="#f0f0f0")
label_month.pack()
entry_month = tk.Entry(window, font=("Arial", 12), width=20)
entry_month.pack()

label_year = tk.Label(window, text="Enter Year:", bg="#f0f0f0")
label_year.pack()
entry_year = tk.Entry(window, font=("Arial", 12), width=20)
entry_year.pack()

# Buttons
btn_calculate = tk.Button(window, text="Calculate", command=calculate_weekday, bg="blue", fg="white", font=("Arial", 12), width=20)
btn_calculate.pack(pady=10)

btn_reset = tk.Button(window, text="Reset", command=reset_fields, bg="gray", fg="white", font=("Arial", 12), width=20)
btn_reset.pack(pady=5)

# Result label
label_result = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0", fg="green")
label_result.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
