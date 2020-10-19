# import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from send_sms import send_text


def send_notification():
    body = 'update: \n'
    # construct message body
    for day, value in availabilities.items():
        if value != 'AvailabilityFull.':
            body += f'\navailability at slot: {day}. ({value})\n'
        else:
            body += f'\nno availability at slot: {day}. ({value})\n'

    send_text(body)


href = "https://app.rockgympro.com/b/widget/?a=offering&offering_guid=5e6292b94ab14ce892b4faedc708faa5&widget_guid=e3778ccd21d04e568279fcd4b06112ec&random=5f8d7a55505df&iframeid=rgpiframe5f8d7a54f0388&mode=e#"
DRIVER_PATH = "C:/Users/Richard/Documents/coding/chromedriver/chromedriver.exe"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

print('beginning web scrape...')

with webdriver.Chrome(executable_path=DRIVER_PATH, options=options) as driver:
    driver.get(href)
    soup = BeautifulSoup(driver.page_source, 'html.parser')


table = soup.find_all('table', id="offering-page-select-events-table")[0]
tableRow = table.find_all('tr')

# init empty availabilities dictionary
availabilities = {}

for i, row in enumerate(tableRow):
    # temp, ignore the first slot of 16:00 to 17:50
    # if i == 0:
    #     continue
    day = row.find('td', class_="offering-page-schedule-list-time-column").text.split('\n')[1]
    value = row.find_all('td')[1].text.split('\n')[1].split('\xa0')[0]
    availabilities[day] = value


# print(availabilities)

# check if there are any available slots
for i, value in enumerate(availabilities.values()):
    # temp, ignore availability for the 16:00 - 17:50 slot
    # if i == 0:
    #     continue
    if value != 'AvailabilityFull.':
        send_notification()
        break
