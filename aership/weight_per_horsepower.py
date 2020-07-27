def calculate_weight_per_horsepower(weight_power_plant_cars, weight_fuel_system):
    hour_per_hp = 60.0
    return weight_power_plant_cars + ( weight_fuel_system *  hour_per_hp)

