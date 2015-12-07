import json
from datetime import date

__author__ = 'Brandon'

from Insert_Data.Data_Insert import ClientDataInsert, InsuranceDataInsert, PatientDataInsert

class UtilClass:

    def __init__(self, **kwargs):

        if kwargs['table'] == 'Client':
            self.table_handle = ClientDataInsert()
        elif kwargs['table'] == 'Insurance':
            self.table_handle = InsuranceDataInsert()
        elif kwargs['table'] == 'Patient':
            self.table_handle = PatientDataInsert()


    def file_read_util(self, input_file):

        #Find out fields associated with input file
        with open(input_file, 'r') as data_load:
            get_first_line = data_load.readline()

            for i in data_load.readlines():
                insertion_dict = json.loads(i)
                if 'due_date' or 'todays_date' in insertion_dict:
                    insertion_dict['due_date'] = date.today()
                    insertion_dict['todays_date'] = date.today()

                self.table_handle.insert_data(**insertion_dict)




