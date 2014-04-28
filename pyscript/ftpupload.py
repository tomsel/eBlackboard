#import ftplib 
import paramiko
import traceback
import os
import sys
	
def upload(path,directory,filename):
	try:
		ssh_host    = "ssh.binero.se"
		ssh_port    = 22

		user     = "193040_raspuser"
		password = "3'kj}/rT[HM[XEp"

		transport = paramiko.Transport((ssh_host, ssh_port))

		transport.connect(hostkey  = None,
				          username = user,
				          password = password,
				          pkey     = None)
		
		sftp = paramiko.SFTPClient.from_transport(transport)
		
		#create directory if it does not exist
		sftp.chdir(path=path)
		dirlist=sftp.listdir('.')
		count=0
		for entry in dirlist:
			if str(entry)==directory:
				break
			else:
				count+=1
				continue
		if count==len(dirlist):
			sftp.mkdir(directory)
			
		#save the file
		sftp.put(filename, directory+'/test.jpg')
		
		#close the connection
		transport.close()
	
	#handle any exception	
	except Exception as e:
		print('*** Caught exception: %s: %s' % (e.__class__, e))
		traceback.print_exc()
		try:
		    transport.close()
		except:
		    pass
		sys.exit(1)

"""
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
"""
