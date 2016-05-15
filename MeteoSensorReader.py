#!/usr/bin/env python


import MySQLdb # import database API
import time # import time API





# connect to database
db = MySQLdb.connect("localhost", "meteo", "Mybite", "meteo")
curs=db.cursor()
 


# querry data from database
curs.execute ("SELECT * FROM sensordat")

print "\nDate     	Time		Temperature(deg C)	Humidity (%)	Pressure (hPa)"
print "======================================================================================"

for reading in curs.fetchall():
    print str(reading[0])+"	"+str(reading[1])+" 	"+\
                str(reading[2])+"        	        "+str(reading[3])+"  	"+str(reading[4])










