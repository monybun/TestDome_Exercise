#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An application that you are implementing requires multiple date formats to be transformed into one common date format.

Implement the function change_date_format which accepts a list of strings, representing dates, 
and returns a new list with each date in the format YYYYMMDD. 
All incoming dates will be valid dates, but only those in one of the following formats: 
    YYYY/MM/DD, DD/MM/YYYY, and MM-DD-YYYY should be included in the returned list, 
    where YYYY, MM, and DD are numbers representing year, month, and day.

For example, change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"]) 
should return the list ["20100330", "20161215", "20121115"].

"""

import datetime as dt
def change_date_format(dates):
    datelist = []
    fmts = ("%Y/%m/%d","%d/%m/%Y","%m-%d-%Y")
    for i in dates:
        for f in fmts:
            try:
                check = dt.datetime.strptime(i, f)
                if check:
                    converted_date = dt.datetime.strptime(i, f).strftime('%Y%m%d')
                    #print(converted_date)
                else:
                    pass
                datelist.append(converted_date)
                break
            except ValueError:
                pass
    
    return datelist
                

if __name__ == "__main__":
    dates = change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"])
    print(*dates, sep='\n')