# Question: Make a script that prints out the current day and time.
# For example Today is Sunday, December 25, 2016.

import datetime

today = datetime.date.today()
print(f"Today is {today.strftime('%A')}, {today.strftime('%B')} {today.day}, {today.year}.")

from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y."))
