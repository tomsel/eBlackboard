import ftplib 
session = ftplib.FTP('localhost','simon','linser') 
file = open('imgsrc/hello.png','rb') # file to send 
session.storbinary('STOR eBlackboardDev/imgdest/hello.png', file) # send the file 
file.close() # close file and FTP 
session.quit()
