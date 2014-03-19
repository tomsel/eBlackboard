import ftplib 
def upload(path,directory,filename):
	session = ftplib.FTP('195.74.38.22','193040_master','eblackboard') 
	file = open(filename,'rb') # file to send
	
	#create directory if it does not exist
	session.cwd(path)
	dirlist=session.nlst()
	count=0
	for entry in dirlist:
		if str(entry) == directory:
			break
		else:
			count+=1
			continue
	if count==len(dirlist):
		session.mkd(directory)
	
	#save the file	
	session.storbinary('STOR '+directory+'/'+filename, file)	

	file.close() # close file 
	session.quit #close FTP
