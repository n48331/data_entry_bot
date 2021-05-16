from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import openpyxl

#Create a DATA sheet
book= openpyxl.load_workbook('data.xlsx')
sheet=book.active


#I used chocolatey to install chromedriver||choco install chromedriver
driver = webdriver.Chrome()
driver.get("YOUR-WEBSITE-LINK-HERE")
driver.maximize_window()

time.sleep(1)


#COPY xpath by inspecting and use it according to you

driver.find_element_by_xpath('XPATH-HERE').click()
dist = driver.find_element_by_xpath('XPATH-HERE/input')
dist.send_keys('TEXT'+ Keys.TAB * 2)

#REST ARE EXAMPLES-CHANGE IT ACCORDINGLY
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/a/span').click()
local = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div/div/input')
local.send_keys('f'+Keys.ENTER+Keys.TAB)



driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[4]/div/a/span').click()
poll = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[4]/div/div/div/input')
poll.send_keys('001'+ Keys.ENTER)

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[5]/fieldset/div/div[2]/label').click()
#A1,A3,A10 etc ARE CELL NAME
slno = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[7]/div/input')
slno.send_keys(sheet['A1'].value)

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[8]/div/div/a/span').click()
vt =driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[8]/div/div/div/div/input')
vt.send_keys(sheet['A2'].value + Keys.ENTER)

name = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[9]/div/input')
name.send_keys(sheet['A3'].value)

mname = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[10]/div/input')
mname.send_keys(sheet['A4'].value)

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[12]/div/div/a/span').click()
g = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[12]/div/div/div/div/input')
g.send_keys(sheet['A5'].value+ Keys.ENTER)

hno = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[13]/div/input')
hno.send_keys(sheet['A6'].value)

hname = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[16]/div/input')
hname.send_keys(sheet['A7'].value)

mhname = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[17]/div/input')
mhname.send_keys(sheet['A8'].value)

loc = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[19]/div/input')
loc.send_keys(sheet['A9'].value)

mloc =driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[20]/div/input')
mloc.send_keys(sheet['A10'].value)

po =driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[22]/div/input')
po.send_keys('TEXT')

mpo = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[23]/div/input')
mpo.send_keys('TEXT ')

pin = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[24]/div/input')
pin.send_keys('TEXT')

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[26]/div/input').click()
dob = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[26]/div/input')
dob.send_keys(Keys.BACKSPACE * 10 + sheet['A11'].value+Keys.TAB)

g = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[28]/div/input')
g.send_keys(sheet['A12'].value)

mg = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[29]/div/input')
mg.send_keys(sheet['A13'].value)

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[31]/div/div/a/span').click()
r = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[31]/div/div/div/div/input')
r.send_keys(sheet['A14'].value+ Keys.ENTER)

tal = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[32]/div/input')
tal.send_keys('TEXT')

mobile = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[33]/div/input')
mobile.send_keys(sheet['A15'].value)

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div/div/form/div[1]/div[35]/div/input').click()



