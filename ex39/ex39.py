# -*-coding:utf8


# oreate a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Hawaii': 'HI',
}

# oreate a basic set of states and some oities in them
cities ={
    'CA': 'Los Angeles',
    'HI': 'Honolulu',
    'FL': 'Jacksonville'
}

# add some more citties
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

#print some states
print('-' * 10)
print("Hawaii's abbreviation is: %s" % states['Hawaii'])
print("Florida's abbreviation is: %s" % states['Florida'])

#print every state abbreviation
print('-' * 10)
print("states = %s" % states)
print("states .items() =  %s" % str(states.items()))
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

#print every city in state
print('-' * 10)
for abbrev, city in states.items():
    print("%s has the city %s" % (abbrev, city))

#now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))



print('-' * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'Not Entered Yet')
print("The city for the state 'TX' is: %s" % city)









