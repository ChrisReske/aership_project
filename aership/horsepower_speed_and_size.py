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
