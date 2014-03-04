import MySQLdb as mdb
import sys
#Bara en grund
try:
	con = mdb.connect('127.0.0.1', 'tomas', 'abc', 'eblackboard');

	cur = con.cursor()
	cur.execute("SELECT * FROM LectureNotes")

	ver = cur.fetchone()

	print "Database version : %s " % ver
    
except mdb.Error, e:

	print "Error %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)

finally:
	print "end"
