import time
import pyautogui
from PIL import Image

while True:
    # 현재 화면을 캡쳐하여 Image 객체로 가져오기
    screenshot = pyautogui.screenshot()
    # 파일명에 현재 시각 포함하여 저장하기
    filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
    screenshot.save(filename)
    # 1분 대기
    time.sleep(60)