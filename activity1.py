import math

def calculate_values(num):
    sqrt = math.sqrt(num)
    log = math.log(num)
    exp = math.exp(num)
    return sqrt, log, exp

num = float(input("Enter a number: "))
sqrt_val, log_val, exp_val = calculate_values(num)

print(f"For number {num}:")
print(f"Square root: {sqrt_val:.4f}")
print(f"Natural log: {log_val:.4f}")
print(f"Exponential: {exp_val:.4f}")