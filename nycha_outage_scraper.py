
# =======================
# Import libraries
# =======================
import requests
import csv
from datetime import datetime
import pytz
from pytz import timezone
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path


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
  'IfNoOutageId': 'ctl00_ContentPlaceHolder1_heatHotWaterOutagesList_panNoOutagesOpen'
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


# outages = [CurrentHeatHotWaterWater, RestoredHeatHotWaterWater, PlannedHeatHotWaterWater, CurrentElevator, RestoredElevator, PlannedElevator, CurrentElectric, RestoredElectric, PlannedElectric]
outages = [CurrentElectric, RestoredElectric, PlannedElectric]



#  Iteraring over the outages list of dictionaries
for everyoutage in outages:

	if (soup.find("table", {"id": everyoutage['HtmlId']})):
	  # Print for QA purposes
	  print( everyoutage['IfOutageMessage'] )
	  # Create dataframe(df) of the HTML table in question, using pandas
	  df = pd.read_html(url, header=0, attrs = {'id': everyoutage['HtmlId']})[0]
	  # printing dataframe for QA purposes
	  print(df)
	  # create a csv and insert the dataframe(df)
	  df.to_csv( everyoutage['CsvPath'] )
	else:
	  noOutageMessage = soup.find("div", {"id": everyoutage['IfNoOutageId']}).find("div").find("div").text
	  # Print for QA purposes
	  print(noOutageMessage)
	  # Create the csv
	  csv = csv.writer(open(csvpath, 'w', newline=''))
	  # Write the message to the csv
	  csv.writerow(noOutageMessage)


# # =======================
# # ELECTRIC
# # 1) name the path of the csv  that will be updated
# # 2) use Pandas(pd) library to get the tables from html into dataframe(df)
# # 3) "set" the csv with the dataframe
# # 4) If there's no table present (b/c there's no outage) instead print the "no outage" message
# # =======================




# # html ids of tables we're interested in
# currentID = 'ctl00_ContentPlaceHolder1_electricOutagesList_grvOutagesOpen'
# restoredID = 'ctl00_ContentPlaceHolder1_electricOutagesList_grvOutagesClosedIn24Hours'
# plannedID = 'ctl00_ContentPlaceHolder1_electricOutagesList_grvOutagesPlanned'
# # html ids of divs if no tables are found (b/c there are no reported outages)
# noCurrentID = 'ctl00_ContentPlaceHolder1_electricOutagesListpanNoOutagesOpen'
# noRestoredID = "ctl00_ContentPlaceHolder1_electricOutagesList_panNoOutagesClosedIn24Hours"
# noPlannedID = 'ctl00_ContentPlaceHolder1_electricOutagesList_panNoPlannedOutages'

# #  CURRENT ELECTRIC OUTAGES
# csvpath = 'outage-scrape-csvs/' + timeofscrape + '/electriccurrentoutage.csv'
# if (soup.find("table", {"id": currentID})):
#   print("There are current electric outages.")
#   df = pd.read_html(url, header=0, attrs = {'id': currentID})[0]
#   # printing dataframe for QA purposes
#   print(df)
#   df.to_csv(csvpath)
# else:
#   noOutageMessage = soup.find("div", {"id":nocurrentID}).find("div").find("div").text
#   # Print for QA purposes
#   print(noOutageMessage)
#   # Create the csv
#   csv = csv.writer(open(csvpath, 'w', newline=''))
#   # Write the message to the csv
#   csv.writerow(noOutageMessage)


# #  RECENT ELECTRIC OUTAGES
# csvpath = 'outage-scrape-csvs/' + timeofscrape + '/electricrestoredlast24hrs.csv'
# if (soup.find("table", {"id": restoredID})):
#   print("There were electric outages restored within last 24hrs.")
#   df = pd.read_html(url, header=0, attrs = {'id': restoredID})[0]
#   # printing dataframe for QA purposes
#   print(df)
#   df.to_csv(csvpath)
# else:
#   noOutageMessage = soup.find("div", {"id":noRestoredID}).find("div").text
#   # Print for QA purposes
#   print(noOutageMessage)
#   # Create the csv
#   csv = csv.writer(open(csvpath, 'w', newline=''))
#   # Write the message to the csv
#   csv.writerow([noOutageMessage])



# #  UPCOMING ELECTRIC OUTAGES
# csvpath = 'outage-scrape-csvs/' + timeofscrape + '/electricplannedoutages.csv'
# if (soup.find("table", {"id": plannedID})):
#   print("There are planned electric outages.")
#   df = pd.read_html(url, header=0, attrs = {'id': plannedID})[0]
#   # printing dataframe for QA purposes
#   print(df)
#   df.to_csv(csvpath)
# else:
#   noOutageMessage = soup.find("div", {"id":noPlannedID}).find("div").text
#   # Print for QA purposes
#   print(noOutageMessage)
#   # Create the csv
#   csv = csv.writer(open(csvpath, 'w', newline=''))
#   # Write the message to the csv
#   csv.writerow([noOutageMessage])



# # =======================
# # GAS
# # 1) name the path of the csv that will be created
# # 2) use Pandas(pd) library to get the tables from html into dataframe(df)
# # 3) update the csv with the first dataframe(df[0])
# # 4) If there's no html table present (b/c there's no outage) instead print the "no outage" message
# # =======================

# # html id of the table we're interested in and the id if _no table_ is seen
# gasID = "ctl00_ContentPlaceHolder1_gasOutagesList_grvOutages"
# noGasID = "ctl00_ContentPlaceHolder1_gasOutagesList_panNoOutages"


# #  GAS OUTAGES
# csvpath = 'outage-scrape-csvs/' + timeofscrape + '/gas.csv'
# if (soup.find("table", {"id": currentID})):
#   print("There are gas outages.")
#   df = pd.read_html(url, header=0, attrs = {'id': gasID})[0]
#   # printing dataframe for QA purposes
#   print(df)
#   # adding dataframe to csv
#   df.to_csv(csvpath)
# else:
#   noOutageMessage = soup.find("div", {"id":currentID}).find("div").find("div").text
#   # Print for QA purposes
#   print(noOutageMessage)
#   # Create the csv
#   csv = csv.writer(open(csvpath, 'w', newline=''))
#   # Write the message to the csv
#   csv.writerow([noOutageMessage])

