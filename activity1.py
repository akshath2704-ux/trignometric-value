import math
def calculate_trigonometric_values(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    sin_value = math.sin(angle_in_radians)
    cos_value = math.cos(angle_in_radians)
    tan_value = math.tan(angle_in_radians)
    return sin_value, cos_value, tan_value
angle = float(input("Enter an angle in degrees: "))
sin_val, cos_val, tan_val = calculate_trigonometric_values(angle)

print(f"For angle {angle}°:")
print(f"sin({angle}) = {sin_val:.4f}")
print(f"cos({angle}) = {cos_val:.4f}")
print(f"tan({angle}) = {tan_val:.4f}")