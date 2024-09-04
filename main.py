from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:\BrowserDrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open the Amazon login page
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com"
           "%2Fcustomer-preferences%2Fedit%3Fie%3DUTF8%26preferencesReturnUrl%3D%252F%26ref_%3Dnav_signin&openid"
           ".identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex"
           "&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
           "%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


# enter email
user_email = driver.find_element(By.ID, "ap_email")
user_email.send_keys("aamina@email.com")

time.sleep(10)

# select continue button
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

time.sleep(10)

# enter password
user_password = driver.find_element(By.ID, "ap_password")
user_password.send_keys("Aamina@121")

time.sleep(10)

# Click the 'Sign In' button
sign_in_button = driver.find_element(By.ID, "signInSubmit")
sign_in_button.click()

# to print sign in status
print(driver.title)

# Close the WebDriver
driver.quit()

