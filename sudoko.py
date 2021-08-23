from Board import Board
from pynput.keyboard import Key, Controller
import time
from selenium import webdriver   
from PIL import Image
import pytesseract
from selenium.webdriver.support.ui import WebDriverWait
import threading

driver = webdriver.Chrome(executable_path=r"C:\Users\shtil\Desktop\Sudoko Solver\chromedriver.exe")
driver.get("https://sudoku.com/")
time.sleep(1)
driver.execute_script('document.querySelector("#sudoku-wrapper > div.game-flex-wrapper > div.game-wrapper > div.game-tip").remove()')
element = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("game")).screenshot('canvas.png')
large_image = Image.open("canvas.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\shtil\Desktop\Sudoko Solver\Tesseract-OCR\tesseract.exe"

grid = Board()
index_x = 0
index_y = 0
threads = []

# The method receives an image and coords and OCR's it to a digit
def img_to_digit(im, indexy, indexx):
    txt = pytesseract.image_to_string(im, config="--psm 10")
    text1 = [int(s) for s in txt.split() if s.isdigit()]
    if len(text1) > 0:
        grid.board[indexy][indexx] = text1[0]
    else:
        grid.board[indexy][indexx] = 0

# Each thread gets 1 block from the board
for y in range(3, 500 - 55, 55):
    for x in range(3, 500 - 55, 55):
        image = large_image.crop((x + 5, y + 5, x + 50, y + 50))

        t1 = threading.Thread(target=img_to_digit, args=(image, index_y, index_x))
        threads.append(t1)
        index_x += 1
    index_y += 1
    index_x = 0

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(grid)

# Gets the full solution
_,x = grid.Solve()

def press(button):
    keyboard.press(button)
    keyboard.release(button)
    
keyboard = Controller()
for i in range(9):
    if i != 0:
        press(Key.down)
        press(Key.left)
        press(Key.left)
        press(Key.left)
        press(Key.left)
        press(Key.left)
        press(Key.left)
        press(Key.left)
        press(Key.left)
    for j in range(9):
        press(str(x[i][j]))
        press(Key.right)


input()
