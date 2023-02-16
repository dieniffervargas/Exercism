''' Instructions
Your friend Chandler plans to visit exotic countries all around the world.
Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed
by currency exchanges during his trip - and he wants you to make a currency calculator for him.
Here are his specifications for the app:
'''

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    num = budget // denomination
    return int(num)

def get_number_of_bills(budget, denomination):
    num = budget // denomination
    n = num * denomination
    result = budget - n
    return float(result)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_dec = (spread/100)+1
    new_rate = (exchange_rate * spread_dec)
    result = budget / new_rate
    resultado = (result // denomination) * denomination
    return (int(resultado))
