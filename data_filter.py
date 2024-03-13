# Question: Create a script that uses the attached countries_by_area.txt
# file as data source and prints out the top 5 most densely populated countries.
# Expected output:
#     India
#     Pakistan
#     Nigeria
#     China
#     Indonesia

import pandas

countries = pandas.read_csv('countries_by_area.txt')

countries.insert(4, 'density', countries['population_2013'] / countries['area_sqkm'] )

# print(countries)

sorted_countries = countries.sort_values(by = 'density', ascending= False)

for index, row in sorted_countries[:5].iterrows():
    print(row["country"])
