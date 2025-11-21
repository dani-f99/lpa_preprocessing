# Custom function to round numbers upward

def round_up(number):
    num_dec = number
    num_round = round(number)
    
    if num_round < num_dec:
        value = num_round + 1
    else:
        value = num_round
    return value