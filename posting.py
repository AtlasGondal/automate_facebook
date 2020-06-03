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

# message to post
imsg = "Hello World!!!"     # CHANGE THIS

try:
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "email")))

    # login
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("pass").send_keys(ipass)
    browser.find_element_by_xpath("//*[@id='u_0_b']").click()

    # posting
    # identifier
    in_your_mind = "/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]"
    msg_box = "/html/body/div[1]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]"
    post_btn = "/html/body/div[1]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div"

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, in_your_mind)))
    browser.find_element_by_xpath(in_your_mind).click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, msg_box)))
    browser.find_element_by_xpath(msg_box).send_keys(imsg)
    browser.find_element_by_xpath(post_btn).click()

    browser.implicitly_wait(5)

    # logout
    browser.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[2]/div[4]/div[1]/span/div/div[1]").click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[5]/div/div[1]").click()
    print("Good Bye!!!")

except TimeoutException as te:
    print("Timeout exception. " + str(te))
    browser.close()

except NoSuchElementException as nsee:
    print("Maybe facebook layout structure is updated, or there's typo in path selector. " + str(nsee))
    browser.close()

finally:
    print("automated execution is completed, press ENTER key to quit")
    input()
    browser.close()
