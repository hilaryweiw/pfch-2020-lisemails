import mailbox
import csv

# GOT THIS CODE FROM HERE : https://stackoverflow.com/questions/33537476/mailbox-to-csv-using-python
#THIS ONE WORKED

def get_message(message):
    if not message.is_multipart():
        return message.get_payload()
    contents = ""
    for msg in message.get_payload():
        contents = contents + str(msg.get_payload()) + '\n'
    return contents
#dont need the below code
#if __name__ == "__main__":

writer = csv.writer(open("pratt_infoschool_body.csv", "w"))
for message in mailbox.mbox("[prattinfoschool].mbox"):
    contents = get_message(message)
    writer.writerow([message["subject"], message["from"], message["date"],contents])
