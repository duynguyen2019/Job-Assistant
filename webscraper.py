from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280,1000')
chrome_options.add_argument('--allow-insecure-localhost')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--no-sandbox')
print("Initiate Chrome Driver")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)

url = 'https://www.google.com'
print(f"Navigating to {url}")
driver.get(url)

search_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_text = "La La La"
print(f"Searching Google for {search_text}")

search_box.send_keys(search_text)
click_search = driver.find_element_by_css_selector('.FPdoLc > center:nth-child(1) > input:nth-child(1)')

# click_search = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
#                              (By.CSS_SELECTOR, '.FPdoLc > center:nth-child(1) > input:nth-child(1)')
#                                                                                 )           
#                                                                                 )
print("Clicking the Search button")
driver.execute_script("arguments[0].click();", click_search)