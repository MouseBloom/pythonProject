import math
year_birth = int(1481074)
person_day = int(year_birth / 364)
person_sec = person_day / 86400
one_person = 21.42 # seconds for 1 person to be born
migration_year = 208000
one_migrant = 25.2 # amount of minutes when 1 person come to the country to stay
migration_from_country_year = 441000
one_migration_from_country = 1.2 # amount of minutes after which one person leave country
year_death = 1800000
time_of_one_person_death = 20 # seconds after which 1 person dies
time = int(input(''))
answer = (year_birth * time) + (migration_year * time) - (migration_from_country_year * time) - (year_death * time)
print('after ', one_person, ' seconds 1 person is born in Russia')
print('after ', one_migrant, ' minutes 1 person comes to country to stay here')
print('after ', one_magration_from_country, ' minutes 1 person leaves Russia to live in another country')
print('after ', time_of_one_person_death, ' seconds 1 person dies in Russia')
print('approximate population of Russia after ', time, ' years ', answer, ' people')
print('all the stats were taken from year 2019 and connected with the coronavirus situation and bad economic situation in Russia, so need to be recounted in future')

