import keyboard
import pyautogui as pag

def main():
	x, y = pag.position()
	pag.rightClick(x, y)
	pag.moveRel(0, -40)
	# pag.doubleClick(x, y)
	pag.click(x, y)

keyboard.add_hotkey('F', main)
keyboard.wait('Esc') # Exit script