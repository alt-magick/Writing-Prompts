import random
import sys

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

file = sys.argv[1]
prompt = int(sys.argv[2])

print("")
print("Prompts")
print("--------")

for x in range(prompt):
    print(random_line(file))

print("")
