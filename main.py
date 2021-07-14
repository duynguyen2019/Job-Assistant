from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import os
import pandas as pd
from faker import Faker
from time import sleep
from random import randint
import datetime
import pytz

# Import local functions
from db_info import *
from send_mail import *
from generateCoverLetter import *
from generateEmailContent import *
from send_mail import *



fake = Faker()
def main():
    print('Script ran')

if __name__ == '__main__':
    #Recruiter INFO
    job_info = [
                {"firstname": fake.name().split(" ")[0],
                 "lastname": fake.name().split(" ")[1],
                 "email": "duynguyenms2021@gmail.com",
                 "position":fake.job(),
                 "company":fake.company()} for _ in range(0,3)   
                    ]
    print("Writing recruiter's info to database")
    maxid = pd.read_sql("SELECT MAX(objectid) AS max_id from tbl_email",eng)['max_id'].iloc[0]
    df = pd.DataFrame(job_info)
    df['objectid'] = [x for x in range(maxid+1,maxid+len(df)+1)]
    df['date_sent'] = pd.Timestamp(datetime.datetime.now(pytz.timezone('US/Pacific')))
    df.to_sql('tbl_email',eng,index=False, if_exists='append')
    print("Successfully pushing data into the database")
    
    for job in job_info:  
        print(f"Generating Cover Letter for {job['position']} at {job['company']}")
        generateCoverLetter(job)
        print(f"Generating Email Content for {job['position']} at {job['company']}")
        text, html = generateEmailContent(job)
        sender = "duynguyen1993@csu.fullerton.edu"
        recipient = job['email']
        subject = f"{job['position']} at {job['company']}"
        attachment_list = ["attachments/Resume_DN.pdf",
                        f"attachments/Duy Nguyen_{job['company']}_CoverLetter.pdf"]
        print(f"Sending email to {recipient}")
        send_mail(sender, recipient, subject, attachment_list, text, html)
        sleep(randint(0, 10))
        print("All done!")
