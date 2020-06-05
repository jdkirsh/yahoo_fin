'''
* test using AAPL
* get options axpiration dates
* get put and calls for one expiration date into DataFrame
* design Sqlite DB
* create functions to retrive info
'''

from yahoo_fin.options import *
import pandas as pd
import sqlite3

con = sqlite3.connect(r'C:\FINANCE\Python\pyCharm\Projects\yahoo_fin\yahooFin.db')

ASSET ='AAPL'
NUM_OF_EXPIRATIONS = 5

try:
    from requests_html import HTMLSession
except Exception:
    pass



def main():
    print ("pause")
    expDatesSim = ['May 29, 2020', 'June 5, 2020', 'June 12, 2020', 'June 19, 2020', 'June 26, 2020', 'July 2, 2020', 'July 17, 2020',
     'September 18, 2020', 'October 16, 2020', 'November 20, 2020', 'December 18, 2020', 'January 15, 2021',
     'June 18, 2021', 'September 17, 2021', 'January 21, 2022', 'June 17, 2022', 'September 16, 2022']
    # expDates = expDatesSim

    full_expDates = get_expiration_dates(ASSET) # get list of expiration dates
    expDatesList=full_expDates[:NUM_OF_EXPIRATIONS]
    print ("expDatesList=", expDatesList)

    appended_data  = []
    for expDate in expDatesList:
        print ("get_options_chain:"," ASSET=", ASSET," expDate=",expDate)
        expDF = get_options_chain(ASSET, str(expDate) ) # DF of Call and Puts for expiration date
        assetCalls = expDF['calls']                 # DF of calls
        assetPuts = expDF['puts']                   # DF of puts
        assetCalls['Symbol'] = ASSET                # append Symbol to Calls DF
        assetPuts['Symbol'] = ASSET                 # append Symbol to Puts DF
        assetCalls['Expiration'] = expDate          # append Expiration to Calls DF
        assetPuts['Expiration'] = expDate           # append Expiration to Puts DF
        assetCalls['Type'] = 'Calls'                # append Type to Calls DF
        assetPuts['Type'] = 'Puts'                  # append Type to Puts DF
        # assetDF = assetDF.concat([assetCalls, assetPuts])
        # assetDF.concat([assetCalls, assetPuts])   # concat Puts and Calls together
        appended_data.append(assetCalls)
        appended_data.append(assetPuts)
    appended_data = pd.concat(appended_data)
    appended_data.to_sql('assetTable', con, if_exists="replace")


            # appended_data = []
            # for infile in glob.glob("*.xlsx"):
            #     data = pandas.read_excel(infile)
            #     # store DataFrame in list
            #     appended_data.append(data)
            # # see pd.concat documentation for more info
            # appended_data = pd.concat(appended_data)
            # # write DataFrame to an excel sheet
            # appended_data.to_excel('appended.xlsx')


    # print ("expDates=", expDates)
    # l = [i.strip('[]') for i in l]
    # expNames = [expDate.replace(' ','').replace(',','') for expDate in expDates]
    # for expDate in expDates:
    # May292020 = get_options_chain(ASSET, 'May 29, 2020')
    # print ("May292020=",May292020)
        # specify an expiration date
    # get_options_chain('amzn', '03/15/2019')

    # for expName, expDate in zip(expNames, expDates):
    #     # print("expName=",expName, " expDate=",expDate)
    #     # expNameCalls = expName+'Calls'
    #     # expNamePuts = expName+'Puts'
    #     # print ("expNameCalls=",expNameCalls," expNamePuts=",expNamePuts)
    #     expName = get_options_chain((ASSET, expDate))
    # print("pause")


if __name__ == '__main__':

    print("pause")
    main()

