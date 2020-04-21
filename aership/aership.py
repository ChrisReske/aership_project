"""
   Main(), add classes and/or functions later
"""

def get_standard_cubic_foot_air_weight():
    """
    Returns weight of a cubic foot of air in standard atmosphere in lbs.

    The weight of a cubic foot of air in the standard atmosphere, i.e.
    temperature 60°F , and 29.92 in barometric pressure at sea level
    is 0.07635 lbs
    """
    return 0.07635

# Testing get_standard_cubic_foot_air_weight():
standard_air = get_standard_cubic_foot_air_weight()
print(standard_air)


def calculate_horsepower_considering_speed_and_size( v, p, V, K ):
    """
    Calculates the relation between horsepower speed and size.
    Returns horspower as decimal value.
    The value 550 used in this calculation is the number of
    ft.lbs./sec developed by one Hp.

    Parameters
    -------------

    v : decimal
        Speed in feet feet/seconds

    p : decimal
        Density of the air in slugs/feet ** 3 (1 slug = 32.lbs)

    V : decimal
        air volume of the ship in cubic feet

    K : decimal
        a non-dimensional coefficient depending upon 
        the propeller efficiency and the design of the hull and its appendages.
        `K` is thus a measure of the overall propulsive energy of an airship, 
        including both the resistances of the ship and the propeller efficiency.
    """
    horsepower = ( V ** ( 2/3 ) * p * ( v ** 3 ) / ( 550 * K) )
    return horsepower

# Testing calculate_horsepower_considering_speed_and_size
my_horsepower = calculate_horsepower_considering_speed_and_size(200, 2, 5, 50)
print(my_horsepower)

def calculate_horsepower_using_standard_displacement(displacement, density_of_air, speed, design_coefficient):
    """
    Parameters
    -------------
    D (displacement) : decimal
        The weight of a cubic foot of air in the standard atmosphere, i.e.
        temperature 60°F , and 29.92 in barometric pressure at sea level
        is 0.07635 lbs

    v (speed) : decimal
        Speed in feet feet/seconds

    p (densitiy_of_air) : decimal
        Density of the air in slugs/feet ** 3 (1 slug = 32.lbs)

    K (design_coefficient): decimal
        a non-dimensional coefficient depending upon 
        the propeller efficiency and the design of the hull and its appendages.
        `K` is thus a measure of the overall propulsive energy of an airship, 
        including both the resistances of the ship and the propeller efficiency.
    """
    horsepower =  (( displacement ** 2/3 ) * density_of_air * ( speed ** 3 ) ) / ( 99 * design_coefficient )
    return horsepower

