# pfch-2020-lisemails
April 2020

For INFO 664-PFCH  2020 final @ *Pratt Institute School of Information*
Matt Miller's class Spring 2020

Project goal was to analyze types of work opportunities sent out on the Pratt Information School listserv emails.  
In February 2020 Pratt Information School created new listservs specifically geared towards each of the four tracks. I decided to create two datasets to parse through:

1. Old “All Students’ listserv
2. New LIS specific listserv

Exported emails → .mbox files from Pratt email using Google Takeout.
Then used a Python script and the csv module → "Export_..py" files to export “subject line” and “email content” data from the .mbox files to write into a .csv

**Note** the exported "email content" .csv files were really messy and terminology used within the emails themselves are inconsistent which made looping through the .csv files a challenge. So I exported two .csv files: 1. Just “subject line” so I could see how many emails were in each data set 2. .csv with “subject line” and “email content.”

Then used a Python script to searched for a breakdown of the number of *full-time, part-time, internship, and volunteer opportunities* using Python loops to search the "subject line" then the "email content" columns in the .csv files for the above terms and wrote it out to a new .csv file 

Finally, a Python script was used to further breakdown the data set to look at the composition of:

1. Full-time opportunities → grant funded or tenured.
2. Internships → paid or unpaid.

