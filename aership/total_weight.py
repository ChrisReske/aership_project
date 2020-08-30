import standard_cubic_weight

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
