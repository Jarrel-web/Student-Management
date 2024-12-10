
def sort_by_tutorialgrp(students):
    tutorial_groups = {}
    for student in students: #For each student in student, the tutgroup will append the student based on said tutorial group
        tutgroup = student.tut_grp
        if tutgroup not in tutorial_groups: #if tutgroup is not stated, it will create a new one
            tutorial_groups[tutgroup] = []
        tutorial_groups[tutgroup].append(student) 
    print("Successfully sort by tutorial group")
    return tutorial_groups

def sort_by_gender_cgpa(students):
    
    males = []
    females = []
    #Sort students based on gender and split them into 2 list: males and females
    for student in students:
        if student.gender == 'Male':
            males.append(student)
        else:
            females.append(student)
    
    
    # Sort males and females by CGPA in ascending order
    males = sorted(males, key=lambda student: student.cgpa)
    females = sorted(females, key=lambda student: student.cgpa)
    
    return males, females