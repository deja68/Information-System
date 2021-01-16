'''
The idea is to model 2 types of employees in one IT company.
'''

class Employee:
    '''
    This is an abstract class
    '''
    def __init__(self, name, years_of_experience, salary):
        self._name = name
        self._years_of_experience = years_of_experience
        self._salary = salary

    @property
    def name(self):
        '''property method for getting name'''
        return self._name

    @name.setter
    def name(self, employee_name):
        if isinstance(employee_name) == str:
            self._name = employee_name

    @property
    def salary(self):
        '''
        property method for retrieving salary
        '''
        return self._salary

    @salary.setter
    def salary(self, employee_salary):
        if isinstance(employee_salary) == float and employee_salary >= 500:
            self._salary = employee_salary

    @property
    def years_of_experience(self):
        '''
        property method for getting years of experience
        '''
        return self._years_of_experience

    @years_of_experience.setter
    def years_of_experience(self, experience):
        if isinstance(experience) == int:
            self._years_of_experience = experience
    def __str__(self):
        return '{0._name!s} {0._years_of_experience!s} {0._salary!s}'.format(self)

class ProjectManager(Employee):
    '''
        ProdjectManager is a subclass
    '''
    def __init__(self, name, years_of_experience, salary, supervises_project):
        super().__init__(name, years_of_experience, salary)
        self._supervises_project = supervises_project

    @property
    def supervises_project(self):
        '''
        method for getting project that is being supervied by project manager
        '''
        return self._supervises_project
    @supervises_project.setter
    def supervises_project(self, project):
        if isinstance(project)==str:
            self._supervises_project = project
    def __repr__(self):
        manager_dict = {
            "name": self._name,
            "years_of_experience": self._years_of_experience,
            "salary": self._salary,
            "supervises_project": self._supervises_project
        }
        return str(manager_dict) + "\n"



class Developer(Employee):
    '''
        Developer is a subclass of class Employee
    '''
    def __init__(self, name, years_of_experience, salary, list_of_projects = None):
        #it's safer to put None insted of []
        super().__init__(name, years_of_experience, salary)
        self._list_of_projects = list_of_projects
    @property
    def list_of_projects(self):
        '''
        getter for list of products
        '''
        return self._list_of_projects
    @list_of_projects.setter
    def list_of_projects(self, projects_list):
        if isinstance(projects_list)==list:
            for project in projects_list:
                self.list_of_projects.append(project)
    def __str__(self):
        developer_dict = {
            "name": self._name,
            "years_of_experience": self._years_of_experience,
            "salary": self._salary,
            "list_of_projects": self._list_of_projects
        }
        return str(developer_dict)
