from itertools import cycle
import numpy as np

from eulerutil.number_theory import divides

def leapyear(year: int) -> bool:
    return divides(400, year) or (divides(4, year) and not divides(100, year))

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days_of_year = [j+1 for i in months for j in range(i)]
year_1900 = list(zip(days_of_year, cycle(weekdays)))

count = 0
monday_offset = 1
for year in range(1901, 2001):
    months[1] = 29 if leapyear(year) else 28
    csum, csumindex = np.cumsum(months), 0
    for day in range(1, csum[-1] + 1):
        if day % csum[csumindex - 1] == 1:
            if weekdays[(monday_offset + day - 1) % 7] == 'Sunday': 
                count += 1
        if day == csum[csumindex]:
            csumindex += 1
    monday_offset += 2 if leapyear(year) else 1

        

