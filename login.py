from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


# for chrome
# browser = webdriver.Chrome()

# if selenium path is not configure then pass driver path as an argument like this:
# browser = webdriver.Firefox(executable_path=EXE_PATH)
browser = webdriver.Firefox()

browser.get("https://www.facebook.com/")

# form data
email = "XXXXXXXXXXX"		# CHANGE THIS
ipass = "XXXXXXXXXXX"		# CHANGE THIS

try:
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "email")))

    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("pass").send_keys(ipass)
    browser.find_element_by_xpath("//*[@id='u_0_b']").click()

except TimeoutException as te:
    print("Timeout exception. " + str(te))
    browser.close()

except NoSuchElementException as nsee:
    print("Maybe facebook login structure is changed, or there's typo in path selector. " + str(nsee))
    browser.close()

except WebDriverException as wde:
    print("Unable to locate driver. " + str(wde))
    browser.close()

finally:
    input()
    browser.close()
