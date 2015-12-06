import json

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
            # field_list = {k: v for k,v }
            self.table_handle.insert_data(**field_list)




