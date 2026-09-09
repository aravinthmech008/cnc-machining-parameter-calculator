import math

print("=== CNC Machining Parameter Calculator ===")

V = float(input("Enter cutting speed (m/min): "))
D = float(input("Enter tool diameter (mm): "))
Z = int(input("Enter number of teeth: "))
f = float(input("Enter feed per tooth (mm/tooth): "))

# Calculate spindle speed
N = (1000 * V) / (math.pi * D)

# Calculate feed rate
F = N * Z * f

print("\n--- Results ---")
print(f"Spindle Speed: {N:.2f} RPM")
print(f"Feed Rate: {F:.2f} mm/min")
