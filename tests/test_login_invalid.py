from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_manual_login_check():
    # ChromeDriver yolunu doğru şekilde belirt
    service = Service("C:/Users/Public/Soru_5/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Sayfayı aç
    driver.get("https://the-internet.herokuapp.com/login")

    print("✅ Sayfa açıldı! Lütfen giriş bilgilerini girin ve Giriş butonuna tıklayın.")
    input("Giriş yaptıktan sonra ENTER tuşuna basın...")

    time.sleep(2)

    try:
        error_message = driver.find_element(By.ID, "flash").text
        if "invalid" in error_message:
            print("❌ Hatalı giriş yapıldı.")
        elif "You logged into a secure area!" in error_message:
            print("✅ Başarılı giriş yapıldı.")
        else:
            print("ℹ️ Bilinmeyen yanıt:", error_message)
    except:
        print("⚠️ Herhangi bir mesaj bulunamadı.")

    driver.save_screenshot("test-sonucu.png")
    input("Kapatmak için ENTER tuşuna bas...")
    driver.quit()

test_manual_login_check()
