from sqlalchemy import create_engine, Column, Integer, String,MetaData,ForeignKey,DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from datetime import datetime
import os

metadata = MetaData()

load_dotenv()
"""
Here this engine which will call create_engine function passing parameters.
-Databasetype
-username
-password
-host
-port
-database name
"""
engine = create_engine(f'mysql://{os.getenv("sanusername")}:{os.getenv("sanpassword")}@{os.getenv("host")}:{os.getenv("port")}/vivaan')
"""
-Session Manages persistence operations for ORM-mapped objects.
-sessionmaker is a configurable Session factory.
-bind is the connection object.
"""
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class StudentData(Base):
    """[Here i have created a class "StudentData"]

    Args:
        Base
    -Here i have created a table with detailed columns.
    """
    __tablename__ = 'student_data'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teacher_data.teacher_id'))
    date_added_on = Column(DateTime, onupdate=datetime.now)
    def __repr__(self):
        return f"name:{self.name},age:{self.age},grade:{self.grade}, date: {self.added_on_date}"

class TeacherData(Base):
    
    __tablename__ = "teacher_data"
    id = Column(Integer, primary_key = True)
    teacher_name = Column(String(50))
    student = relationship("StudentData")
    def __repr__(self):
        return f"name:{self.teacher_name}"
