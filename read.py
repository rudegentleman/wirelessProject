#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 00:39:52 2018

@author: rudegentleman
Last Edit: March 22, 2018 16:29:30
"""
import serial
import MySQLdb
# Initializing open communication port and baud or datarate
# The serial port might change, so make sure you check which port you're 
# connecting to. Also check to ensure you've priviledges to access it
# The format for the ports is usually /dev/ttyUSB* or /dev/ttyACM*
serialPort = 'Specify Serial Port'
dataRate = 9600
ser = serial.Serial(serialPort, dataRate)
# Initialize variables to be used to connect to your database
hostname = 'location of database (localhost or IP address)' # Location of the database
username = 'Username' # Username to connect to database
password = 'Password' # Password of username
database = 'Database name' # Database to connect to
# Establish database connection to begin data collection
myConnection = MySQLdb.connect(host=hostname,
                     user=username,
                     passwd=password,
                     db=database)
cur = myConnection.cursor() # Function that helps you execute all mysql commands
while True: # This checks if the serial port is available and has data
    try:
        value = ser.readline() # Read serial port and assign it's contents to value
        print (value) # This is just for visualizing the data read from your serial port
	# This is the part where you insert values to your database
    except KeyboardInterrupt:
        break
myConnection.close() # Close the connection when done
ser.close()    # Close the serial connection when done
