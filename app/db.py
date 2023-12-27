import os

from sqlmodel import SQLModel, create_engine

DATABASE_URL = f"sqlite:///../data/{os.environ.get('DB_NAME', 'processed_data_2023.db')}"

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
