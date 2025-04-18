import time

from XLUtils import *
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(4)
url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
# time.sleep(2)
file=r"OrangeHRM/test_cases.xlsx"
file2=r"OrangeHRM/BugReport.xlsx"
s1="Sheet1"

rows=getRowCount(file,s1)
cols=getColumnCount(file,s1)
print(rows,cols)
# time.sleep(2)
for r in range(2,rows+1):
    for c in range(7,9):
        username=readData(file,s1,r,7)
        password=readData(file,s1,r,8)
        expected=readData(file,s1,r,9)
        if c==7:
            driver.find_element(By.NAME,"username").send_keys(username)
            # time.sleep(1)
        elif c==8:
            driver.find_element(By.NAME,"password").send_keys(password)
            # time.sleep(1)

            driver.find_element(By.XPATH,"//button[@type='submit']").click()

            if expected=="Required":
                act=driver.find_element(By.XPATH,"//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]").text
                print(act)
            elif expected=="Dashboard":
                # time.sleep(2)
                act=driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
            else:
                act=driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text


            if expected==act:
                fillGreenColor(file2,s1,r,11)
                writeData(file2,s1,r,11,"passed")
            else:
                fillRedColor(file2,s1,r,11)
                writeData(file2,s1,r,11,"Failed")
            print(f"test {r-1} done")

print("Go, and check Exl File")