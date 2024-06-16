from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys

# 옵션 설정
options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.use_chromium = True
options.add_experimental_option("detach", True)

# Edge 파일 위치 설정
options.binary_location = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
s = service.Service(r"C:\study\browser_driver\edgedriver_win64\msedgedriver.exe")

# Edge 드라이버 생성
driver = webdriver.Edge(options=options, service = s)

# Edge 추적 방지 엄격으로 전환
driver.get("edge://settings/privacy")
driver.refresh()
driver.find_element(By.XPATH, "//*[@id='엄격']").click()

#Edge 쿠키 차단 사이트 설정
driver.get("edge://settings/content/cookies")
driver.refresh()
driver.find_element(By.XPATH, "//*[@id='CookiesAddblock']/span").click()
inputBlockSite = driver.find_element(By.ID, "sitePermissionUrl")
inputBlockSite.send_keys("새로고침할 페이지의 대표주소이자 모주소")
driver.implicitly_wait(0.1)
driver.find_element(By.XPATH, "//*[@id='modal-root']/div/div/div/div[2]/div/div[2]/div/form/div[2]/button[1]").click()

# 내가 지정한 url로 접속
driver.get('새로고침할 주소')
for _ in range(2000):   # 새로고침할 횟수 지정
    driver.refresh()


print("2천번 새로고침 끝")


