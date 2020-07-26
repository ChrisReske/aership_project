import standard_cubic_weight
import horsepower

"""
   Main()
"""

standard_air_weight = standard_cubic_weight.get_standard_weight()
aership_horsepower = horsepower.calculate_horsepower(200, 2, 5, 50)
print( "aership_hp: " + str( aership_horsepower) )

def calculate_total_weight_of_air_and_gas( 
    percentage_filled_total_volume, 
    lift_per_unit_volume, standard_air_weight):
    """
   Problem 1
   Find the volume and horsepower of a rigid airship to carry a military load of 15,000 lbs.
   at 60 knots (101.3 ft. / sec.). for 60 hours, 85% of the total volume being filled with helium
   lifting .064 lb./ft.**3 (94 % pure) in the standard atmosphere.

   Since the hull is specified in the condition of the problem to be 85% full of gas, 
   the weight of the gas is 85% D multiplied by the difference between the weight of air and
   the lift of gas per unit volume, and divided by the weight of air per unit volume. The total
   weight of air and gas is therefore ...
"""

    # Entire equation
    #total_air_weight =  ( (100 - percentage_filled_total_volume) / 100.0 ) + \
    #                    ( ( percentage_filled_total_volume * ( standard_air_weight - lift_per_unit_volume ) )\
    #                   / standard_air_weight )

    ttaw_equation_01 = ( (100 - percentage_filled_total_volume) / 100.0 ) 
    ttaw_tmp_result_02 =( ( percentage_filled_total_volume / 100.0 ) * standard_air_weight )
    ttaw_tmp_result_03 = ( ( percentage_filled_total_volume / 100.0 ) * ( lift_per_unit_volume ) * ( -1.0 ) )
    # Using results from first binomial block for second block (division)
    ttaw_tmp_result_04 = ttaw_tmp_result_02 / standard_air_weight
    ttaw_tmp_result_05 = ttaw_tmp_result_03 / standard_air_weight
    total_air_weight = ttaw_equation_01 + ttaw_tmp_result_04 + ttaw_tmp_result_05
    return round(total_air_weight, 5)

my_ttaw = calculate_total_weight_of_air_and_gas( 85.0, 0.064, standard_air_weight )
print("Total weight of air and gas is: ", my_ttaw )

def compute_auxilliary_weight(total_air_weight, 
                              fixed_weights_power = 0.30, 
                              fixed_weights_ballast_and_crew = 0.055):
    """
    From existing data, the fixed weights exclusive of power plant, 
    power cars, and fuel system equal -.3D, and the crew, 
    stores and ballast amount to .055 D. 
    There remains for power plant, fuel, and military load
    """
    return round(1 - total_air_weight - fixed_weights_power - fixed_weights_ballast_and_crew, 5)

my_auxilliary_weight = compute_auxilliary_weight(my_ttaw)
print( "Weight for power plant, fuel and military load is: ", my_auxilliary_weight )