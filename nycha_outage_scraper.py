
# =======================
# Import libraries
# =======================
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from pytz import timezone
import csv
from pathlib import Path
import pandas as pd


# Fetch the html file
url = 'https://my.nycha.info/Outages/Outages.aspx'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


# =======================
# Create folder with date/time of scrape
# =======================

# datetime object containing current date and time, modifying with NYC timezone(pytz)
now = datetime.now(pytz.timezone('US/Eastern'))

# Format of dd-mm-YY H:M:S
dt_string = now.strftime("%m-%d-%Y %H:%M:%S")
timeofscrape = dt_string
print("date/time of scrape is ", timeofscrape)

# Create a folder named date/time of current scrape
currentfolder = Path("outage-scrape-csvs/" + timeofscrape).mkdir(parents=True, exist_ok=True)


# =======================
# HEAT/HOT WATER/WATER DICTIONARIES
# =======================
CurrentHeatHotWaterWater = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/heathotwatercurrentoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_grvOutagesOpen',
  'IfOutageMessage': 'There are current heat/hot water/water outages.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_panNoOpenOutages'
}

RestoredHeatHotWaterWater = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/heathotwaterrestoredoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_grvOutagesClosedIn24Hours',
  'IfOutageMessage': 'There were heat & hot water outages restored within last 24hrs.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_panNoOutagesClosedIn24Hours'
}

PlannedHeatHotWaterWater = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/heathotwaterplannedoutages.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_grvOutagesPlanned',
  'IfOutageMessage': 'There are heat & hot water outages planned.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_panNoOutagesPlanned'
}

# =======================
# ELEVATOR DICTIONARIES
# =======================
CurrentElevator = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/elevatorcurrentoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_elevatorOutagesList_grvOutagesOpen',
  'IfOutageMessage': 'There are current elevator outages.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_elevatorOutagesListpanNoOutagesOpen'
}

RestoredElevator = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/elevatorrestoredoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_elevatorOutagesList_grvOutagesClosedIn24Hours',
  'IfOutageMessage': 'There were elevator outages restored within last 24hrs.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_elevatorOutagesList_panNoPlannedOutages'
}

PlannedElevator = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/elevatorplannedoutages.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_elevatorOutagesList_grvOutagesPlanned',
  'IfOutageMessage': 'There are elevator outages planned.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_elevatorOutagesList_panNoOutagesPlanned'
}

# =======================
# ELECTRIC DICTIONARIES
# =======================
CurrentElectric = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/electriccurrentoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_electricOutagesList_grvOutagesOpen',
  'IfOutageMessage': 'There are current electric outages.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_electricOutagesListpanNoOutagesOpen'
}

RestoredElectric = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/electricrestoredoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_electricOutagesList_grvOutagesClosedIn24Hours',
  'IfOutageMessage': 'There were electric outages restored within last 24hrs.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_electricOutagesList_panNoPlannedOutages'
}

PlannedElectric = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/electricplannedoutages.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_electricOutagesList_grvOutagesPlanned',
  'IfOutageMessage': 'There are electric outages planned.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_electricOutagesList_panNoOutagesPlanned'
}

# =======================
# GAS DICTIONARY
# =======================
GasOutage = {
  'CsvPath': 'outage-scrape-csvs/' + timeofscrape + '/gasoutage.csv',
  'HtmlId': 'ctl00_ContentPlaceHolder1_gasOutagesList_grvOutages',
  'IfOutageMessage': 'There are gas outages.',
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_gasOutagesList_panNoOutages'
}

# outages = [CurrentHeatHotWaterWater, RestoredHeatHotWaterWater, PlannedHeatHotWaterWater, CurrentElevator, RestoredElevator, PlannedElevator, CurrentElectric, RestoredElectric, PlannedElectric, GasOutage]
outages = [CurrentHeatHotWaterWater, RestoredHeatHotWaterWater, PlannedHeatHotWaterWater]



# =======================
# Iteraring over the outages list of dictionaries
# =======================
for everyoutage in outages:
    if (soup.find("table", {"id": everyoutage['HtmlId']})):
      # Print to terminal for QA purposes
      print( everyoutage['IfOutageMessage'] )
      # Create dataframe(df) of the HTML table in question, using pandas
      df = pd.read_html(url, header=0, attrs = {'id': everyoutage['HtmlId']})[0]
      # printing dataframe for QA purposes
      print(df)
      # create a csv and insert the dataframe(df)
      df.to_csv( everyoutage['CsvPath'] )
    else:
      noOutageMessage = soup.find("div", {"id": everyoutage['IfNoOutageId']}).find("div").text
      # Print to terminal for QA purposes
      print(noOutageMessage)
      # Create the csv
      csv = csv.writer(open(everyoutage['CsvPath'], 'w', newline=''))
      # Write the message to the csv
      csv.writerow([noOutageMessage])







    # Before creating the dataframe, we must sort out the issue of the nested impact table
    impactTable = soup.find("table", {"id": everyoutage['HtmlId']}).find("table", {"class": "nested"})
    # print("impactTable", impactTable)
    impactTableHeaders = impactTable.find_all("th")

    for impactTableHeader in impactTableHeaders:
      impactTableHeader = str(impactTableHeader.text) + '/'
      print("impactTableHeader", impactTableHeader)


    impactTableData = impactTable.find_all("td")
    print("impactTableData", impactTableData)

    for impactTableDatum in impactTableData:
      impactTableDatum = str(impactTableDatum.text) + '/'
      print("impactTableData", impactTableDatum)







