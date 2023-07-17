#Gerekli kütüphaneleri ve modülleri içe aktarıyoruz:

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#Selenium'u kullanarak Chrome WebDriver'ı başlatıyoruz ve PATH ortam değişkenine ChromeDriver'ın yolunu ekliyoruz:

os.environ['PATH'] += r"C:\selenyumdireve"
driver = webdriver.Chrome()

#Tarayıcının açılmasını istediğimiz web sayfasını belirliyoruz:
driver.get("https:......")

#Bir döngü kullanarak sayfayı aşağı kaydırıyoruz ve verileri işleyebileceğimiz veya istediğimiz işlemleri yapabileceğimiz bir noktada durduruyoruz:
while True:
    # Sayfanın HTML kodunu alın
    html = driver.page_source

    # BeautifulSoup ile HTML kodunu ayrıştırın
    soup = BeautifulSoup(html, "html.parser")

    # Verileri işleyin veya istediğiniz şeyleri yapın
    # ...

    # Sayfayı aşağı kaydırmak için bir kez "Page Down" tuşuna basın
    driver.find_element("xpath", 'Sayfadan XPath kopyasını buraya yapıştır.').send_keys(Keys.PAGE_DOWN)

    #BeautifulSoup kullanarak sayfadaki belirli bir div öğesini buluyoruz:
    div_element1 = soup.find("div", class_=".....classın adı .........")# "class adı" sınıfına sahip bir div öğesini buluyoruz.
    inner_divs = div_element1.find('div', class_='....class adı 2................')# içerisindeki "class adı 2" sınıfına sahip div öğesini inner_divs değişkenine atıyoruz.

    # "inner_divs" öğesini düzenleyerek ve temizlenmemiş-link.txt adlı bir dosyaya yazarak verileri kaydediyoruz:
    aa = inner_divs.prettify() 
    #"prettify()" metodu, BeautifulSoup nesnesini düzenli bir şekilde metin formatına dönüştürür. Bu metni temizlenmemiş-link.txt adlı dosyaya ekliyoruz.

    with open("temizlenmemiş-link.txt", "a", encoding="utf-8") as dosya:
        dosya.write(str(aa) + "\n")


