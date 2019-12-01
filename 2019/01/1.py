cache = dict()

def fuel_needed(mass):
    if mass <= 0:
        return 0
    if mass in cache:
        return cache[mass]

    needed = max(0, mass // 3 - 2)
    cache[mass] = needed + fuel_needed(needed)
    return cache[mass]

if __name__ == "__main__":
    # tests = [
    #     14,
    #     1969,
    #     100756
    # ]

    # for t in tests:
    #     needed = fuel_needed(t)
    #     print(f'Fuel needed for {t} is {needed}')

    lines = []
    with open('1.in') as f:
        lines = f.readlines()

    fuel = 0
    for line in lines:
        mass = int(line)
        fuel += fuel_needed(mass)
    
    print(f'{fuel} needed')
