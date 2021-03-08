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

![Alt text](/img/thinkscript_editor_add_sma.png)

3. Once back at the main screen, go to your chart where you are displaying the strategy that you just added the SMA line to. Notice how high it is above the actual candles. Thats what we want. (See image below)

![Alt text](/img/sma_line.png)

4. Next, double click on the SMA line, and a customizing popup will display. Click on the plots dropdown, then click on the SMA tab. The image below is what should be displayed.

![Alt text](/img/customize_sma_line.png)

5. Next, we need to change the draw as display, which changes how the plot is shown on the chart.
6. We need to change this to a bar graph that covers the entire chart. (See image below)

![Alt text](/img/customize_sma_line_to_cover.png)

7. Click apply, and save.
8. You should now have something like the image below.

![Alt text](/img/basic_chart_cover.png)

### Getting coordinates for key locations based on your screen size

- There are key locations that you must obtain so the program knows where to send the cursor.
- The images below will show the the locations.
- There are two types of coordinates you will need. Relative and Absolute.

  1. Relative - x, y coordinates are relative to where your mouse cursor currently is located.
  2. Absolute - x, y coordinates are not relative to your mouse cursor and will go to the precise screen location specified.

- All of these coordinates will need to be set in accordance to where they are needed in the program. The program has comments throughout to help you locate theses areas.

1. First, you will need the absolute coordinates for the watchlist dropdown hamburger icon and relative coordinates for the Export to file... [Hamburger icon > Export to file... tab]

![Alt text](/img/sidebar_export_watchlist.png)

2. In the file explorer that pops up after you click the Export to file..., get the relative coordinates for the save button. Make sure you change the directory to your working directory before saving. This will set the working directory as the default so you don't have to change it everytime.

![Alt text](/img/export_watchlist_to_local.PNG)

3. After that, you need the the absolute coordinates for the top most symbol in your watchlist. Always make sure that your watchlist is scrolled all the way to the top before you run the program, or you won't export all the files in the watchlist.

![Alt text](/img/watchlist_first_row_click.png)

4. Next, you will need absolute coordinates to any location within the red box below.

![Alt text](/img/chart_covered.png)

5. This dropdown propegates when you right click on the chart only where the SMA graph is covering the chart. You will need the relative coordinates for the Show report tab.

![Alt text](/img/show_report_dropdown.png)

6. You will need the relative coordinates for the Export File button. [Show report tab > Export File button]

![Alt text](/img/export_strategy_report_button.png)

7. You will need the relative coordinates for the Save button. All files will be downloaded to your documents folder by default. The program will automatically move each file from there to your csv_files directory in your working folder. [Export File button > Save button]

![Alt text](/img/save_export_to_local.png)

8. Next, we need the relative coordinates for the Close button. [Save button > Close Button]

![Alt text](/img/close_export_strategy.png)

9. Once closed, the program will automatically arrow down to the next symbol in the watchlist.

![Alt text](/img/watchlist_arrow_down_to_next_row.png)

10. This process will continue until it reaches the final symbol in the watchlist.

11. Upon completion, an alert will sound letting you know that the program has finished. That way you can be away from your computer and you will hear when it's complete.

### What if theres an error?

- Well, the program can handle that. Just restart the program, and make sure that the watchlist is all the way to the top, and the program will automatically scroll down to where the program left off.

- If there is an error, an alert sound will trigger, all remaining strategy reports located in the users documents folder will be deleted, and the error message will display in your terminal.

- Most common error is when there is a missed export, due to either the user moving the mouse or Thinkorswim not loading charts fast enough, or not at all.

### Video below shows the program in action.

[![TOS Auto Export Demo](https://yt-embed.herokuapp.com/embed?v=_nUJVA0clU0)](https://www.youtube.com/watch?v=_nUJVA0clU0 "TOS Auto Export Demo")
