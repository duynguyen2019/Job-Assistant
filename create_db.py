from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import os
from send_mail import *
import pandas as pd
from db_info import *

meta = MetaData(schema = "public")
tbl_email = Table(
   'tbl_email', meta, 
   Column('objectid', Integer, primary_key = True), 
   Column('first_name', String), 
   Column('last_name', String),
   Column('email_address',String) 
)
meta.create_all(eng)
results = pd.read_sql("SELECT DISTINCT(table_name) FROM INFORMATION_SCHEMA.columns WHERE table_name LIKE 'tbl_%%'",eng) 
df = pd.read_sql("SELECT * FROM tbl_email",eng)
df = pd.DataFrame({
                    'objectid':[1], 
                    'first_name':['Duy'],
                    'last_name':['Nguyen'],
                    'email_address':['duynguyen2021ms@gmail.com'] 
                    })