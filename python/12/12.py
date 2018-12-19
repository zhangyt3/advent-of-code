import sys


# Make plant 0 map to index 500.
# This wastes space, but will probably work and make things a lot simpler.
RULE_WIDTH = 2
OFFSET = 5000  # plant 0 -> index 500; plant i -> index i + 500
SIZE = 10000


def simulate(plants, rules):
    next_gen = [False for _ in range(len(plants))]

    # For each plant, check if it will be alive next round
    for i in range(RULE_WIDTH, len(plants) - RULE_WIDTH):
        section = tuple(plants[i - RULE_WIDTH:i + RULE_WIDTH + 1])
        for condition, res in rules.items():
            if section == condition:
                next_gen[i] = res
                break
    
    return next_gen


def sum_plants(plants):
    # Sum plant numbers of pots with a plant
    summed = 0
    for i, plant in enumerate(plants):
        if plant:
            plant_num = i - OFFSET
            summed += plant_num
    return summed


if __name__ == '__main__':
    src = [False for _ in range(SIZE)]
    
    # Initialize plants
    start = input().split(" ")[2].strip()
    for i in range(len(start)):
        if start[i] == "#":
            src[i + OFFSET] = True
    # Make copy for part 2
    plants = [x for x in src]
    
    # Record the rules
    input()  # Read empty line
    rules = dict()
    for line in sys.stdin:
        condition, result = line.split(" => ")
        condition = tuple([True if x == "#" else False for x in condition])
        result = (result.strip() == "#")
        rules[condition] = result

    # Simulate...
    GENERATIONS = 20
    for gen in range(GENERATIONS):
        plants = simulate(plants, rules)
    summed = sum_plants(plants)
    print("Sum of all plant numbers for pots with plants: {}".format(summed))
        
    # Part 2: after generation 102, each subsequent generation adds 67 to the sum
    plants = [x for x in src]
    # summed = sum_plants(plants)
    # print("Gen {} Sum: {}".format(0, summed))
    # for gen in range(1000):
    #     plants = simulate(plants, rules)
    #     prev = summed
    #     summed = sum_plants(plants)
    #     print("Gen {} Sum: {}".format(gen + 1, summed))
    #     diff = summed - prev
    #     print("Diff: {}".format(diff))
    #     print()

    for gen in range(102):
        plants = simulate(plants, rules)
    summed = sum_plants(plants)
    summed += (50000000000 - 102) * 67       
    print("After 50000000000 Generations: {}".format(summed))
    


    