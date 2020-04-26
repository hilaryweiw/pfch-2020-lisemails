import csv

# The goal is to loop through the subject column [0] and the email body column [1]
# to find each instances of the terms:
# Full-time --> sometimes ("FT," "Job") --> [for full time is it "Grant", "Termed" or "tenure"];

# Internship --> sometimes ("intern")--> [if it is "Paid or unpaid"];
# Then determine with in each of the above the types of Full-time or internships


#Job type terms
full_time_terms = ["Full-time", "Full time", "FT", "Job", "Job:"]
internship_terms =["Intern", "Internship", "Internship:"]

#Type of full-time job
grant_terms = ["Grant", "grant", "termed", "Termed", "grant-funded", "fellowship", "temporary" ,"1-year", "2-year"]
tenured_terms =["tenured," "tracked", "tenure-track", "Tenure-track"]
#type of internship
paid_terms = ["paid", "Paid"]
unpaid_terms = ["unpaid", "Unpaid", "(unpaid)", "volunteer", "Volunteer", "credit"]

#full-time type count
grant = 0
tenured = 0
#Internship type count
paid = 0
unpaid = 0

#open the infoschool email body text csv
with open("infoschool_bodytext.csv","r") as infoschool_emailbody:
    info_body = csv.reader(infoschool_emailbody)

# loop through the row in subjectline column
    for column in info_body:
        email_subject = column[0]
        email_body = column[1]

        if any(term in email_subject for term in full_time_terms):
            #create a list for grant if multi terms like for full_time
            if any(term in email_body for term in grant_terms):
                # if "grant" in email_body:
                grant = grant + 1
            if any(term in email_body for term in tenured_terms):
                #counter
                tenured = tenured + 1
# in addition to searching for internships
        elif any(term in email_subject for term in internship_terms):

            if any(term in email_body for term in paid_terms):
                paid = paid + 1

            if any(term in email_body for term in unpaid_terms):
                unpaid = unpaid + 1

    print('Grant Funded', grant)
    print("Tenured", tenured)
    print("Paid Internship", paid)
    print("Unpaid Internship", unpaid)
