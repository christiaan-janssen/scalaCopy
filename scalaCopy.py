#################################################################################################
#																								#
#	Filename: 	scalaCopy.py 																	#
#	Author: 	Christiaan Janssen																#
#	version:	1.0				 																#
#																								#
#	Usage:		I run this script from the windows task scheduler. It is importand to note 		#
#				that you need to change the paths and create the folders. If the Scripts		#
#				can't find the folders it will log the error but it shuld just finish 			#
#				without errors. 																#
#																								#
#################################################################################################				

from shutil import *
import os.path as path
import logging
import datetime

# Create a timestamp:
now = datetime.datetime.now()
datetime.time(now.hour, now.minute, now.second)
theTime = str(datetime.time(now.hour, now.minute, now.second))

# Setup a log file:
logging.basicConfig(filename='scalaCopy.log',level=logging.DEBUG)

# Array with erver names:
players = ['PL-W7P-SG01', 'PL-W7P-SG08', 'PL-W7P-SG09', 'PL-W7P-SG10', 'PL-W7P-SG11']

# Start of the main script
for player in players:
	try: # Try to compair the 2 files. This is in a try/catch because if the file doesnt exsists it will crash
		if (path.getmtime('//srv-wxp-ifc/Scala Runned/Daily Events Runned.csv') > path.getmtime('//' + player + '/c$/Scala Daily Events/Daily Events Runned.csv')):
			logging.info(theTime + ': Copying files to the players')
			# if the server copie is newer, copy it to the player
			try:
				copyfile('//srv-wxp-ifc/Scala Runned/Daily Events Runned.csv', '//' + player + '/c$/Scala Scripts/Daily Events Runned.csv')
				logging.info(theTime + ': copy to ' + player + ' success')
			except WindowsError, e:
				logging.warning(theTime + ': ' + str(e))
		else:
		 	logging.info(theTime + ': Nothing to do for ' + player + ', going to sleep.')
	
	# If the file isnt on the Player catch the error and copy the file.
	except WindowsError, e:
		logging.warning(theTime + ': ' + str(e))
		try:
			copyfile('//srv-wxp-ifc/Scala Runned/Daily Events Runned.csv', '//' + player + '/c$/Scala Daily Events/Daily Events Runned.csv')
			logging.info(theTime + ': copy ' + player + ' success')
		except WindowsError, e:
			logging.warning(theTime + ': WindowsError: ' + str(e))

		except IOError, e:
			logging.warning(theTime + ': IOError: ' + str(e))