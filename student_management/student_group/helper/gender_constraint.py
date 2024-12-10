def gender_constraint(males,females,team_size):
    male_ratio = len(males)/(len(males)+len(females))
    target_males = min(round(team_size * male_ratio), (team_size // 2 + team_size % 2))  
    target_females = team_size - target_males

    return target_males,target_females