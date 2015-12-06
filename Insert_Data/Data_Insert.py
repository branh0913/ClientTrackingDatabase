from datetime import date
import json

__author__ = 'Brandon'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import abc
from abc import ABCMeta


from Model import Client, Insurance, Patient, Base

engine = create_engine('sqlite:///../customerTrackerDB.db')


class DataInsertion:

    __metaclass__ = ABCMeta

    @abc.abstractclassmethod
    def insert_data(self, **kwargs):
        pass


class ClientDataInsert(DataInsertion):

    def __init__(self):

        Base.metadata.bind =engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def insert_data(self, **kwargs):

        client_table_obj = Client(id=kwargs['id'], patient_Id=kwargs['patient_Id'],
                                  insurance_Id=kwargs['insurance_Id'], priority=kwargs['priority'],
                                  due_date=kwargs['due_date'], todays_date=kwargs['todays_date'],
                                  summary=kwargs['summary'])

        self.session.add(client_table_obj)
        print(self.session.commit())

class InsuranceDataInsert(DataInsertion):

    def __init__(self):

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def insert_data(self, **kwargs):

        insurance_table_obj = Insurance(id=kwargs['id'], Insurance_Name=kwargs['Insurance_Name'])
        self.session.add(insurance_table_obj)
        print(self.session.commit())

class PatientDataInsert(DataInsertion):

    def __init__(self):

        Base.metadata.bind = engine
        DBSession = sessionmaker()
        self.session = DBSession()

    def insert_data(self, **kwargs):

        patient_table_obj = Patient(id=kwargs['id'], last_name=kwargs['last_name'],
                                    first_name=kwargs['first_name'])
        self.session.add(patient_table_obj)
        print(self.session.commit())



# if __name__ == "__main__":
#
#     client_insert_inst = ClientDataInsert()
#     insurance_insert_inst = InsuranceDataInsert()
#     # patient_insert_inst = PatientDataInsert()
#
#     with open('SampleClientData') as ClientIputs:
#         for clientrec in ClientIputs.readlines():
#             client_insertion_json = json.loads(clientrec)
#             client_insertion_json['due_date'] = date.today()
#             client_insertion_json['todays_date'] = date.today()
#             client_insert_inst.insert_data(id=int(client_insertion_json['id']),
#                                            patient_Id=client_insertion_json['patient_Id'],
#                                            insurance_Id=client_insertion_json['insurance_Id'],
#                                            priority=client_insertion_json['priority'],
#                                            due_date=client_insertion_json['due_date'],
#                                            todays_date=client_insertion_json['todays_date'],
#                                            summary=client_insertion_json['summary'])
#
#     with open('SampleInsuranceData') as InsuranceInputs:
#         for insurancerec in InsuranceInputs.readlines():
#             insurance_insertion_json = json.loads(insurancerec)
#             insurance_insert_inst.insert_data(id=insurance_insertion_json['id'],
#                                               Insurance_Name=insurance_insertion_json['Insurance_Name'])
#
#
#
#
#
# # sample_client_record = Client(id=5, patient_Id=5, insurance_Id=5, priority="HIGH", due_date=date.today(),
# #                               todays_date=date.today(),
# #                               summary="One word, bad!", note="It killed me!")
# # session.add(sample_client_record)
# # session.commit()
# #
# # sample_insurance_record = Insurance(id=5, Insurance_Name="Shrewd Insurance")
# # session.add(sample_insurance_record)
# # session.commit()
# #
# # sample_patient_record = Patient(id=5, first_name="Frank", last_name="Underwood")
# # session.add(sample_patient_record)
# # session.commit()
#
