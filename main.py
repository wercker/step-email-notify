#coding: UTF8
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
import mailer
import sys

if len(sys.argv) < 8 :
  print 'There should be 8 arguments'
  sys.exit(1)

fromaddr = str(sys.argv[1])
toaddrs = str(sys.argv[2])
subject  = str(sys.argv[3])
body  = str(sys.argv[4])
username  = str(sys.argv[5])
password  = str(sys.argv[6])
host  = str(sys.argv[7])

message = mailer.Message()
message.From = fromaddr
message.To = toaddrs
message.RTo = fromaddr
message.Subject = subject
message.Body = body

if ":" in host:
    host_data = host.split(":")
    port = host_data[1]
    host = host_data[0]
else:
    port = None

print message
sender = mailer.Mailer(host=host, use_tls=True, usr=username, pwd=password)

if(port):
    sender.port = port
sender.send(message)
