"""
Program: MyProgram.py
Author: Tomi Simic
Last date modified: 2024-02-24
This program is to be used for Assignment 2 in Module 06. It's an expansion on
final project, so it will start by displaying a new window.
"""
# Import Tkinter
# Import other modules as needed
# Default window Class
# Main function

# Importing everything from tkinter:
import tkinter as tk
# Importing other module(s) if needed:

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

# Leaving dormant as I cannot make it work correctly.
# Child Window function:
# class Window(tk.Toplevel):
#     """Provides a window with details needed."""

#     def __init__(self, parent):
#         super().__init__(parent)

#         self.geometry('200x120')
#         self.title("Run details:")
#         ttk.Button(self, text="Close", command=self.destroy).pack(expand=True)


# Class that holds all parts
class App:
    """The class holding all GUI components"""

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("FurBabyBoarding")

        def get_window():
            # clears the textbox on click:
            def clear_textbox(Event):
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

        # Create a button function:
        def buttoned(entry, foreground, background):
            self.button = tk.Button(self.master, text=f"{entry}", fg=f"{
                                    foreground}", bg=f"{background}", command=get_window)
            self.button.pack()
            return self.button

        # Create Detail Window function: # throws missing self.
        # def get_window(self):
        #     second_window = Window(self)
        #     second_window.grab_set()

        # Create a label
        self.label = tk.Label(self.master, text="Welcome to Hillside Animal\
 Hospital Boarding!", width=70, fg="white", bg="dark red")
        self.label.pack()

        # Create Buttons:
        self.button_1 = buttoned(f"Deluxe spots open: {
            runs().get('DELUXE')}", "white", "dark red")
        self.button_2 = buttoned(f"Suite spots open: {
            runs().get('SUITE')}", "white", "dark red")
        self.button_3 = buttoned(f"In&Out spots open: {
            runs().get('IN_OUT')}", "white", "dark red")
        self.button_4 = buttoned(f"Double run spots open: {
            runs().get('DOUBLE_RUN')}", "white", "dark red")
        self.button_5 = buttoned(f"Regular run spots open: {
            runs().get('REGULAR')}", "white", "dark red")

        # Used only for testing as I cannot get the Window class to work:
        # self.random = tk.Button(
        #     self.master, text="Testing extra window", command=get_window)
        # self.random.pack()


# Main function that starts the show:
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
