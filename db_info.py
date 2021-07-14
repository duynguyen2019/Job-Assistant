import os
from sqlalchemy import create_engine

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
eng = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}")

