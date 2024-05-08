from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://www.naver.com"
driver.get(url)
time.sleep(3)

driver.find_element(By.ID, "query").send_keys("인공지능")
# query = driver.find_element(By.NAME, "#query")
# query.send_keys("인공지능")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
# search_btn.click()
time.sleep(2)

driver.save_screenshot("naver_인공지능.png")
driver.quit()