import os
import time
import pyautogui
from PIL import Image

# 저장할 경로 저장하기
path = r"C:\ScreenCaptured"

while True:
    # 현재 화면을 캡처하여 Image 객체로 가져오기
    screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    # JPEG 이미지로 변환하여 파일로 저장하기
    filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
    # screenshot.save(filename, format="JPEG", quality=95)
    screenshot.save(os.path.join(path, filename), format="JPEG", quality=100)
    # 10초 대기
    time.sleep(10)

