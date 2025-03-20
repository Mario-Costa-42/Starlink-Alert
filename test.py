from datetime import datetime

date_string = "Time: 4:58 am\nDate: 23 Mar 2025"

# Extract the time and date part separately
lines = date_string.split("\n")
time_part = lines[0].replace("Time: ", "").strip()
date_part = lines[1].replace("Date: ", "").strip()

# Combine them into a single string
datetime_string = f"{date_part} {time_part}"
print(datetime_string)

# Convert to datetime object
date_object = datetime.strptime(datetime_string, "%d %b %Y %I:%M %p")

print(date_object)  # Output: 2025-03-23 04:58:00
