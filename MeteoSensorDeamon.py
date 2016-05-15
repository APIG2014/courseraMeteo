#!/usr/bin/env python


from BME280_APIfromAdafruit import * # import sensor API
import MySQLdb # import database API





# connect to database
db = MySQLdb.connect("localhost", "meteo", "Mybite", "meteo")
curs=db.cursor()
 
# connect to sensor
sensor = BME280(mode=BME280_OSAMPLE_8)


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









degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
print 'Temp      = {0:0.3f} deg C'.format(degrees)
print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
print 'Humidity  = {0:0.2f} %'.format(humidity)
