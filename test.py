from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


explorer = webdriver.Edge(executable_path='msedgedriver.exe')
explorer.get('http://courses.cuc.edu.cn/user/index/')

sleep(2)



print(QRcode)
sleep(20)
