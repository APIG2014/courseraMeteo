#!/usr/bin/env python

import MySQLdb

# connect to database
db = MySQLdb.connect("localhost", "meteo", "Mybite", "meteo")
curs=db.cursor()

# incert data into database
try:
    curs.execute ("""INSERT INTO sensordat 
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 23, 234, 21)""")
     
    db.commit()
    print "Data committed"

except:
    print "Error: the database is being rolled back"
    db.rollback()




# querry data from database
curs.execute ("SELECT * FROM sensordat")

print "\nDate     	Time		Temperature	Humidity	Pressure"
print "==========================================================="

for reading in curs.fetchall():
    print str(reading[0])+"	"+str(reading[1])+" 	"+\
                str(reading[2])+"  	"+str(reading[3])+"  	"+str(reading[4])
