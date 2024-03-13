# Question: Please take a look at the following list:
# checklist = ["Portugal", "Germany", "Munster", "Spain"]
# One of the items is not a country. Please use Python and the file
# containing the list of countries (attached) as the data source to
# filter out the checklist  of non-country items. Once you have filtered
# out checklist , then print it out.

checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('countries_clean.txt', 'r') as f:
    countries = list(f.readlines())

countries = [c.strip('\n') for c in countries if '\n' in c]
# print(countries)

checked = [c for c in checklist if c in countries]

print(checked)
