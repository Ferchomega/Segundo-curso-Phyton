countries = ["México", "Venezuela", "Colombia", "Argentina" ]
"""ages = [12,18,24,34,50]
print(id(countries))
print(countries)
countries[0]= "Ecuador"
print(countries)"""

"""name = "David"
print(name [0])
name[0]= d
print (name)"""


import copy

print(countries)
global_countries = None
global_countries = copy.copy(countries) #copy te ayuda para que se no se modifique la lista global para que sean independientes el global
global_countries [0] = "Honduras"
print(countries)
print(global_countries)

for country in countries:
    print(country)