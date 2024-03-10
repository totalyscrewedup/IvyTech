"""
Program: MyProgram.py
Author: Tomi Simic
Last date modified: 2024-03-09 
This program is used to test FurBabyBoarding application. Specifically,
testing the user verification aspect of the application.
"""
# Pseudo code:
# import GUI needed module
# import other module(s)
# create class that verifies for all possible user type and logic errors

# Importing everything from tkinter:
import tkinter as tk
# Importing other module(s):
import datetime

# User input validation:


class UserInput:
    """Verifying inputs provided by the user"""

    def prompts(self):
        """Jumpbox for prompts needed during verification process"""
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
            "old_day": "The day value cannot be in the past."
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
            prompt = input(
                f"When is the client checking out? (i.e.: {now.month}-\
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

    def __str__(self):
        return str(self.date_format())


print(UserInput())
