######CLIENT_CODE###########
import socket
import os
import datetime
HOST = 'localhost'
PORT = 3500
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

#########to find file size###################
def filesize(fileobj):
	fileobj.seek(0,2)
	filsize=fileobj.tell()
	return filsize
##########Reading File #######################
print 'enter the path of the file to txd'  
path=raw_input('path: ') 
fo=open(path,'rb',50000000)
size=filesize(fo)
size=str(size)
print 'file size:',size
s.sendall(size)

dat=s.recv(1024)
print dat
if dat!='invalid client':
	
####sending file##########	
	print 'enter y if you wish to send'
	enter=raw_input('->')
	if enter=='y':
		start =datetime.datetime.now()
		op= open(path).read()
		s.sendall(op)
		#print (data)
		end=datetime.datetime.now()
		print 'sending file',repr(op)
		transmission_time=float((end-start).microseconds)
		print transmission_time

					
	else: 
		print('connection closed')

s.close()
#end=datetime.datetime.now()













