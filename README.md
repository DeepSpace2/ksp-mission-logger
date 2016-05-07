#ksp-mission-logger

A basic (for now :) ) mission logger for Kerbal Space Program written in Django.

### Setting up

Since this project is still in it's early days, you will need to set up some things manually.

1. Make sure you have Python 3 installed.

2. Make sure you have Django installed (1.9 or later).
   If you don't, simply run `pip install django` in your favorite command line interface.

3. Under the project's root directory, open `/ksp_mission_logger/settings.py` with any text editor, and insert your KSP root directory in line 16.
   It should resemble the following:
   `ROOT_KSP_PATH = r'/some/path/to/KSP'`.
   Please make sure you have the `r` in the beginning and you don't have a trailing slash.

   This is needed so the list of vessels in the logger will be populated with all the ships names in KSP.
   Note that if the root you provided is wrong, you will still be able to use the logger but you will have to input your vessels manually,
   
### Running

1. Dir into the project's root directory with any command line interface, and run `python manage.py runserver`. 
   Launch your favorite browser and go to http://127.0.0.1:8000 and you should be greeted with the logger's homepage.
   
   ![missionlogger index](index.jpg?raw=true)
   
### Usage

When viewing the main page (the /missions page) it is possible to filter by clicking on a vessel name or on a mission status.

This will show only the respective missions.

In order to view all the missions again, click on `All Missions` in the top left.