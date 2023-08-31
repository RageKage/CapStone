city_state = [("Seattle", "WA"), ("Portland", "OR"), ("San Francisco", "CA"), ("Los Angeles", "CA")]

first_city_state = city_state[0]

print(first_city_state[0])
print(first_city_state[1])


city, state = first_city_state

print(city)
print(state)

for i in range(len(city_state)):
    city, state = city_state[i]
    print(f"{city} is in {state}")
    

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km


# distance = get_distance()

miles, km = get_distance()

print(miles, km)