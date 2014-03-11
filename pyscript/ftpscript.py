import ftplib 
def upload(filename,course):
	session = ftplib.FTP('195.74.38.22/','193040_master','eblackboard') 
	file = open(filename,'rb') # file to send
	#att implementera: skapa mapp om den inte finns 
	session.storbinary('STOR /eblackboard.se/public_html/img/'+course+'/'+filename, file) # send the file 
	file.close() # close file 
	session.quit #close FTP

