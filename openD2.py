import pyautogui
import subprocess
import time
from datetime import date
import cloudscraper
from bs4 import BeautifulSoup

def clickWhenYouSee(imageFile):
    location = None
    while (location == None):
        try:
            location = pyautogui.locateCenterOnScreen(imageFile, confidence=0.9)
            print(f"could not locate {imageFile}")
        except Exception as e:
            print(e)
        time.sleep(1)
    print(f"found {imageFile} at {location.x}, {location.y}")
    pyautogui.click(location)

scraper = cloudscraper.create_scraper()

while(True):
	page = scraper.get('https://diablo2.io/dclonetracker.php?sk=p&sd=d&ladder=2&hc=2&xc=1')
	soup = BeautifulSoup(page.text, 'html.parser')
	servers = []
	for tr in soup.find_all('tr'):
		cell = tr.find_all('span','zi')
		code = tr.find_all('code')
		if(len(cell) and len(code)):
			info = (cell[0]['title'], code[0].getText())
			servers.append(info)
			print(f"{info[0]} {info[1]}")
	print()

    #DEBUG
    #servers = [("Europe","5/6"),("Americas","1/6"),("Asia 1/6")]
    #servers = [("Europe","4/6"),("Americas","5/6"),("Asia 1/6")]
    #servers = [("Europe","3/6"),("Americas","1/6"),("Asia 5/6")]
    
	if(any("5" in item[1] for item in servers)):
		region = [s[0] for s in servers if "5" in s[1]][0]
		print(f"WE IN IT TO WIN IT IN {region.upper()} BOIZ!!!")
		openMe = "C:\Program Files (x86)\Diablo II Resurrected\Diablo II Resurrected Launcher.exe"
		subprocess.call([openMe])

		clickWhenYouSee('RegionButton.png')
		clickWhenYouSee(f'{region}.png')
		clickWhenYouSee('PlayButton.png')
		time.sleep(9)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.press('enter')
		clickWhenYouSee('PressAnyKey.png')
		clickWhenYouSee('OtherPlayButton.png')
		clickWhenYouSee('HellButton.png')
		exit()
    
	time.sleep(300)
