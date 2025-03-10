from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Use webdriver.Firefox() if using Firefox
driver.get("https://findstarlink.com/#3451668;3")  # Replace with your actual URL

# Wait for JavaScript to load the content
time.sleep(6)  # Adjust sleep time if needed

# Find the element by class name
element = driver.find_element(By.ID, "avgTimings") #change for the good visialização later 
#print("Extracted Text:", element.text)

# Regex pattern to extract time and date
# pattern = r"(\d{1,2}:\d{2} (?:am|pm)), (\d{1,2} \w{3} \d{4})"

# Extract matches
# matches = re.findall(pattern, element.text)

# Print results
# for match in matches:
#     print(f"Time: {match[0]}, Date: {match[1]}")

# Regex patterns
date_time_pattern = r"(\d{1,2}:\d{2} (?:am|pm)), (\d{1,2} \w{3} \d{4})"
duration_pattern = r"for (\d+) mins"
direction_pattern = r"Look from (\w+) to (\w+)"
elevation_pattern = r"Elevation \(from horizon\): start: (\d+)°, max: (\d+)°, end: (\d+)°"

# Extract matches
date_time_matches = re.findall(date_time_pattern, element.text)
duration_matches = re.findall(duration_pattern, element.text)
direction_matches = re.findall(direction_pattern, element.text)
elevation_matches = re.findall(elevation_pattern, element.text)

# Print extracted information
for i in range(len(date_time_matches)):
    time, date = date_time_matches[i]
    duration = duration_matches[i] if i < len(duration_matches) else "N/A"
    direction_from, direction_to = direction_matches[i] if i < len(direction_matches) else ("N/A", "N/A")
    elevation_start, elevation_max, elevation_end = elevation_matches[i] if i < len(elevation_matches) else ("N/A", "N/A", "N/A")

    print(f"Time: {time}, Date: {date}")
    print(f"Duration: {duration} mins")
    print(f"Viewing Direction: {direction_from} to {direction_to}")
    print(f"Elevation: Start {elevation_start}°, Max {elevation_max}°, End {elevation_end}°")
    print("-" * 50)








# Close the browser
driver.quit()
