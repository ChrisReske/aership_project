import standard_cubic_weight
import horsepower
import total_weight

"""
   Main()
"""

standard_air_weight = standard_cubic_weight.get_standard_weight()
aership_horsepower = horsepower.calculate_horsepower(200, 2, 5, 50)
print( "aership_hp: " + str( aership_horsepower) )
# Calculate total weight of air and gas
my_ttaw = total_weight.calculate_total_weight_of_air_and_gas( 85.0, 0.064, standard_air_weight )
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