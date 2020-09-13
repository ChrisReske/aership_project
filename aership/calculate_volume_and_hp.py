import total_weight
import standard_cubic_weight
import auxiliary_weight
import weight_per_horsepower

def calculate_vol_and_hp( 
    load, 
    speed_in_knots=60.0, 
    operating_hours=60.0, 
    fill_volume=100, 
    lift_capacity=0.064, 
    power_plant = 1.0, 
    weight_fuel_system=1.0):
    """
    Calculates volume and horsepower of a rigid airship taking into account a user-defined
    military or commercial load, a user-defined speed in knots, user-defined hours for operating
    on the speed defined in this function as well as the total volume the airship is supposed to be
    filled with.
    Returns volume in ft. cubed

    Parameters
    --------------
    load:               decimal
                        User-defined military or commercial load in lbs, the airship is expected to carry.

    speed_in_knots:     decimal
                        User-defined speed in knots the airships is suppose to operate.
                        If not indicated otherwise, the default speed is 60 knots.

    operating_hours:    decimal
                        User-defined hours for which the speed defined in parameter 'speed' should be maintained.
                        If not specificed, a default of 60 hourse will be used
    
    fill_volume:        integer
                        The total volume being fille for the calculation.
                        Use integers to denote the percentage, e.g. 85 for 85% of the airship volume being filled.
                        If not indicated, the default of 100 = 100% will be used

    lift_capacity:      decimal
                        Lift of lb per cubed feet depending on gas used and its purity in the standard atmosphere.
                        If not indicated otherwise, a default of 0.064 lb/ft**3 using 94 % pure helium is used.

    The book author just eliminated Hp from 1 by the formula 2.
    15000+44(.39D2/3)=.357D

    Do arthitmatic and rearrange:

    .357D−17.16D2/3=42000

    Divide by the .357 to get

    D−48.067 ** D2/3 =42016.8

    Then round off because he used a slide rule not a calculator.


    """

    # First compute total weight of air and gas

    air_weight = standard_cubic_weight.get_standard_weight()

    if air_weight == 0:
        print("Standard air weight is null, please check your code")
        return None

    # I calculate air and gas
    tw_air_and_gas = total_weight.calculate_total_weight_of_air_and_gas(85.0, 0.064, air_weight)
    
    if tw_air_and_gas == 0:
        return None
        print("Total weight of air and gas is 0, please check your code")
    
    # Calculate total air weight and auxiliary weight
    aux_weight = auxiliary_weight.compute_auxilliary_weight(tw_air_and_gas)
    tmp = aux_weight
   
    if aux_weight == 0:
        return None
        print("Auxiliary weight is 0, please check your code")

    # Calculate combined weight for fuel and fuel system
    fuel_and_fuel_system = weight_per_horsepower.calculate_weight_per_horsepower(
        power_plant, weight_fuel_system) 

    if fuel_and_fuel_system == 0:
        return None
        print("Weight for fuel and fuel system is 0, please check your code.")

    # Combine previous results with military load
    