import os

__author__ = 'Brandon'

from utils.UtilClass import UtilClass


var = UtilClass(table='Client')

print(var.file_read_util(os.getcwd()+'\SampleClientData'))







