import MySQLdb as mdb
import sys
from contextlib import closing
#Bara en grund
def insertdata(PATH, DATE, COURSE):
	try:
		con = mdb.connect('127.0.0.1', '193040_vn74392', 'u55MZngO4Z', '193040-eblackboard');
		with con:
			with closing( con.cursor() ) as cur:
				cur.execute("INSERT INTO LectureNotes VALUES (NULL, '"+PATH+"', '"+DATE+"', '"+COURSE+"')") 
		
	except mdb.Error, e:

		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)

	if con:
		con.close()
		print ('connection closed')

		
insertdata('/img/2014-03-04.2.png', '2014-03-04', 'TDA515')
