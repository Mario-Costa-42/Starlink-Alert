# from bs4 import BeautifulSoup
# import requests

# html_text = requests.get('https://findstarlink.com/#3451668;3').text
# soup = BeautifulSoup(html_text, 'lxml')


# resultBox = soup.find_all('span', class_ = 'entryTiming bold')
# print(resultBox)

#Here I will be testing the webDriver shit with the selemiun libray

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
print("Extracted Text:", element.text)

# Regex pattern to extract time and date
pattern = r"(\d{1,2}:\d{2} (?:am|pm)), (\d{1,2} \w{3} \d{4})"

# Extract matches
matches = re.findall(pattern, element.text)

# Print results
for match in matches:
    print(f"Time: {match[0]}, Date: {match[1]}")










# Close the browser
driver.quit()
