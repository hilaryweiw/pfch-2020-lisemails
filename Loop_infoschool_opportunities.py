import csv

## For Pratt Information School All-Student Listserv
## Date July 31, 2019 - Feb 3, 2020
## 50 emails

# The goal is to loop through the subject column [0] and the email body column [1]
# to find each instances of the terms:
# Full-time --> sometimes ("FT," "Job") --> [for full time is it "Grant", "Termed" or "tenure"];
#     Part-time --> sometimes ("PT", "P/T");
#         Internship --> sometimes ("intern")--> [if it is "Paid or unpaid"];
#             Volunteer
# Dictionary ["Full-time", "Full time", "FT", "Job";
#         "Part-time", "Part time", "PT", "P/T", "Fellowship";
#         "Intern", "Internship",;
#         "Volunteer" ]

# For the Full-time term type do a seperate Python script
# For Internship paid or not do a seperate script
#
# Then export that all to another .csv to make a chart from!


######build a list for each term search in subjectline -->column[0]
full_time_terms = ["Full-time", "Full time", "FT", "Job", "Job:"]
part_time_terms = [ "Part-time", "Part time", "PT", "P/T", "Fellowship", "Graduate Assistant", "GA"]
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

#open the infoschool email body text csv
with open("infoschool_bodytext.csv","r") as infoschool_emailbody:
    info_body = csv.reader(infoschool_emailbody)

# loop through the row in subjectline column
    for column in info_body:
        email_subject = column[0]
        email_body = column[1]

        if any(term in email_subject for term in full_time_terms):
            full_time = full_time + 1
        # use to be if
        elif any(term in email_subject for term in part_time_terms):
            part_time = part_time + 1

        # use to be if
# how do you do search for variations "Intern" --> created a term list above
        elif any(term in email_subject for term in internship_terms):
            internship = internship + 1

# use to be if
        elif any(term in email_subject for term in volunteer_terms):
            volunteer = volunteer + 1

            #look for terms if it doesnt show in subject column[1] to loop through body column
            #if it apears in body we will count it
        else:
            #if there are different terms in the email body create new lists for  "full_time_bodyterms"
            if any(term in email_body for term in full_time_terms):
                full_time = full_time + 1

                # use to be if
            elif any(term in email_body for term in part_time_terms):
                part_time = part_time + 1

            # use to be if
    # how do you do search for variations "Intern" --> created a term list above
            elif any(term in email_body for term in internship_terms):
                internship = internship + 1

    # use to be if
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
with open("loop_results_infoschool.csv","w") as csv_out:
    csv_writer = csv.writer(csv_out)
#this writes a new column for every term in the csv and the counter
    csv_writer.writerow(["Full Time", full_time])
    csv_writer.writerow(["Part Time", part_time])
    csv_writer.writerow(["Internship", internship])
    csv_writer.writerow(["Volunteer", volunteer])

#     ##RESULTS
# FT 24
# -------
# PT 10
# -------
# Internship 8
# -------
# Volunteer 1

#---------------------------------
