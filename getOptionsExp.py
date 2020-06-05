from yahoo_fin.options import *

# expDates = get_expiration_dates('ABT')
exp = get_expiration_dates('nflx')
print ("exp=", exp)

# myCalls = get_calls('nflx')

# print (myCalls)

# get data on the earliest upcoming expiration date
get_options_chain('nflx')

# specify an expiration date
get_options_chain('amzn', '03/15/2019')