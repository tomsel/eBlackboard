import MySQLdb as mdb
import sys
from contextlib import closing
#Bara en grund
def insertdata(PATH, DATE, COURSECODE, COURSENAME):
	try:
		con = mdb.connect('127.0.0.1', '193040_vn74392', 'u55MZngO4Z', '193040-eblackboard');
		print 'connected to mysql database'
		with con:
			with closing( con.cursor() ) as cur:
				cur.execute("INSERT INTO Images VALUES (NULL, '"+PATH+"', '"+DATE+"', '"+COURSECODE+"', DEFAULT)")
				cur.execute("SELECT EXISTS(SELECT 1 FROM Courses WHERE CODE='"+COURSECODE+"')")
				if cur.fetchone()[0]==0:
					cur.execute("INSERT INTO Courses VALUES (NULL,'"+COURSECODE+"','"+COURSENAME+"')")
		print 'completed insertion of data'
	except mdb.Error as e:
		try:
			con.close()
		except:
			raise Exception
		raise Exception
