def compute_auxilliary_weight(total_air_weight, 
                              fixed_weights_power = 0.30, 
                              fixed_weights_bc = 0.055, 
                              rounding = 5):
    """
    Returns the auxiliary weight for power plant, fuel and military or
    commercial load as decimal

    Parameters
    ------------------

    total_air_weight:       decimal
                            Weight of air and the lift of gas per unit volume, 
                            divided by the weight of air per unit volume (cf. corresponding
                            module and functions).
    fixed_weights_power:    decimal (default: 0.30)
                            Constant for fixed weights exclusive of power plant, 
                            power cars, and fuel system based on existing data.
                            If no parameter is provided, default is used.
    fixed_weights_bc:       decimal (default: 0.055)
                            Refers to the fixed weight for ballast (b) and crew (c).
                            Constant based on data and estimates. 
                            If no parameter is provided, default is used.
    rounding:               integer (default: 5)
                            Number of decimals the result should be rounded upon computation.
                            If no integer is provided, default is used.
    """
    return round(1 - total_air_weight - fixed_weights_power - fixed_weights_ballast_and_crew, rounding)
