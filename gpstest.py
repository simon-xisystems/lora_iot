
import serial
import csv
import time

port = "/dev/ttyS0"
utc_time =' ' 
lat = ' '
dirLat = ' '
lon = ' '
dirLon =  ' '
alt =  ' '
sat =  ' '


def parseGPS(data):
	if data[0:6] =="$GPGGA":
	   s=data.split(",")
	   if s[7] =='0':
		print "no satellite data available"
		return
	   global utc_time
	   global lat
	   global dirLat
	   global lon
	   global dirLon
	   global alt
	   global sat
	   utc_time =s[1][0:2] + ":" + s[1][2:4] + ":" +s[1][4:6]
	   lat=decode(s[2])
	   dirLat =s[3]
	   lon = decode(s[4])
	   dirLon = s[5]
	   alt = s[9] +" m"
	   sat = s[7]
	   #print "Time(UTC): %s-- Latitude: %s(%s)-- Longitude:%s(%s)" %(time, lat, dirLat, lon, dirLon)

def savelog ():

	   logWriter = csv.writer(open('data.csv', 'a'))
	   logWriter.writerow(['UTC:',utc_time,lat,dirLat,lon,dirLon])



def decode(coord):
	v = coord.split(".")
	head = v[0]
	tail = v[1]
	deg = head[0:-2]
	min = head[-2:]
	return deg + "." + min + "." + tail + "." 


ser = serial.Serial(port, baudrate = 9600, timeout = 5)
print "logging"

try:
    while True:
	data = ser.readline()
	parseGPS(data)
	savelog()
except KeyboardInterrupt :
	pass
