import mailbox
import csv
# GOT THIS FROM HERE: https://kamal.io/blog/exporting-email-threads-from-gmail-into-csv-file
#This doesn't give email content

writer = csv.writer(open("pratt_infoschool.csv", "w"))

for message in mailbox.mbox('[prattinfoschool].mbox'):
    writer.writerow([message['subject'], message["date"], message['from']])
