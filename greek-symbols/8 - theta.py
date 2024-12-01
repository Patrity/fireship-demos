import math

def calculate_angle(opposite, adjacent):
    θ = math.atan2(opposite, adjacent)
    return θ * (180 / math.pi)

tower_height = 173
distance_from_tower = 100
θ = calculate_angle(tower_height, distance_from_tower)

print(f"{θ:.0f}")