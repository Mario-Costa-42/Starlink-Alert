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

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Use webdriver.Firefox() if using Firefox
driver.get("https://findstarlink.com/#3451668;3")  # Replace with your actual URL

# Wait for JavaScript to load the content
time.sleep(6)  # Adjust sleep time if needed

# Find the element by class name
element = driver.find_element(By.CLASS_NAME, "timingEntry")
print("Extracted Text:", element.text)

# Close the browser
driver.quit()
