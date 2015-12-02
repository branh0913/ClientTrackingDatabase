from sqlalchemy import Column, ForeignKey, Integer, String, Date, create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship

__author__ = 'Brandon'



Base = declarative.declarative_base()

class Insurance(Base):

    __tablename__ = "Insurance"

    Insurance_Id = Column('Id', Integer, primary_key=True)
    Insurance_Name = Column('InsuranceName', String(40))

class Patient(Base):

    __tablename__ = "Patient"

    first_name = Column("FirstName", String(20))
    last_name = Column("LastName", String(20))
    patient_id = Column("Id", Integer, primary_key=True)

class Client(Base):

    __tablename__ = "Client"

    client_Id = Column('Id', Integer, primary_key=True)
    patient_Id = Column('PatientId', Integer, ForeignKey('Patient.Id'), nullable=False)

    insurance_Id = Column('InsuranceId', Integer, ForeignKey('Insurance.Id'), nullable=False)
    insurance = relationship(Insurance)

    priority = Column('Priority', String(10))
    due_date = Column('DueDate', Date)
    todays_date = Column('TodaysDate', Date)
    summary = Column('Summary', String(100))
    note = Column('Note', String(100))




customer_tracker = create_engine('sqlite:///customerTrackerDB.db')

Base.metadata.create_all(customer_tracker)








