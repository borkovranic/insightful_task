import time

from pywinauto import findwindows
from pywinauto.application import Application
from utils.logger import logger


def get_calculator():
    Application(backend='uia').start("calc.exe")
    for i in range(5):
        try:
            app_w = Application(backend='uia').connect(title_re=".*Calculator.*")
            calculator_window = app_w.top_window()
            calculator_window.set_focus()
            logger.info("Calculator app is found...")
            return calculator_window
        except:
            logger.info("Calculator app is not yet ready...")
        time.sleep(0.3)


def close_multiple_calculator_windows():
    try:
        calc_windows = findwindows.find_windows(title_re=".*Calculator.*")
        if not calc_windows:
            logger.info("No calculator windows found.")
            return
        for hwnd in calc_windows:
            app = Application(backend='uia').connect(handle=hwnd)
            calc_window = app.window(handle=hwnd)
            calc_window.close()
            logger.info("Calculator window closed.")
    except Exception as e:
        logger.error(f"Failed to close all calculator windows: {e}")
