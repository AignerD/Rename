import os
import csv

# Variables
application_path = os.getcwd() # 

# path = open(f'{application_path}\\names.csv')

csv_file = open(f'{application_path}\\names.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)
# site1 = initiate_nornir().filter(name="site1")

for i in csv_reader: 
    old,new_filename = i
    os.rename(f"{old}", f"{new_filename}")

from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('E:\Movies') if isfile(join('E:\Movies', f))]