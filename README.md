# pfch-2020-lisemails
April 2020

For pfch 2020 final @ Pratt Institute School of Information
Matt Miller's class Spring 2020

Exported emails → .mbox from Pratt email.
In February 2020 Pratt Information School created new listservs specifically geared
towards each of the four tracks so two .mbox exports created using Google Takeout:
1. Old “All Students’ listserv
2. New LIS specific listserv

Then used a Python script "Export_..py" files to export data from the .mbox files in a .csv
Note the exported "email content" .csv files were really messy and terminology used within the emails themselves are inconsistent which made looping through the .csv files a challenge. So I exported two .csv files; 1. Just subjectline so I could see how many emails 2. .csv with email content.

Results searched for a breakdown of the number of Full-time, part-time, Internship, and volunteer opportunities using Python loops to search the "subject line" then the "email content" columns in the .csv files for the above terms. 

Then wrote another Python script to further breakdown specifically looking at the composition of:
1. Full-time opportunities → grant funded or tenured.
2. Internships → paid or unpaid.
