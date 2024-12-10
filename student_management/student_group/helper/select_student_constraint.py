def check_gender(gender):
    if gender == 'Male':
        return True
    else:
        return False
def check_school(school,school_count,school_constraint):
    if school_count.get(school,0)+1 <= school_constraint:
        return True
    else:
        return False

def update_school_count(school,school_count):
   
    if school in school_count:
        school_count[school] += 1
    else:
        school_count[school] = 1
    return school_count