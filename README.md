# NYCHA Outages Scaper

The New York City Housing Authority (NYCHA) maintains a page on their site that lists services outages in thier developments for heat, hot water, water, elevators, electricity & gas. The outage site is updated regularly, however there is no easy way for stakeholders to download the data. This scraper extracts the data from the NYCHA website and saves the results in csv tables, within a folder named with the date and time of the scrape.

NYCHA Service Outages Page: https://my.nycha.info/Outages/Outages.aspx

## How to Use

Note: you'll need python installed on your computer. *Learn more here: https://www.python.org/about/gettingstarted/*

- Clone this repo then navigate into the project folder

`cd nycha-outages-scraper2`

- To build the virtual environment, in your terminal run:

`python3 -m venv nycha-outages-scraper2`

- To activate the virtual environment, in your terminal run:

`source nycha-outages-scraper2/bin/activate`

- You will need the following python packages installed: requests, bs4, datetime, pytz, csv, pathlib & pandas.  These are all listed in requirements.txt.  To install those packages automatically, in your terminal run:

`pip install -r requirements.txt`

- To run the scraper, in your terminal run:

`python3 nycha_outage_scraper.py`

The scraping isn't instant. On my system it takes 20 seconds. You can view the progress in your terminal.

You'll know the scrape is successful if you see a csv file with the timestamp of the scrape as the folder name, within a folder called outage-scrape-csvs within the project folder. Within the timestamped folder, there should be 10 csvs. Each csv represents a type of outage.


## Built With
- python
- beautiful soup
- pandas
