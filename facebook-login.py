from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
try:
    usr = "95020170" 
    pwd = "Nyamka0127"

    driver = None

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://erp.e-mongolia.mn/login')

    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Нэвтрэх нэр']")
    username_field.send_keys(usr)   
    sleep(1)

    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Нууц үг']")
    password_field.send_keys(pwd)
    print("Password entered")
    wait = WebDriverWait(driver, 10)

    login_button = driver.find_element(By.CSS_SELECTOR, "button.el-button.enterButton.el-button--primary.el-button--small span")
    driver.execute_script("arguments[0].click();", login_button)

    WebDriverWait(driver, 10).until(EC.url_contains("https://erp.e-mongolia.mn/"))
    print("Login successful, redirected to:", driver.current_url)

    burtguuleh_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-button.el-button--success.el-button--small span"))
    )
    
    driver.execute_script("arguments[0].click();", burtguuleh_button)

    sleep(10)

except Exception as e:
    print("The error raised is: ", e)

finally:
    if 'driver' in locals() and driver is not None:
        sleep(12)
        driver.quit()
        print("Driver quit successfully.")
