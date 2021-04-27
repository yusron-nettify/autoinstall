from selenium import webdriver
from selenium.webdriver.chrome.options import Options



option = Options()
option.add_argument("--autoplay-policy=no-user-gesture-required")
option.add_argument("--use-fake-ui-for-media-stream")
option.add_argument("--incognito")
# option.add_argument("--kiosk")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(executable_path="/snap/bin/chromium.chromedriver", options=option)