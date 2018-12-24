from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import pickle
from proxylist import ProxyList

pl = ProxyList()
pl.load_file('./web/proxy.txt')
proxy = pl.random().address()
print(proxy[1:-5])

from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = proxy
prox.socks_proxy = proxy
prox.ssl_proxy = proxy

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = '/usr/bin/firefox'

# chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium")

# driver = webdriver.Firefox(capabilities=firefox_capabilities)
# driver = webdriver.Firefox(capabilities=firefox_capabilities ,firefox_options=chrome_options)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=100,100")
# chrome_options.add_argument("user-data-dir=selenium")


def my_proxy(PROXY_HOST, PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    print
    PROXY_PORT
    print
    PROXY_HOST
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", PROXY_HOST)
    fp.set_preference("network.proxy.http_port", int(PROXY_PORT))
    fp.set_preference("general.useragent.override", "whater_useragent")
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp)


webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
}
# driver = webdriver.Chrome(chrome_options=chrome_options,desired_capabilities=capabilities)
# driver = my_proxy("64.132.98.60","80")
# you have to use remote, otherwise you'll have to code it yourself in python to
# driver = webdriver.Remote("https://www.aparat.com/v/aQfED", webdriver.DesiredCapabilities.CHROME)


# import browsercookie
#
# cookies1 = browsercookie.firefox()
# driver.add_cookie(cookies)

import time
import threading


exitFlag = 0


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print ("Starting " + self.name)
      i = 0
      driver = webdriver.Chrome(options=chrome_options)
      # driver.set_page_load_timeout(10000000)

      # driver.implicitly_wait(3000)
      # driver.get("https://www.aparat.com/Gho3tShadow/live")
      # time.sleep(100)

      while 1:
          driver = webdriver.Chrome(options=chrome_options)
          # print("a")
          # driver.get("https://www.khodrobank.com/TestDrive/12574/6-%D8%B3%DB%8C%D9%84%D9%86%D8%AF%D8%B1-%DA%98%D8%A7%D9%BE%D9%86%DB%8C-%D8%AF%D8%B1-%D8%A8%D8%B1%D8%A7%D8%A8%D8%B1-4-%D8%B3%DB%8C%D9%84%D9%86%D8%AF%D8%B1-%DA%A9%D8%B1%D9%87-%D8%A7%DB%8C%D8%9B-%D8%A8%D8%B1%D8%B1%D8%B3%DB%8C-%D8%AF%D9%88-%DA%A9%D8%B1%D8%A7%D8%B3-%D8%A7%D9%88%D9%88%D8%B1-%D8%AF%D8%B3%D8%AA-%D8%AF%D9%88%D9%85-%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1")
          driver.get("https://www.aparat.com/v/aQfED")
          # driver.get("https://cafebazaar.ir/app/shayan.app.applock/")
          time.sleep(5)
          driver.close()
          print(i)
          i+=1
      print ("Exiting " + self.name)






threads = []
for o in range(0, 10):
# for o in range(0, 2):
 threads.append(myThread(1, "Thread-1", 1))
 threads[o].start()



    # for o in range(0, 10):
    #     # Create new threads
    #
    #
    #     thread2 = myThread(2, "Thread-2", 2,webdriver.Chrome())
    #
    #     # Start new Threads
    #     thread1.start()
    #     thread2.start()
    #
    #     # driver =
    #     driver.append(webdriver.Chrome())
    #     driver[o].get("https://www.aparat.com/v/aQfED")
    #     print("AAA1")
    #
    # print("AAA2")
    # time.sleep(2)
    # for ip in driver:
    #  ip.close()

    # img = driver.find_element(By.ID,"cimg1").find_element(By.TAG_NAME,"img")
    # src = img.get_attribute("src");
    # number1 = src.split("/")[-1].split(".")[0]
    #
    # img = driver.find_element(By.ID,"cimg2").find_element(By.TAG_NAME,"img")
    # src = img.get_attribute("src");
    # number2 = src.split("/")[-1].split(".")[0]
    #
    # img = driver.find_element(By.ID,"cimg3").find_element(By.TAG_NAME,"img")
    # src = img.get_attribute("src");
    # number3 = src.split("/")[-1].split(".")[0]
    #
    # img = driver.find_element(By.ID,"cimg4").find_element(By.TAG_NAME,"img")
    # src = img.get_attribute("src");
    # number4 = src.split("/")[-1].split(".")[0]
    # mynumber = int(number1+number2+number3+number4)
    #
    # # driver.execute_script("document.getElementsByTagName('input')[0].value='jjj'")
    # driver.execute_script("document.getElementsByTagName('input')[0].value="+str(mynumber)+"")
    # driver.execute_script("javascript:dosub()")
    # time.sleep(5)
