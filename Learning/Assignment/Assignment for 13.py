
def Age(year,current_year=2022):
    age_now = current_year - int(year)
    return age_now


old = Age(1980)
print(old)