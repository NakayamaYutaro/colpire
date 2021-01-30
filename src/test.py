import time                            # スリープを使うために必要
#import chromedriver_binary 
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/kao/stockTrade/chromedriver')
driver.get('https://www.google.com/')  # Googleを開く
time.sleep(5)                          # 5秒間待機
driver.quit()                          # ブラウザを閉じる
