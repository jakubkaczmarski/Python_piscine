import time
import datetime
import calendar

date = datetime.date.today()
now = time.time()

print("Seconds since January 1, 1970:",
      f"{now:,.4f}", " or ", f"{now:.2e}", " in scientific notation")
print(f"{calendar.month_name[10] :.3}", date.day, date.year)
