import MySQLdb as mdb
import sys
from contextlib import closing
#Bara en grund
def insertdata(PATH, DATE, COURSECODE, COURSENAME):
	try:
		con = mdb.connect('127.0.0.1', '193040_vn74392', 'u55MZngO4Z', '193040-eblackboard');
		with con:
			with closing( con.cursor() ) as cur:
				cur.execute("INSERT INTO Images VALUES (NULL, '"+PATH+"', '"+DATE+"', '"+COURSECODE+"', DEFAULT)")
				cur.execute("SELECT EXISTS(SELECT 1 FROM Courses WHERE CODE='"+COURSECODE+"')")
				if cur.fetchone()[0]==0:
					cur.execute("INSERT INTO Courses VALUES (NULL,'"+COURSECODE+"','"+COURSENAME+"')")
		
	except mdb.Error:
		try:
			con.close()
		except:
			raise
	raise
