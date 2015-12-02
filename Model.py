from sqlalchemy import Column, ForeignKey, Integer, String, Date, create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship

__author__ = 'Brandon'

Base = declarative.declarative_base()


class Insurance(Base):
    __tablename__ = "Insurance"

    id = Column(Integer, primary_key=True)
    Insurance_Name = Column(String(40))


class Patient(Base):
    __tablename__ = "Patient"

    first_name = Column(String(20))
    last_name = Column(String(20))
    id = Column(Integer, primary_key=True)


class Client(Base):
    __tablename__ = "Client"

    id = Column(Integer, primary_key=True)
    patient_Id = Column(Integer, ForeignKey('Patient.id'), nullable=False)

    insurance_Id = Column(Integer, ForeignKey('Insurance.id'), nullable=False)
    insurance = relationship(Insurance)

    priority = Column(String(10))
    due_date = Column(Date)
    todays_date = Column(Date)
    summary = Column(String(100))
    note = Column(String(100))


customer_tracker = create_engine('sqlite:///customerTrackerDB.db')

Base.metadata.create_all(customer_tracker)








