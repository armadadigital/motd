# Splitting log programme

messagesLog = open('/var/log/speedtest.log')

for line in messagesLog:
	readLine = line.split()
	print(readLine)
