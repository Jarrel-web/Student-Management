from student_group.helper.gender_constraint import *
from student_group.helper.select_student_constraint import *
from student_group.helper.calculate_cgpa_range import *

def form_teams(males,females, team_size):
     teams = []
     #Number of students from the same school constraint
     max_school_ratio=0.5
     school_constraint = int(max_school_ratio*team_size)
     

     try:
        target_teams = int((len(males)+len(females))/team_size)
        while (males or females) and len(teams) <target_teams: 
            target_male,target_female = gender_constraint(males,females, team_size)
            team = []
            school_count = {}

            for _ in range(target_male):
                if males:
                    for i in range(len(males)):
                        selected_student = males[i]
                        school = selected_student.school
                        valid_school = check_school(school,school_count,school_constraint)
                        if valid_school:
                            team.append(selected_student)
                            school_count = update_school_count(school,school_count)
                            males.pop(i)
                            break
                        
            for _ in range(target_female):
                if females:
                    for i in range(len(females)-1,-1,-1):
                         selected_student = females[i]
                         school = selected_student.school
                         valid_school = check_school(school,school_count,school_constraint)
                         if valid_school:
                            team.append(selected_student)
                            school_count = update_school_count(school,school_count)
                            females.pop(i)
                            break
                         
            while len(team) < team_size:
                if males:
                    middle_index = len(males)//2
                    team.append(males.pop(middle_index))
                # Add from females if available
                if len(team) < team_size and females:
                    # Choose the middle female if there are females left
                    middle_index = len(females) // 2
                    team.append(females.pop(middle_index))   
            teams.append(team) 
            if len(teams) == target_teams:
                leftover_students = males + females
                if leftover_students:
                # Calculate the average CGPA for each team
                    avg_groups = [
                        sum(student.cgpa for student in team) / len(team) if team else 0
                        for team in teams
                    ]

                # Calculate the number of students to add (leftover students)
                no_of_students_to_add = len(leftover_students)

                for i in range(no_of_students_to_add):
                    if leftover_students:
                        student = leftover_students.pop(0)  # Take the next student from the leftover list

                        # Try adding the student to each team and calculate the new CGPA range
                        best_team_index = None
                        best_new_range = float('inf')  # Initialize with a very high value

                        # Evaluate adding the student to each team
                        for idx, team in enumerate(teams):
                            # Create a temporary team list to simulate adding the student
                            temp_team = team + [student]

                            # Calculate the new average CGPA for each team after adding the student
                            temp_avg_groups = avg_groups[:]
                            temp_avg_groups[idx] = sum(s.cgpa for s in temp_team) / len(temp_team)

                            # Calculate the range of CGPAs for all teams after adding the student
                            new_range = max(temp_avg_groups) - min(temp_avg_groups)

                            # If the new range is smaller, this team is a better choice
                            if new_range < best_new_range:
                                best_new_range = new_range
                                best_team_index = idx

                        # Add the student to the best team that minimizes the CGPA range
                        teams[best_team_index].append(student)

                        # Update the average CGPA for the selected team
                        avg_groups[best_team_index] = sum(s.cgpa for s in teams[best_team_index]) / len(teams[best_team_index])


            
                   

     except IndexError as e:
        raise RuntimeError(f"An error occurred while processing students: {e}")
     return teams

