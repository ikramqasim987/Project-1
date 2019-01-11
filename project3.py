#Project 3 by Ikram Qasim

import sqlite3
import csv
conn=sqlite3.connect('Towed_Vehicles.db')
c=conn.cursor()
air = ' CREATE TABLE towed_vehicles (Tow_Date, Make, Style, Color, State)'
try:
    c.execute(air)
except:
    pass

#Importing the proper elements needed to help create the table


#f=open('Towed_Vehicles.csv', 'r')
#f.readline()
#for line in f:
 #   line=line.strip().split(',')
    #values=(Tow_Date, Make, Style, Color, State)
  #  c.execute("INSERT INTO towed_vehicles VALUES(?, ?, ?, ?,?)",line)
#f.close()
#conn.commit()

#conn.close()



sql='SELECT COUNT (DISTINCT State) FROM towed_vehicles'
c.execute(sql).fetchall()
print(c.execute(sql).fetchall())

#Writing the SQL Command


#1. The database is #179kb
#2.There are 75 different car makes
#3. There are 40 cars from out of the state
#4. 9/09/2017 cars were towed the most









     
