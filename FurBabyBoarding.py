"""
Program: MyProgram.py
Author: Tomi Simic
Last date modified: 2024-02-29
This program is to be used for Assignment 2 in Module 06. It's an expansion on
final project, so it will start by displaying a new window.
"""
# import Tkinter
# import other modules as needed
# user input validation class
# class to manage scheduling
# Create a class with sqlite3 database to store dates, runs, and pets
# Default window Class
# Main function

# Importing everything from tkinter:
import tkinter as tk
# pip install needed for tkcalendar
# from tkcalendar import DateEntry

# Importing other module(s) if needed:
import datetime
from PIL import ImageTk, Image
import sqlite3

# Function used as a jump box holding all names of suites:


# def runs():
#     """Provides a dictonary of runs and their count."""
#     runs = {
#         # Spots for 2 - 3 pets:
#         'DELUXE': 2,
#         'SUITES': 7,
#         'IN_OUT': 12,
#         'DOUBLE_RUN': 4,
#         'REGULAR': 16,

#         # Spots for single pet:
#         'LARGE_CAGE': 2,
#         'MEDIM_CAGE': 4,
#         'CAT_CAGE': 7,
#         'RABBIT_CAGE': 2,
#         'STALLS': 2
#     }
#     return runs

# User input validation:


class UserInput:
    """Verifying inputs provided by the user"""

    def prompts(self):
        """Jumpbox for prompts needed during verification process"""
        now = datetime.datetime.now()
        prompts = {
            "dividor": "You didn't use a dash to separate month, day, and \
year.",
            "try": "Please try again and enter correct date format.",
            "wrong": "Please check your date as you have not entered values \
for either month, day, year, or your format is wrong.",
            "no_number": "You have not entered number(s) for one or more date \
segments.",
            "bad_month": "A month value cannot be more than 12.",
            "bad_day": "A day value cannot be more than 31.",
            "bad_year": "The year value cannot be in the past.",
            "old_month": "The month value cannot be in the past.",
            "old_day": "The day value cannot be in the past.",
            "ask": f"When is the client checking out? (i.e.: {now.month}-\
{now.day + 5}-{now.year})> "
        }
        return prompts

    def date_format(self):
        """Verifying user input for correct date entry"""
        now = datetime.datetime.now()
        # Collecting date entries into single unit:
        schedule = []
        # Starting the input loop, looking for valid data entry or restarting
        # the loop:
        prompt = "EMPTY"
        while prompt == "EMPTY":
            # Providing prompt with an example that stays current:
            prompt = input(f"When is the client checking out? (i.e.: {now.month}-\
{now.day + 5}-{now.year})> ")
            print(prompt)
            # Checking for correct separator:
            if '-' not in prompt:
                print(self.prompts().get('dividor'), self.prompts().get('try'))
                prompt = "EMPTY"
            else:
                # Checking for correct count of values entered:
                if len(prompt.split('-')) < 3:
                    print(self.prompts().get('wrong'),
                          self.prompts().get('try'))
                    prompt = "EMPTY"
                else:
                    # Separating user's input into year, month, and day:
                    month, day, year = prompt.split('-')
                    # Verifying the user is using only numbers in date entry:
                    if month.isnumeric() is False or day.isnumeric() is False \
                            or year.isnumeric() is False:
                        print(self.prompts().get('no_number'),
                              self.prompts().get('try'))
                        prompt = "EMPTY"
                    # Verifying the upper limit for month and day
                    elif int(month) > 12:
                        print(self.prompts().get('bad_month'),
                              self.prompts().get('try'))
                        prompt = "EMPTY"
                    elif int(day) > 31:
                        print(self.prompts().get('bad_day'),
                              self.prompts().get('try'))
                        prompt = "EMPTY"
                    # Verifying the date wasn't entered in the past
                    elif int(year) < now.year:
                        print(self.prompts().get('bad_year'),
                              self.prompts().get('try'))
                        prompt = "EMPTY"
                    elif int(month) < now.month:
                        print(self.prompts().get('old_month'),
                              self.prompts().get('try'))
                        prompt = "EMPTY"
                    elif int(day) < now.day:
                        print(self.prompts().get('old_day'),
                              self.prompts().get('try'))
                        prompt = "EMPTY"
                    else:
                        # Populating the list holding individual values:
                        schedule.append(year)
                        schedule.append(month)
                        schedule.append(day)
        return schedule


# Class that holds all parts
class App(UserInput):
    """The class holding all GUI components"""

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("FurBabyBoarding")
        self.master.iconbitmap("FurryResources\\Fbb.ico")
        self.runs = {
            # Spots for 2 - 3 pets:
            'DELUXE': 2,
            'SUITES': 7,
            'IN_OUT': 12,
            'DOUBLE_RUN': 4,
            'REGULAR': 16,

            # Spots for single pet:
            'LARGE_CAGE': 2,
            'MEDIM_CAGE': 4,
            'CAT_CAGE': 7,
            'RABBIT_CAGE': 2,
            'STALLS': 2
        }

        # Create a button function:
        self.row_ = 2
        self.second_row = 2

        # Create a label
        self.entry_text = "Welcome to FurBaby Boarding!"
        self.label = tk.Label(
            self.master, width=39, text=self.entry_text, fg="white", bg="dark red")
        self.label.grid(row=0, column=1, columnspan=4)
        self.entry_id_label = tk.Label(
            self.master, text="Main Display. Click on it to type:")
        self.entry_id_label.grid(row=1, column=0)
        self.entry_box = tk.Entry(
            self.master, width=54, fg="dark red", bg="white")
        self.entry_box.grid(row=1, column=1, columnspan=4)
        self.entry_box.insert(0, self.entry_text)
        # Adding picture label:
        self.picture_1 = ImageTk.PhotoImage(
            Image.open("FurryResources\\PitterPatter3.jpg"))
        self.picture_frame = tk.Label(
            image=self.picture_1, width=200, height=200)
        self.picture_frame.grid(row=0, column=5, rowspan=12)

        def buttoned(entry, padding=0):
            """Generates buttons as needed"""
            self.button = tk.Button(self.master, padx=padding, text=f"{
                                    entry}", fg=f"white", bg=f"dark red")

            if self.row_ <= 6:
                self.button.grid(row=self.row_, column=0, sticky="w")
                self.row_ += 1
            else:
                self.button.grid(row=self.second_row, column=3, sticky="e")
                self.second_row += 1
            return self.button

        # Create Buttons for double runs:
        self.button_1 = buttoned("DELUXE spots open", 4)
        self.button_1.configure(
            command=lambda m=f'DELUXE': self.reaction(m, self.field_1))
        self.button_2 = buttoned("Suites open", 22)
        self.button_3 = buttoned("In&Out spots open", 2)
        self.button_4 = buttoned("Double run(s) open", 2)
        self.button_5 = buttoned("Regular run(s) open", 1)

        # Create Buttons for single runs:
        self.button_6 = buttoned("Large cage(s) open", 8)
        self.button_7 = buttoned("Medium cage(s) open")
        self.button_8 = buttoned("Cat cage(s) open", 14)
        self.button_9 = buttoned("Rabbit cage(s) open", 6)
        self.button_10 = buttoned("Stalls open", 30)

        # Create a label function:
        self.row_ = 2
        self.second_row = 2

        def fielded(entry):
            """Generates labels as needed"""
            self.field = tk.Entry(
                self.master, width=10)
            self.field.insert(1, entry)

            if self.row_ <= 6:
                self.field.grid(row=self.row_, column=1, sticky="w")
                self.row_ += 1
            else:
                self.field.grid(row=self.second_row, column=4, sticky="e")
                self.second_row += 1
            return self.field

        self.field_1 = fielded(f"{self.runs.get('DELUXE')}")
        self.field_2 = fielded(f"{self.runs.get('SUITES')}")
        self.field_3 = fielded(f"{self.runs.get('IN_OUT')}")
        self.field_4 = fielded(f"{self.runs.get('DOUBLE_RUN')}")
        self.field_5 = fielded(f"{self.runs.get('REGULAR')}")
        self.field_6 = fielded(f"{self.runs.get('LARGE_CAGE')}")
        self.field_7 = fielded(f"{self.runs.get('MEDIM_CAGE')}")
        self.field_8 = fielded(f"{self.runs.get('CAT_CAGE')}")
        self.field_9 = fielded(f"{self.runs.get('RABBIT_CAGE')}")
        self.field_10 = fielded(f"{self.runs.get('STALLS')}")

        # Close button:
        close = tk.Button(self.master, text="Close",
                          command=self.master.quit, width=20)
        close.grid(row=self.row_ + 2, column=0, sticky="w")

        # User manual (help):
        help = tk.Button(self.master, text="User manual",
                         command=self.get_help, width=20)
        help.grid(row=self.row_ + 2, column=1, sticky="e")

    def reaction(self, clicked, field):
        """Enables field to enter checkout date"""
        # Clear entry box when needed:
        def clear_entry(button):
            self.entry_box.delete(0, tk.END)
        self.entry_box.delete(0, tk.END)
        entry = self.spots_available(clicked, field)
        if entry != "No spots available!!!":
            self.entry_box.delete(0, tk.END)
            self.entry_box.insert(0, UserInput().prompts().get('ask'))
            self.entry_box.bind("<Button-1>", clear_entry)
        else:
            self.entry_box.insert(0, entry)

    def spots_available(self, clicked, field):
        """Checks and modifies run availability"""
        count = self.runs.get(clicked)
        if count > 0:
            self.runs[clicked] = count - 1
            print(self.runs.get(clicked))
            field.delete(0, tk.END)
            field.insert(0, self.runs.get(clicked))
            return self.runs.get(clicked)
        self.entry_box.configure(background="yellow")
        return "No spots available!!!"

    def get_help(self):
        """Opens the READme.txt file as GUI's internal help"""
        with open("FurryResources\\READme.txt", "r", encoding="UTF-8") as manual:
            text = manual.read()
        help = tk.Toplevel()
        help.title("Getting started & help")
        help.iconbitmap("FurryResources\\Fbb.ico")
        close = tk.Button(help, text="Close", command=help.destroy)
        close.grid(row=1, column=0, columnspan=1)
        instructions = tk.Text(help, background="tan")
        instructions.insert(tk.END, text)
        instructions.grid(row=0, column=0)

    # Child Window function:

    def get_window(self):
        """Creates the second window with text entry box"""
        # clears the textbox on click:
        def clear_textbox(button):
            textbox.delete("1.0", tk.END)
        window = tk.Toplevel()
        window.configure(height=400, width=600)
        window.title("Run details:")
        window.iconbitmap("FurryResources\\Fbb.ico")
        close = tk.Button(window, text="Close", command=window.destroy)
        close.grid(row=1, column=0, columnspan=1)
        # Create a textbox:
        textbox = tk.Text(window, height=20, width=60, background="tan")
        textbox.insert(tk.END, f"Today's date and time is: {
            Schedule().today()}. Please enter boarding details here:")
        textbox.grid(row=0, column=0)
        # Clear the textbox on the click
        textbox.bind("<Button-1>", clear_textbox)


# Function that handles date and time at the pet entry:
class Schedule:
    """Provides current time and definitions needed to calculate run availability"""

    def __init__(self):
        self.now = datetime.datetime.now()

    def today(self):
        """Run on boarding time as entry time"""
        # today = datetime.date.today()
        now_rounded = self.now.strftime("%Y-%m-%d, %H:%M")
        return now_rounded

    def checking_in(self):
        self.check_in = input("When is the client checking out?")
        self.scheduled_checkout = self.check_in - self.now

    def checking_out(self):
        pass

    def __str__(self):
        return str(self.today())


# Class that hold functions to handle entry data into database:
class DB:
    """Establishes a connection and handles retrival and saving of data"""

    def __init__(self):
        """Establishing connection to the database"""
        self.connection = sqlite3.connect("FurBaby_DB.db")
        self.cursor = self.connection.cursor()

    def save_to_db(self):
        """Saving changes to the database and closing connection"""
        pass

        # Closing connection once completed
        # self.connection.close()


# Main function that starts the show:
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
