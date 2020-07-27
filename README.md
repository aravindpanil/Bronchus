# Bronchus
COVID Analysis and Data Parsing

This project uses the https://api.covid19india.org/ API to fetch COVID Data for India and do analysis. 
The API endpoint currently being used is https://api.covid19india.org/v4/data.json

The provided data contains delta which is the information for the latest day. It includes deceased, confirmed and recovered. It is important to take a note of the last_updated from the meta portion since the information is extracted from state bulletins. Updation of information from these bulletins is not regular. Hence, use the last_updated to check when the information was last provided as you might get some days with no updates at all. 
