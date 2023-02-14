''' Define an EXPECTED_BAKE_TIME constant that returns how many minutes the lasagna
should bake in the oven. According to your cookbook, the Lasagna should be in the
oven for 40 minutes:'''

EXPECTED_BAKE_TIME = 40

''' Implement the bake_time_remaining() function that takes the actual minutes the 
lasagna has been in the oven as an argument and returns how many minutes the lasagna 
still needs to bake based on the EXPECTED_BAKE_TIME.'''

def bake_time_remaining(actual_minutes):
    bake_time = EXPECTED_BAKE_TIME - actual_minutes
    return bake_time

# print(bake_time_remaining(10))

''' Implement the preparation_time_in_minutes() function that takes the number of layers you
 want to add to the lasagna as an argument and returns how many minutes you would spend making 
 them. Assume each layer takes 2 minutes to prepare.'''

def preparation_time_in_minutes(number_layers):
    return number_layers * 2
# print(preparation_time_in_minutes(6))

''' Implement the elapsed_time_in_minutes() function that has two parameters: number_of_layers 
(the number of layers added to the lasagna) and elapsed_bake_time (the number of minutes the 
lasagna has been baking in the oven). This function should return the total number of minutes 
you've been cooking, or the sum of your preparation time and the time the lasagna has already 
spent baking in the oven.'''

"""
   This function takes two numbers representing the number of layers & the time already spent 
   baking and calculates the total elapsed minutes spent cooking the lasagna.
"""

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    layers = preparation_time_in_minutes(number_of_layers)
    return layers + elapsed_bake_time

print(elapsed_time_in_minutes(3,20))