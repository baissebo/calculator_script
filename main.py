import os
import pyautogui


def open_calculator():
    if os.name == "nt":
        os.system("start calc")
    elif os.name == "posix":
        os.system("open -a Calculator")
    else:
        os.system("gnome-calculator &")


def press_buttons():
    buttons = ["img/1.png", "img/2.png", "img/plus.png", "img/7.png", "img/equals.png"]

    for button in buttons:
        button_position = pyautogui.locateOnScreen(button, confidence=0.9)
        pyautogui.click(button_position)
        pyautogui.sleep(0.5)


if __name__ == "__main__":
    open_calculator()
    pyautogui.sleep(2)
    press_buttons()
