from pprint import pprint
burger = {
    'patties': 1,
    'patty_type': 'beef',
    'cheese': True,
    'toppings': ['lettuce', 'tomato', 'onion', 'pickles', 'ketchup', 'mustard'],
    'bun': 'sesame seed',
}

print(f"{burger["patties"]} {burger["patty_type"]} patties on your burger.")

print(f"Your burger has {burger['bun']} bun.")
if burger['cheese']:
    print("Cheese is on your burger.")
else:
    print("No cheese on your burger.")

# List toppings
for topping in burger['toppings']:
    print(f"- {topping}")

all_toppings = burger['toppings']

for topping in all_toppings:
    print(f"- {topping}")

print(type(all_toppings))

burger['toppings'][0]
all_toppings[0]

player = {
    'health': 100,
    'level': 5,
    'hardcore': True
}

HEALTH_KEY = 'health_points'
CLASS_KEY = 'class'


player[HEALTH_KEY] = 50
player[HEALTH_KEY] -= 5
player[HEALTH_KEY] = player[HEALTH_KEY] - 5

player['hardcore'] = False

player['hardcore'] = 500

print(player.get(CLASS_KEY, 'Unknown'))
# print(player['class'])

player[CLASS_KEY] = "Herbalist"

print(player[CLASS_KEY])
print(player.get(CLASS_KEY, 'Unknown'))

if HEALTH_KEY in player:
    print("Player has health")

player.pop(HEALTH_KEY)

if HEALTH_KEY in player:
    print("Player has health")
else:
    print("Player has no health key")


football_teams = {
    'PSG': {
        'player_count': 20,
        'wins': 0,
        'coach': "Dude McDuderson"
    },
    'Chelsea': {
        'player_count': 25,
        'wins': 10,
        'coach': "Rod Coachington"
    }
}

print(football_teams['Chelsea']['player_count'])
print(football_teams['PSG'])
pprint(football_teams)

car = {
    'brand': 'Mega Car',
    'engine': {
        'horse_power': 0,
        'brand': 'brand',
        'timing_belt': {
            'wear': 0,
            'last_service': {
                'time': '',
                'mechanic': 'mechanic'
            }
        }
    }
}

print("i want 'single quotes' in my string")

print('i want \'single quotes\' in my string')