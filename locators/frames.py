import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get("https://www.linkedin.com")
time.sleep(2)
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(google_frame)
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)
driver.switch_to.parent_frame()
time.sleep(2)
ref_ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac.scroll_to_element(ref_ele).perform()
time.sleep(2)
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
