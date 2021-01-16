'''
The view model
'''
import project_manager_controller as pm
import developer_controller as dc

OPERATION = 0
while OPERATION != -1:
    print("\t Available OPERATIONs: ")
    print("\t ----------------------------------------")
    print("""
        1: Engage a new project manager
        2: Show project manager's personal information
        3: Show all hired project managers 
        4: Update project manager's personal information 
        5: Fire a project manager
        6: Engage a new developer
        7: Show developer's personal information 
        8: Display information for the least experienced developer
        9: Display a list of projects that developer is engaged to6
        10: Display a developer with highest salary
    """)
    OPERATION = int(input("\t Chose a number next to the action you want to perform: "))

    if OPERATION == 1:
        pm.engage_project_manager()
    elif OPERATION == 2:
        pm.get_project_manager()
    elif OPERATION == 3:
        pm.get_all_project_managers()
    elif OPERATION == 4:
        pm.update_project_manager()
    elif OPERATION == 5:
        pm.fire_project_manager()
    elif OPERATION == 6:
        dc.engage_developer()
    elif OPERATION == 7:
        dc.get_developer()
    elif OPERATION == 8:
        dc.get_least_experienced_developer()
    elif OPERATION == 9:
        dc.list_developer_projects()
    elif OPERATION == 10:
        dc.get_highest_payed_developer()
    elif OPERATION < 0 or OPERATION > 10:
        break

    check = input("\t Do you want to proceed with more actions? Press [Y|N]: ")
    OPERATION = 0 if check.lower() == 'y' else -1
