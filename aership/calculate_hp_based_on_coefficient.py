import total_weight

def calculate_hp_based_on_coefficient( speed_per_sec ):
    """
       Calculates horsepower based on coefficient K. 
       K is a measure of the overall propulsive efficiency of an
       airship, including both the resistance of the ship and the 
       propeller efficiency.

       PARAMETERS

       speed_per_sec:               decimal
                                    Projected speed of the airship in seconds.
       
       K:                           decimal
                                    A non-dimensional coefficient depending upon the propeller efficiency
                                    and the design of the hull and its appendages. If not indicated otherwise
                                    the default value is 63.5. The value is based on data of airships
                                    and first mentioned in Burgess. Airship Design, 1927. p.14

       total_weight_air_and_gas:    decimal
                                    The total weight of air and gas in the projected airship.
       
       density_air_and_gas:         decimal
                                    The density of air and gas. Based on volume and coefficients.
       


    """

