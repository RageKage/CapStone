""" 
Generate quotes for lawn mowing service.
small lawn = $10
medium lawn = $15
large lawn = $20


add $5 for same-day service
"""

def lawn_quote(size, same_day):
    """ Generate quote for lawn mowing service. """
    if size == "small":
        price = 10
    elif size == "medium":
        price = 15
    elif size == "large":
        price = 20
    else:
        return 
    if same_day:
        price += 5
    return price