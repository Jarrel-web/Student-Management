import csv
from student.student import Student
def read_csvfile(filepath):
    allstudents = []
    try:
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    tut_grp = row.get('Tutorial Group', 'Unknown')
                    student_id = row.get('Student ID', 'Unknown')
                    school =row.get('School', 'Unknown')
                    name =row.get('Name', 'Unknown')
                    gender =row.get('Gender', 'Unknown')
                    cgpa =float(row.get('CGPA',0.0))
                    student = Student(tut_grp,student_id,school,name,gender,cgpa)
                    allstudents.append(student)
                except ValueError:
                    print(f"Invalid CGPA value in row {row}")
                    continue
            print("Successfully stored student's details")        
    except(FileNotFoundError, PermissionError) as e:
         print(f"An error occurred: {e}")
    except Exception as e:  
         print(f"An error occurred: {e}")
    return allstudents
    
def write_csv(all_teams):
    print("Commence writing csv")
    with open('assign_team_records.csv','w') as file:
        file.write('Tutorial Group,Student ID,School,Name,Gender,CGPA,Team Assigned\n')
        for student in all_teams:
            tut_grp=student.tut_grp
            student_id=student.id
            school=student.school
            name=student.name
            gender=student.gender
            cgpa=str(student.cgpa)
            team_assigned=student.team_assigned
            file.write(tut_grp+','+student_id+','+school+','+name+','+gender+','+cgpa+','+team_assigned+'\n')