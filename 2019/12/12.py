class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]
    
    def update_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

    def calc_energy(self):
        return sum([abs(x) for x in self.pos]) * sum([abs(x) for x in self.vel])
    
    def get_state_string(self):
        return ' '.join([str(x) for x in self.pos]) + ' ' + ' '.join([str(x) for x in self.vel])

def hash_state(moons):
    state = ""
    for moon in moons:
        state += moon.get_state_string()
        state += "|"
    return state

def simulate_round(positions):
    # Calculate gravity
    gravity = [[0, 0, 0] for _ in range(len(positions))]
    for axis in range(3):
        for i in range(len(positions)):
            for j in range(i, len(positions)):
                # Find diff between i, j for this axis
                if positions[i].pos[axis] < positions[j].pos[axis]:
                    gravity[i][axis] += 1
                    gravity[j][axis] -= 1
                elif positions[i].pos[axis] > positions[j].pos[axis]:
                    gravity[i][axis] -= 1
                    gravity[j][axis] += 1
    
    # Update velocity
    for i, grav in enumerate(gravity):
        positions[i].vel[0] += grav[0]
        positions[i].vel[1] += grav[1]
        positions[i].vel[2] += grav[2]

    # Update position
    for moon in positions:
        moon.update_position()

    return positions

def simulate(positions, rounds):
    states = set()
    for r in range(rounds):
        positions = simulate_round(positions) 
        state = hash_state(positions)
        if state in states:
            print(f'Rounds needed to reach previous state: {r+1}')
            break

        states.add(state)
    
    # energy = 0
    # for moon in positions:
    #     energy += moon.calc_energy()
    # print(f'After {rounds} rounds the total energy is {energy}')

if __name__ == '__main__':
    positions = [
        Moon([-14, -4, -11]),
        Moon([-9, 6, -7]),
        Moon([4, 1, 4]),
        Moon([2, -14, -9])
    ]

    simulate(positions, 1000000)

