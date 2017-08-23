# coding:utf-8

cities = {'CA':'San Francisco', 'MI':'Detroit','FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print cities.items()
# >>> [('FL', 'Jacksonville'), ('CA', 'San Francisco'), ('MI', 'Detroit'), ('OR', 'Portland'), ('NY', 'New York')]

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not Found."

cities['_find'] = find_city

for state in cities.items():
    print "State? (Enter to quit)",
    state = raw_input(">")

    if not state: break

    city_found = cities['_find'](cities,state)
    print city_found
