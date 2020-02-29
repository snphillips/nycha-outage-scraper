# NYCHA Outages Scaper

The New York City Housing Authority (NYCHA) maintains a page on their site that lists services outages in thier developments for heat, hot water, water, elevators, electricity & gas. The outage site is updated regularly, however there is no easy way for stakeholders to download the data. This scraper extracts the data from the NYCHA website and saves the results in csv tables, within a folder named with the date and time of the scrape.

NYCHA Service Outages Page: https://my.nycha.info/Outages/Outages.aspx

## How to Use
1) Navigate to the project folder and use the following command to build the virtual environment:

`python3 -m venv nycha-outages-scraper2`

2) To activate the virtual environment, input the following command in the terminal:

`source nycha-outages-scraper2/bin/activate`

3) Run code by inputting the following command in the terminal:

`python3 nycha_outage_scraper.py`


## Built With
- python
- beautiful soup
- pandas
