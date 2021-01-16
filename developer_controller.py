'''
The functions below show the real state among developers in this company
'''
from classes import Developer
from helpers import write_to
from helpers import read_from
from helpers import check_if_unique

FILE_PATH = "developers.json"

def engage_developer():
    '''
    hire an developer --- (create operation)
    '''
    name = input("\t Enter developer's name: ")
    years_of_experience = input("\t Enter developer's years of experience: ")
    salary = input("\t Enter a salary for developer: ")
    projects_str = input("\t Enter all projects that developer is working on. \n"
    "\t So enter name of the project followed by , \n"
    "\t For instance: Ime Projekta 1, Ime Projekta 2 \n"
    "\t Now your turn:" )
    list_of_projects = projects_str.split(",")
    developer = Developer(name, years_of_experience, salary, list_of_projects)
    output_data = {
        "name": developer.name,
        "years_of_experience": developer.years_of_experience,
        "salary": developer.salary,
        "list_of_projects": developer.list_of_projects
    }
    if check_if_unique(developer.name, FILE_PATH):
        write_to(output_data, FILE_PATH)
        print("\t Developer hired!")
    else:
        print("\t This entity already exists in database. Please, enter another one")

def get_developer():
    '''
    It considered name to be the primary key, so you can get developer by searching
    through database using his name. --- (read operation)
    '''
    developer = input("\t Enter developer's name: ")
    json_data = read_from(FILE_PATH)
    if json_data:
        #if is not empty
        for obj in json_data:
            if obj["name"] == developer:
                developer_projects = ""
                for project in obj["list_of_projects"]:
                    developer_projects += project + ","
                print("\t {} is a developer, with {} years of experience and he/she "
                "is engaged on several projects: {} for a salary {}"
                .format(obj["name"], obj["years_of_experience"],
                developer_projects[:-1], obj["salary"]))
                return
        print("\t We do not have a developer with that name!")
    else:
        print("\t We do not have a developer with that name!")

def get_least_experienced_developer():
    '''
    read and select
    '''
    json_data = read_from(FILE_PATH)
    experience_years = []
    if json_data:
        for obj in json_data:
            experience_years.append(int(obj["years_of_experience"]))
        min_experience = min(experience_years)

        for obj in json_data:
            if int(obj["years_of_experience"]) == min_experience:
                print("\t The least experienced developer is: {}".format(obj["name"]))
    else:
        print("\t File is empty. You haven't engaged any developer")

def list_developer_projects():
    '''
    It's nice to know on what projects developer is working on
    '''
    json_data = read_from(FILE_PATH)
    if json_data:
        name = input("\t Enter developer's name: ")
        for obj in json_data:
            if obj["name"] == name:
                developer_projects = ""
                for project in obj["list_of_projects"]:
                    developer_projects += project + ","
                print("\t Developer {} is working on projects: {}"
                .format(name, developer_projects[:-1]))
    else:
        print("\t No such developer")

def get_highest_payed_developer():
    '''
    Let's see who has the best results and thus the highest payed developer
    '''
    json_data = read_from(FILE_PATH)
    developers_salaries = []
    if json_data:
        for obj in json_data:
            developers_salaries.append(float(obj["salary"]))
        max_payed = max(developers_salaries)

        for obj in json_data:
            if float(obj["salary"]) == max_payed:
                print("\t The highest payed developer is: {}".format(obj["name"]))
    else:
        print("\t File is empty. You haven't engaged any developer")
