#!/usr/bin/env python


from BME280_APIfromAdafruit import * # import sensor API
import MySQLdb # import database API
import time # import time API





# connect to database
db = MySQLdb.connect("localhost", "meteo", "Mybite", "meteo")
curs=db.cursor()
 
# connect to sensor
sensor = BME280(mode=BME280_OSAMPLE_8)


# incert data into database

while(1):
    try:
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()

        
        # print 'Temp      = {0:0.3f} deg C'.format(degrees)
        # print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
        # print 'Humidity  = {0:0.2f} %'.format(humidity)
        
        myQuerry = "INSERT INTO sensordat values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), " + str(degrees) +", "+ str(humidity)+ ", "+ str(hectopascals)  +")"
            
        curs.execute (myQuerry)
     
         
        db.commit()
        print "Data committed"

    except:
        print "Error: the database is being rolled back"
        db.rollback()
    time.sleep(300)



 



