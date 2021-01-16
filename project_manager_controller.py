'''
These functions are describing project manager's behavior
'''
from classes import ProjectManager
from helpers import write_to
from helpers import read_from
from helpers import check_if_unique
from helpers import delete_entity

FILE_PATH = "project_manager.json"

def engage_project_manager():
    '''
    hire an employee - create operation
    '''
    name = input("\t Enter project manager's name: ")
    years_of_experience = input("\t Enter project manager's years of experience: ")
    salary = input("\t Enter a salary for product manager: ")
    supervises_project = input("\t Enter a project that project manager supervises: ")

    project_manager = ProjectManager(name, years_of_experience, salary, supervises_project)
    output_data = {
        "name": project_manager.name,
        "years_of_experience": project_manager.years_of_experience,
        "salary": project_manager.salary,
        "supervises_poject": project_manager.supervises_project
    }
    if check_if_unique(project_manager.name, FILE_PATH):
        write_to(output_data, FILE_PATH)
        print("\t Project manager hired!")
    else:
        print("\t This entity already exists in database. Please, enter another one")

def get_project_manager():
    '''
    select a project manager with certain name -- read operation
    '''
    manager_name = input("\t Enter project manager's name: ")
    json_data = read_from(FILE_PATH)
    if json_data:
        #if is not empty
        for obj in json_data:
            if obj["name"] == manager_name:
                print("\t {} is a project manager, with {} years of experience and he/she"
                " is engaged on a {} for a salary {}"
                .format(obj["name"], obj["years_of_experience"],
                obj["supervises_poject"], obj["salary"]))
                return
        print("\t We do not have a project manager with that name!")
    else:
        print("\t We do not have a project manager with that name!")

def get_all_project_managers():
    '''
    it comes handy to see all project managers hired (read operation)
    '''
    json_data = read_from(FILE_PATH)
    if json_data:
        for obj in json_data:
            print("\t {} ".format(obj["name"]))
    else:
        print('\t There are no project managers at all!')

def update_project_manager():
    '''
    It considered name to be the primary key, so user is promted to one
    to be able to change one of 3 other fields --- (update operation)
    '''
    json_data = read_from(FILE_PATH)
    if json_data:
        name = input("\t Enter project manager's name: ")
        print("\t You can update one of three following options: ")
        print("\t ----------------------------------------")
        print("""
            1: years of experience
            2: salary
            3: project that's being supervised
        """)
        option = int(input("\t Choose a number next to the action you want to perform: "))
        for obj in json_data:
            if obj["name"] == name:
                if option == 1:
                    years_of_experience = input("\t Enter project manager's years of experience: ")
                    if years_of_experience:
                        delete_entity(name, FILE_PATH)
                        obj["years_of_experience"] = years_of_experience
                        write_to(obj, FILE_PATH)
                elif option == 2:
                    salary = input("\t Enter a salary for product manager: ")
                    if salary:
                        delete_entity(name, FILE_PATH)
                        obj["salary"] = salary
                        write_to(obj, FILE_PATH)
                elif option == 3:
                    supervises_project = input("\t Enter a project that is "
                    "being supervised by project manager: ")
                    if supervises_project:
                        delete_entity(name, FILE_PATH)
                        obj["supervises_project"] = supervises_project
                        write_to(obj, FILE_PATH)
                elif option < 1 or option > 3:
                    print("\t That's not an option")
                    break
def fire_project_manager():
    '''
    Project manager has done something bad and he need to be fired immediately!
    (delete operation)
    '''
    name = input("\t Enter project manager's name you want to fire: ")
    delete_entity(name, FILE_PATH)
