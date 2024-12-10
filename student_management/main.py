from file_operation.file_op import *
from student_group.sort_group import *
from student_group.form_team import form_teams
def main():
    try:
      team_size = int(input("Please input team size (4-10): "))
      while team_size<4 or team_size>10:
         print("You have entered a invalid team size")
         team_size = int(input("Please input team size (4-10): "))
    except ValueError:
         print("The user did not enter a valid number")
         main()
    all_teams = []
    file_path = "student_management/assets/records.csv"
    students = read_csvfile(file_path)
    tutorial_groups = sort_by_tutorialgrp(students)
    for group in tutorial_groups:
        tutorial_groups[group] = sort_by_gender_cgpa(tutorial_groups[group])
    for tutorial_group, (males,females) in tutorial_groups.items():
        print('Forming teams for ' + tutorial_group + '...')
        teams = form_teams(males,females,team_size)
        print('Forming teams for ' + tutorial_group + ' is done')
        for i, team in enumerate(teams, 1):
            for student in team:
                group = student.tut_grp
                student.team_assigned = f"{group}_Team{i}"
            all_teams.extend(team)
           
    write_csv(all_teams)
if __name__ == '__main__':
     main()