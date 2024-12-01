current_target = 150
delta = 10

def adjust_target_weight(current_target, delta, α):
    return current_target - α * delta

new_target = adjust_target_weight(current_target, delta, 0.5)

print(new_target)