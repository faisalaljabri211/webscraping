from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔧 إعداد المتصفح
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 🌐 فتح موقع الهيئة
driver.get("https://www.ca-oman.com/")

# 🕒 الانتظار لعرض الصفحة
time.sleep(5)

# 🖨️ طباعة عنوان الصفحة
print("Page Title:", driver.title)

# ❌ إغلاق المتصفح
driver.quit()
