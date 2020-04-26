import csv

## For Pratt Information School LIS track only listserv
#Date Range from Feb 14, 2020 -- April 2, 2020
##18 emails

full_time_terms = ["Full-time", "Full time", "FT", "Job", "Job:"]
part_time_terms = [ "Part-Time", "Part-time", "Part time", "PT", "P/T", "Fellowship", "Graduate Assistant", "GA"]
internship_terms =["Intern", "Internship", "Internship:"]
volunteer_terms = ["Volunteer", "Volunteers"]

##### build a list for each term in body -->column[1]
full_time_bodyterms = ["Full-time", "Full time", "FT", "job", "tenured", "tenure", "tenure-track"]
part_time_bodyterms = ["Part-time", "Part time", "PT", "P/T", "Fellowship", "Graduate Assistant", "Library Page"]
intnership_bodyterms = ["Intern", "Internship", ""]
volunteer_bodyterms = ["volunteers","volunteer", "Volunteers", "Volunteer"]
# two count how many times each apears?
full_time = 0
part_time = 0
internship = 0
volunteer = 0

#open the lis school email body text csv
with open("lis_bodytext.csv","r") as lis_emailbody:
    lis_body = csv.reader(lis_emailbody)

# loop through the row in subjectline column
    for column in lis_body:
        email_subject = column[0]
        email_body = column[2]

        if any(term in email_subject for term in full_time_terms):
            full_time = full_time + 1

        elif any(term in email_subject for term in part_time_terms):
            part_time = part_time + 1

        elif any(term in email_subject for term in internship_terms):
            internship = internship + 1

        elif any(term in email_subject for term in volunteer_terms):
            volunteer = volunteer + 1

            #look for terms if it doesnt show in subject column[3] to loop through body column
            #if it apears in body we will count it
        else:
            if any(term in email_body for term in full_time_terms):
                full_time = full_time + 1

            elif any(term in email_body for term in part_time_terms):
                part_time = part_time + 1

            elif any(term in email_body for term in internship_terms):
                internship = internship + 1

            elif any(term in email_body for term in volunteer_terms):
                volunteer = volunteer + 1


    print("FT", full_time)
    print("-------")
    print("PT", part_time)
    print("-------")
    print("Internship", internship)
    print("-------")
    print("Volunteer", volunteer)


    #this will write it to a csv.
with open("loop_results_lis.csv","w") as csv_out:
    csv_writer = csv.writer(csv_out)
#this writes a new column for every term in the csv and the counter
    csv_writer.writerow(["Full Time", full_time])
    csv_writer.writerow(["Part Time", part_time])
    csv_writer.writerow(["Internship", internship])
    csv_writer.writerow(["Volunteer", volunteer])
    ##RESULTS##
# FT 8
# -------
# PT 1
# -------
# Internship 5
# -------
# Volunteer 0
