# TOS Auto Export
This program allows you to auto export strategy reports from the TDAmeritrades Thinkorswim desktop platform.

## Getting Started
This program has only been tested on Windows OS.

You will need the Thinkorswim desktop application, for the program is created for this application specifically.
The program uses pyautogui to automate native keyboard and mouse functionalities.

### Prerequisites
Virtual Env: Pipenv [OPTIONAL]

Dependencies: pyautogui, playsound, keyboard

Desktop App: TDAmeritrades Thinkorswim

Language: Python 3.8+

### First thing we need to do is setup the Thinkorswim app.

1. Go into your thinkscript editor for the strategy of your choice and plot a SMA or anything that will plot a line, and multiply it by 2 or more. (See image below)
2. Once entered, apply and save.

![alt text](https://github.com/TreyThomas93/TOS-Auto-Export/tree/master/img/thinkscript_editor_add_sma.png "")

3. Once back at the main screen, go to your chart where you are displaying the strategy that you just added the SMA line to. Notice how high it is above the actual candles. Thats what we want.
4. Next, double click on the SMA line, and a customizing popup will display. Click on the plots dropdown, then click on the SMA tab. The image below is what should be displayed.

![alt text](https://github.com/TreyThomas93/TOS-Auto-Export/tree/master/img/customize_sma_line.png "")

5. Next, we need to change the draw as display, which changes how the plot is shown on the chart.
6. We need to change this to a bar/histogram that covers the entire chart. (See image below)

