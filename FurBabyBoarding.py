"""
Program: MyProgram.py
Author: Tomi Simic
Last date modified: 2024-02-24
This program is to be used for Assignment 2 in Module 06. It's an expansion on
final project, so it will start by displaying a new window.
"""
# Import Tkinter
# Import other modules as needed
# Create sqlite3 database to store dates, runs, and pets
# Default window Class
# Entry box window function
# Main function

# Importing everything from tkinter:
import tkinter as tk

# Importing other module(s) if needed:
import datetime
import sqlite3


# Function that handles date and time at the pet entry:
def today():
    """Run on boarding time as entry time"""
    today = datetime.date.today()
    return today


# Class that hold functions to handle entry data into database:
def db():
    pass

# Function used as a jump box holding all names of suites:


def runs():
    """Provides a dictonary of runs and their count."""
    runs = {
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
    return runs


# Child Window function:
def get_window():
    """Creates the second window with text entry box"""
    # clears the textbox on click:
    def clear_textbox(button):
        textbox.delete("1.0", tk.END)
    window = tk.Toplevel()
    window.configure(height=400, width=600)
    window.title("Run details:")
    close = tk.Button(window, text="Close", command=window.destroy)
    close.grid(row=1, column=0, columnspan=1)
    # Create a textbox:
    textbox = tk.Text(window, height=20, width=60,
                      borderwidth=4, background="tan")
    textbox.insert(tk.END, "Please enter boarding details here:")
    textbox.grid(row=0, column=0)
    # Clear the textbox on the click
    textbox.bind("<Button-1>", clear_textbox)


# Class that holds all parts
class App:
    """The class holding all GUI components"""

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("FurBabyBoarding")

        # Create a button function:
        self.row_ = 1
        self.second_row = 1

        def buttoned(entry, foreground, background):
            self.button = tk.Button(self.master, text=f"{entry}", fg=f"{
                                    foreground}", bg=f"{background}", command=get_window)
            # self.button.pack()
            if self.row_ <= 5:
                self.button.grid(row=self.row_, column=0)
                self.row_ += 1
            else:
                self.button.grid(row=self.second_row, column=1)
                self.second_row += 1
            return self.button

        # Create a label
        self.label = tk.Label(self.master, text="Welcome to Hillside Animal\
 Hospital Boarding!", width=70, fg="white", bg="dark red")
        self.label.grid(row=0, column=0, columnspan=2)

        # Create Buttons for double runs:
        self.button_1 = buttoned(f"Deluxe spots open: {
                                 runs().get('DELUXE')}", "white", "dark red")
        self.button_2 = buttoned(f"Suites open: {
                                 runs().get('SUITES')}", "white", "dark red")
        self.button_3 = buttoned(f"In&Out spots open: {
                                 runs().get('IN_OUT')}", "white", "dark red")
        self.button_4 = buttoned(f"Double run(s) open: {
                                 runs().get('DOUBLE_RUN')}", "white", "dark red")
        self.button_5 = buttoned(f"Regular run(s) open: {
                                 runs().get('REGULAR')}", "white", "dark red")

        # Create Buttons for single runs:
        self.button_6 = buttoned(f"Large cage(s) open: {
            runs().get('LARGE_CAGE')}", "dark red", "white")
        self.button_7 = buttoned(f"Medium cage(s) open: {
            runs().get('MEDIM_CAGE')}", "dark red", "white")
        self.button_8 = buttoned(f"Cat cage(s) open: {
            runs().get('CAT_CAGE')}", "dark red", "white")
        self.button_9 = buttoned(f"Rabbit cage(s) open: {
            runs().get('RABBIT_CAGE')}", "dark red", "white")
        self.button_10 = buttoned(f"Stalls open: {
            runs().get('STALLS')}", "dark red", "white")


# Main function that starts the show:
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
