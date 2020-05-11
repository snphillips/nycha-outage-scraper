# NYCHA Outages Scraper

The New York City Housing Authority (NYCHA) maintains a page on their site that lists services outages in thier developments for heat, hot water, water, elevators, electricity & gas. The outage site is updated regularly, however there is no easy way for stakeholders to download the data. 

This python scraper extracts the data from the NYCHA website and saves the results in csv tables, within a folder named with the date and time of the scrape.

NYCHA Service Outages Page: https://my.nycha.info/Outages/Outages.aspx

## How to Use

Note: you'll need python installed on your computer. *Learn more here: https://www.python.org/about/gettingstarted/*

- Clone this repo 

`git clone https://github.com/snphillips/nycha-outage-scraper.git`

- Navigate into the project folder

`cd nycha-outages-scraper`

- To build the virtual environment, in your terminal run:

`python3 -m venv nycha-outage-scraper`

(FYI, now you will see an other directory within the parent directory also with the name nycha-outage-scraper.)

- To activate the virtual environment, in your terminal run:

`source nycha-outage-scraper/bin/activate`

- You will need the following python packages installed: *requests, bs4, datetime, pytz, csv, pathlib & pandas.*  These are all listed in requirements.txt.  To install those packages, in your terminal run:

`pip install -r requirements.txt`

Install lxml too

`pip3 install lxml`

If you've made it this far, you've completed set-up. Now you are ready to scrape data!

- To run the scraper, in your terminal run:

`python3 nycha_outage_scraper.py`

The scraping isn't instant. On my system it takes 20 seconds. You can view the progress in your terminal.

To check if the scrape is successful, open the directory called *outage-scrape-csvs*.  In there you see an other directory named with the timestamp of the scrape. Within the timestamped folder, there should be 10 csvs. Each csv represents a type of outage.

Here's what a csv *with outages* looks like:

<img src="https://i.imgur.com/3CmQKwE.png" width="800" alt="screengrab of csv with outage data">

You can open the csv with your favorite csv-editing program:

<img src="https://i.imgur.com/W97xMDy.png" width="800" alt="screengrab of csv with outage data">

Here's what a csv *without outages* looks like:

<img src="https://i.imgur.com/1y4g93S.png" width="800" alt="screengrab of csv if no outage data">


## Built With
- python
- beautiful soup
- pandas

## TODO
The "Impact" column has nested tables that need to be unpacked. Currently, all the impact data is squished together, rendering it useless.
