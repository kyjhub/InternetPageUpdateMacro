from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys
from tkinter import *
import threading
import sys

# 루트화면 생성
tk = Tk()
tk.title("새로고침 매크로")
# http://www.gcnuri.or.kr/
# http://www.gcnuri.or.kr/bbs/board.php?bo_table=s3_1&wr_id=3944&sca=%EC%98%88%EC%82%B0+%EA%B3%B5%EC%8B%9C&sfl=wr_subject&stx=2023%EB%85%84&sop=and
def inputAndUpdate():
    homePage = str(hp.get())
    updateSite = str(bs.get())

    # 옵션 설정
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.use_chromium = True
    options.add_experimental_option("detach", True)

    # Edge 파일 위치 설정
    options.binary_location = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    s = service.Service(r"C:\study\browser_driver\edgedriver_win64\msedgedriver.exe")

    # Edge 드라이버 생성
    driver = webdriver.Edge(options=options, service=s)
    # Edge 추적 방지 엄격으로 전환
    driver.get("edge://settings/privacy")
    driver.refresh()
    driver.find_element(By.XPATH, "//*[@id='엄격']").click()

    # Edge 쿠키 차단 사이트 설정
    driver.get("edge://settings/content/cookies")
    driver.refresh()
    driver.find_element(By.XPATH, "//*[@id='CookiesAddblock']/span").click()
    inputBlockSite = driver.find_element(By.ID, "sitePermissionUrl")
    inputBlockSite.send_keys(homePage)
    driver.implicitly_wait(0.1)
    driver.find_element(By.XPATH,
                        "//*[@id='modal-root']/div/div/div/div[2]/div/div[2]/div/form/div[2]/button[1]").click()

    # 내가 지정한 url로 접속
    driver.get(updateSite)
    for _ in range(50):  # 새로고침할 횟수 지정
        driver.refresh()

    print("50번 새로고침 끝")

def execute():
    thread = threading.Thread(target=inputAndUpdate)
    thread.start()

label1 = Label(tk, text="대표 홈페이지 주소").grid(row=0, column=0)
label2 = Label(tk, text="새로고침할 주소").grid(row=1, column=0)

hp = Entry(tk)
bs = Entry(tk)
hp.grid(row=0, column=1)
bs.grid(row=1, column=1)

btn1 = Button(tk, text="확인", command=execute).grid(row=2, column=1)
tk.mainloop()

sys.exit()


