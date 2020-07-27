# Bronchus
COVID Analysis and Data Parsing

This project uses the https://api.covid19india.org/ API to fetch COVID Data for India
and do analysis. 
The API endpoint currently being used is https://api.covid19india.org/v4/data.json

The provided data contains delta which is the information for the latest day. 
It includes deceased, confirmed and recovered. It is important to take a note of 
the last_updated from the meta portion since the information is extracted 
from state bulletins. Updation of information from these bulletins is not regular. 
Hence, use the last_updated to check when the information was last provided as you 
might get some days with no updates at all. 

[Taskernet Link](https://taskernet.com/shares/?user=AS35m8lpIQwnXCcmhtRaGG8JV4%2BF95VX8yA1A8bpO%2BlsM4c5ZS8%2BdPHxI%2Fffp5slPxIzIyFg5A%3D%3D&id=Task%3AGet+Covid+Data)

## What does the above link do? 
This project was essentially developed as a small script to extract COVID data for my
city and put as a widget on my phone. There are multiple ways to do this - 
1. The most straightforward and non-app dependent way is to run a python script and 
use the android toast method via ADB to display the task. You would need something 
like termux to run the script and hence, it is not completely App Dependent. 
2. My setup involves Tasker and KWGT. Tasker is many things but for this task, it 
essentially runs the equivalent of fetch.py by accessing the API. If you have tasker,
you can directly click on the taskernet link to import the required task. 
The actual widget display is done via KWGT. Again, KWGT is extremely powerful but for
 this the sake of this project, we simply pass the variables from tasker to KWGT using
 a broadcast method. If you would like me to share the KWGT widget file or need any 
 other resource, please raise an issue. 
 
![Widget Screenshot](https://i.imgur.com/6Ztwi84.png)

## Future Tasks

As of now, the main aim of the project is complete. For the future, there could be 
analysis of covid data and a predictive model (Even though this is aa quite overdone 
trope)