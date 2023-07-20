from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
import os


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://localhost/form/form.php')


def sendBruteForce(number):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#cpfInput')))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#cpfInput')))

    inputCpf = driver.find_element(By.CSS_SELECTOR, '#cpfInput')
    inputCpf.click()
    inputCpf.send_keys(number)


def clickInButton():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#form > button')))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#form > button')))

    driver.find_element(By.CSS_SELECTOR, '#form > button').click()


def verifyAlert():
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        Alert(driver).accept()
        return True
    except:
        return False


def verifyIsGenareted():
    sleep(2)
    download_path = 'C:\\Users\\lucia\\Downloads\\certificado.pdf'
    if os.path.exists(download_path):
        return True


number = 22222222110

while True:
    sendBruteForce(number)
    clickInButton()
    if verifyAlert():
        print(f"Numero da tentativa ---- {number}")
        number += 1
    # elif verifyIsGenareted():
    #     print(f"Achou certificado no cpf: {number}")
    #     sleep(100)
    #     number += 1
    # else:
    #     sleep(3)
    #     print("Falha")
