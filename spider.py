import time
import csv
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def Crewling():
    driver = webdriver.Chrome()
    url = 'https://maoyan.com/board/4?offset=0'
    driver.get(url)
    time.sleep(2)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/ul/li[2]/a'))
        )
        if element:
            """打开文件"""
            file = open('data.csv', 'a+', newline='', encoding='utf-8')
            f = csv.writer(file)
            for i in range(10):
                for j in range(1, 11):
                    movie = '//*[@id="app"]/div/div/div[1]/dl/dd[' + str(j) + ']/div/div/div[1]/p[1]/a'
                    m = driver.find_element_by_xpath(movie).text

                    actors = '//*[@id="app"]/div/div/div[1]/dl/dd[' + str(j) + ']/div/div/div[1]/p[2]'
                    a = driver.find_element_by_xpath(actors).text

                    integet = '//*[@id="app"]/div/div/div[1]/dl/dd[' + str(j)+ ']/div/div/div[2]/p/i[1]'
                    inte = driver.find_element_by_xpath(integet).text
                    fraction = '//*[@id="app"]/div/div/div[1]/dl/dd[' + str(j) + ']/div/div/div[2]/p/i[2]'
                    frac = driver.find_element_by_xpath(fraction).text
                    score = inte + frac

                    """进入二级页面找简介"""
                    content = '//*[@id="app"]/div/div/div[1]/dl/dd[' + str(j) + ']/a'
                    driver.find_element_by_xpath(content).click()
                    time.sleep(3)
                    introduction = '//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span'
                    intro = driver.find_element_by_xpath(introduction).text
                    """返回一级页面"""
                    driver.back()
                    time.sleep(3)

                    text = [m, a, score, intro]
                    f.writerow(text)
                
                print("完成第{}页信息收集".format(i+1))
                next_page = '//*[@id="app"]/div/div/div[2]/ul/li[last()]/a'
                driver.find_element_by_xpath(next_page).click()
                time.sleep(3)

            file.close()
    finally:
        driver.quit()
