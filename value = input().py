value = input().strip()

if value.startswith("Ce"):
	celsius = float(value[2:])
	fahrenheit = celsius * 9 / 5 + 32
	print(f"Fa{fahrenheit:.2f}")
elif value.startswith("Fa"):
	fahrenheit = float(value[2:])
	celsius = (fahrenheit - 32) * 5 / 9
	print(f"Ce{celsius:.2f}")
