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
        try:
            button_position = pyautogui.locateOnScreen(button, confidence=0.9)
            if button_position:
                pyautogui.click(button_position)
                pyautogui.sleep(0.5)
            else:
                print(f"Кнопка '{button}' не найдена на экране.")
        except Exception as e:
            print(f"Произошла ошибка при обработке кнопки '{button}': {e}")


if __name__ == "__main__":
    open_calculator()
    pyautogui.sleep(2)
    press_buttons()
