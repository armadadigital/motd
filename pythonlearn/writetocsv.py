# Write to CSV files
import csv

messagesLog = open('/var/log/speedtest.log')
csvFile = open('/home/azmimn/dummy/pythonlearn/speedtest.csv', 'w')

for line in messagesLog:
        readLine = line.split()
        writer=csv.writer(csvFile)
        writer.writerow(readLine)
