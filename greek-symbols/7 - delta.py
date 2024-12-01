def calculate_change(old_value, new_value):
    return new_value - old_value

old_temp = 75
new_temp = 70
change = calculate_change(old_temp, new_temp)

print(f"Δ: {change}")