import pyautogui
from datetime import datetime
import os
import csv
import time
from pprint import pprint
import shutil
from playsound import playsound
import threading
import keyboard


class AutoExport:

    def __init__(self):

        # ADJUST THIS TO ALLOW FOR SLOWER OR FASTER MOVEMENTS
        # DELAY MAY NEED TO BE INCREASED BASED ON INTERNET SPEED AND AGGREGATION/LENGTH OF CHARTS
        # THIS IS NEEDED BECAUSE SOMETIMES THE CHARTS DO NOT LOAD FAST ENOUGH
        self.delay = 0.15  # 0.15

        # THIS IS THE WATCHLIST FILE FROM TOS, WHICH IS FORMATED WITH THE CURRENT DATE OF WHICH DOWNLOADED
        self.watchlist_file = f"{datetime.now().strftime('%Y-%m-%d')}-watchlist.csv"

        # PATH TO USERS DOCUMENTS FOLDER. THIS IS WHERE TOS DOWNLOADS THE STRATEGY REPORTS
        self.path = "C:/Users/TreyT/Documents"

        # TOTAL NUMBER OF SYMBOLS IN WATCHLIST
        self.watchlist_length = 0

        # ADDED CONDITIONAL FOR THE WHILE LOOP.
        # IF ERROR, ATTRIBUTE WILL BE SET TO FALSE AND WHILE LOOP WILL STOP
        self.no_error = True

    def throwError(self, error):

        self.no_error = False

        for _ in range(3):

            playsound('audio/error.mp3')

        print(error)

        # REMOVE ALL EXISTING CSV FILES FROM DOCUMENTS FOLDER
        for file in os.listdir(self.path):

            sep = file.split("_")

            if file.endswith(".csv") and sep[0].strip() == "StrategyReports":

                os.remove(file)

    def checkHotKey(self):

        while self.no_error:

            try:

                if keyboard.is_pressed('ctrl+c'):

                    self.throwError(
                        "CTRL C PRESSED - STOPPING PROGRAM - PLEASE RESTART")

            except Exception as e:

                print(e)

    def getWatchlist(self):

        pyautogui.click(282, 144)

        time.sleep(self.delay)

        pyautogui.move(0, 155)

        pyautogui.click()

        time.sleep(self.delay)

        pyautogui.move(500, 215)

        time.sleep(self.delay)

        pyautogui.click()

        time.sleep(self.delay)

        if os.path.exists(self.watchlist_file):

            print("FOUND WATCHLIST!")

            with open(self.watchlist_file, "r") as watchlist:

                reader = csv.reader(watchlist)

                # THESE 4 NEXTS START THE ITERATION AT THE NEEDED ROWS WITH THE SYMBOL DATA
                # MAY NEED TO BE ADJUSTED BASED ON USERS NEEDS
                next(reader)
                next(reader)
                next(reader)
                next(reader)

                for row in reader:

                    self.watchlist_length += 1

            os.remove(self.watchlist_file)

            # SUBTRACT ALREADY EXISTING COUNT IN CSV FILES DIRECTORY FROM WATCHLIST LENGTH
            self.watchlist_length -= len(
                [file for file in os.listdir("csv_files")])

            print("SYMBOLS EXTRACTED FROM WATCHLIST!\n")

            print("BEGINNING AUTO EXPORTS....")

            time.sleep(5)

            self.start()

    def moveCSVFile(self):

        # ABSOLUTE PATH TO CSV_FILES DIRECTORY
        dst_dir = "C:/Users/TreyT/Desktop/AlgoTrading/TOS_Auto_Export/csv_files"

        for root, dirs, files in os.walk(self.path):

            for f in files:

                sep = f.split("_")

                if f.endswith('.csv') and sep[0].strip() == "StrategyReports":

                    shutil.move(os.path.join(root, f), dst_dir)

                    self.watchlist_length -= 1

                    return

        # IF MISS, THROW ERROR

        self.throwError("MISSED EXPORT - STOPPING PROGRAM - PLEASE RESTART")

    def start(self):

        threading.Thread(target=self.checkHotKey, daemon=True).start()

        start = time.perf_counter()

        # GET THE SIZE OF THE MONITOR THAT WILL DISPLAY THE TOS APP
        screen_width, screen_length = pyautogui.size()

        # START_X AND START_Y ARE BOTH WHERE THE MOUSE ARROW WILL START ON SCREEN.
        # THIS SHOULD BE PLACED WHERE THE CHART IS TO BE ABLE TO GET THE REPORTS.
        # WILL NEED TO BE ADJUSTED BASED ON SCREEN SIZE
        start_x = int(screen_width / 2.660194174757281)
        start_y = int(screen_length / 1.728)

        while self.watchlist_length != 0 and self.no_error:

            # show report
            pyautogui.rightClick(start_x, start_y)

            time.sleep(self.delay)

            pyautogui.move(30, 90)

            time.sleep(self.delay + 0.25)

            pyautogui.click()

            # export
            pyautogui.move(520, 40)

            time.sleep(self.delay)

            pyautogui.click()

            # save
            pyautogui.move(-160, -90)

            time.sleep(self.delay)

            pyautogui.click()

            # # overwrite
            # pyautogui.move(-85, -575)

            # time.sleep(self.delay)

            # pyautogui.click()

            time.sleep(self.delay)

            # close
            pyautogui.move(200, 100)

            time.sleep(self.delay)

            pyautogui.click()

            time.sleep(self.delay)

            # next symbol
            pyautogui.press(['down'])

            time.sleep(self.delay + .3)

            ###############
            self.moveCSVFile()

            if self.no_error:

                middle = time.perf_counter()

                running_time = time.strftime(
                    '%H:%M:%S', time.gmtime(middle - start))

                print(
                    f"REMAINING --> {self.watchlist_length} | RUNNING TIME: {running_time} | EST. TIME REMAINING: N/A")

        if self.no_error:

            end = time.perf_counter()

            # FINISHED

            print("\nFINISHED!")

            playsound("audio/alert_on_call.mp3")

            took = time.strftime('%H:%M:%S', time.gmtime(end - start))

            print(f"TOTAL RUN TIME: {took}")


if __name__ == "__main__":

    export = AutoExport()

    time.sleep(2)

    export.getWatchlist()
