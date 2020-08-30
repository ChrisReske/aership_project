import standard_cubic_weight
import horsepower
import total_weight
import auxiliary_weight
import weight_per_horsepower
import calculate_volume_and_hp

"""
   Main()
"""

# Compute standard air weight and horspower (based on volume and displacement) 
standard_air_weight = standard_cubic_weight.get_standard_weight()
aership_horsepower = horsepower.calculate_horsepower(200, 2, 5, 50)
print( "aership_hp: " + str( aership_horsepower) )

# Compute total weight of air and gas (ttaw)
ttaw = total_weight.calculate_total_weight_of_air_and_gas( 85.0, 0.064, standard_air_weight )
print("Total weight of air and gas is: ", ttaw )

# Compute auxiliary weight( power plant, fuel, military or commercial load)
auxilliary_weight = auxiliary_weight.compute_auxilliary_weight(ttaw)
print( "Auxiliary weight is: ", auxilliary_weight )

# Compute weight per horsepower
weight_hp = weight_per_horsepower.calculate_weight_per_horsepower(8, 0.6)
print("Weight for power plant and fuel system is: "  + str( weight_hp ) )

test = calculate_volume_and_hp.calculate_vol_and_hp(15000.0) 