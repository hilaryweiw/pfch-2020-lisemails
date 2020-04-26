import mailbox
import csv
# GOT THIS FROM HERE: https://kamal.io/blog/exporting-email-threads-from-gmail-into-csv-file
#This doesn't give email content

writer = csv.writer(open("lis_subjectline.csv", "w"))

for message in mailbox.mbox('[prattischool-lis].mbox'):
    writer.writerow([message['subject'], message['from'], message["date"]])
