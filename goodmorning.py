import datetime

# Get the current timestamp
current_time = datetime.datetime.now().time()

# Extract the hour from the timestamp
current_hour = current_time.hour

# Convert the hour to 12-hour format
current_hour_12 = current_hour % 12 if current_hour % 12 != 0 else 12

# Get the AM/PM indicator
am_pm = "AM" if current_hour < 12 else "PM"

# Define the time ranges
morning_start = 6
afternoon_start = 12
evening_start = 18

# Check the current hour and wish accordingly
if morning_start <= current_hour < afternoon_start:
    greeting = "Good Morning"
elif afternoon_start <= current_hour < evening_start:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

# Print the greeting
print(f"{greeting}, it's {current_hour_12}:{current_time.minute:02d} {am_pm}!")
