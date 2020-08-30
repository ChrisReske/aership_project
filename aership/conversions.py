
def convert_knots_to_ft_sec( knots ):
    """
       Converts knots to feet in seconds

       PARAMETERS

       knots:   decimal
                knots as decimal. If no knots are passed, function returns None
    """
    if knots == None:
        return None

    return knots * 1.6878
