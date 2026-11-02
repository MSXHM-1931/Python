import time


total = 50
for current in range(total + 1):
	percent = current * 100 // total
	bar = "+" * current + "-" * (total - current)
	print("\r[{0}] {1:3d}%".format(bar, percent), end="", flush=True)
	time.sleep(0.1)

print()
