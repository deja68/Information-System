'''
This module has functions that are controllers use frequently
so it's practical to write them here
'''
import json
from os import path

def read_from(file_path):
    '''
    reads from file
    '''
    if path.exists(file_path):
        with open(file_path,"r") as file:
            data = json.load(file)
        return data
    return None
def write_to(obj, file_path):
    '''
    writes data to file
    '''
    if not path.exists(file_path):
        output = []
    else:
        output = read_from(file_path)
    output.append(obj)
    with open(file_path,"w") as file:
        json.dump(output,file, indent = 4)
def check_if_unique(primary_key, file_path):
    '''
    say smth
    '''
    unique = True
    if path.exists(file_path):
        json_data = read_from(file_path)
        if json_data:
            #check if is not empty
            for obj in json_data:
                if obj["name"] == primary_key:
                    unique = False
    return unique
def delete_entity(name, file_path):
    '''
    say smth
    '''
    json_data = read_from(file_path)
    output_data = []
    if json_data:
        for obj in json_data:
            if obj["name"] != name:
                output_data.append(obj)
        with open(file_path,"w") as file:
            json.dump(output_data, file, indent = 4)
            print("\t Done!")
