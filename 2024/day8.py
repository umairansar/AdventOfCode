

class Puzzle:
    def __init__(self):
        self.filename = "input_day8.1.txt"
        self.antennae = dict()
        self.combos = dict()
        self.bounds = []
        self.__parse_file()
        self.__get_combos()

    def in_bounds(self, x, y):
        return self.bounds[0][0] <= x <= self.bounds[1][0] and self.bounds[0][1] <= y <= self.bounds[1][1]

    def __parse_file(self):
        lines = open(self.filename).read().splitlines()
        for row, line in enumerate(lines):
            for col, word in enumerate(list(line)): # .split() did not work because no white spaces to separate
                if word != ".":
                    self.antennae[word] = [(row, col)] if self.antennae.get(word) == None else self.antennae[word] + [(row, col)]
        self.bounds.append([0, 0])
        self.bounds.append([len(lines) - 1, len(lines[0]) - 1])

    def __get_combos(self):
        self.combos = dict()
        for key, values in self.antennae.items():
            for a in values:
                for b in values:
                    if a == b:
                        continue
                    if self.combos.get(key) == None:
                        self.combos[key] = [(a, b)] # Can I yield here?
                    else:
                        combo_values = self.combos.get(key)
                        if (a, b) in combo_values or (b, a) in combo_values:
                            continue
                        else:
                            self.combos.get(key).append((a, b)) # Can I yield here?

    def get_combos_yield(self):
        self.combos = dict()
        for key, values in self.antennae.items():
            for a in values:
                for b in values:
                    if a == b:
                        continue
                    if self.combos.get(key) == None:
                        self.combos[key] = [(a, b)] # Can I yield here?
                        yield (a, b)
                    else:
                        combo_values = self.combos.get(key)
                        if (a, b) in combo_values or (b, a) in combo_values:
                            continue
                        else:
                            self.combos.get(key).append((a, b)) # Can I yield here?
                            yield (a, b)

if __name__ == "__main__":
    p = Puzzle()
    print(p.antennae)
    print("___")
    print(p.combos)

    # Non yield solution
    antinodes = set()
    for key, combos in p.combos.items():
        for combo in combos:
            ant1 = combo[0]
            ant2 = combo[1]
            x, y = ant1[0] - ant2[0], ant1[1] - ant2[1]
            node1 = ant1[0] - 2*x, ant1[1] - 2*y
            node2 = ant1[0] + x, ant1[1] + y
            if p.in_bounds(*node1):
                antinodes.add(node1)
            if p.in_bounds(*node2):
                antinodes.add(node2)

    print("Non Yield")
    print(len(antinodes))

    # Yield solution
    p = Puzzle()
    antinodes = set()
    for ant1, ant2 in p.get_combos_yield():
        x, y = ant1[0] - ant2[0], ant1[1] - ant2[1]
        node1 = ant1[0] - 2*x, ant1[1] - 2*y
        node2 = ant1[0] + x, ant1[1] + y
        if p.in_bounds(*node1):
            antinodes.add(node1)
        if p.in_bounds(*node2):
            antinodes.add(node2)

    print("Yield")
    print(len(antinodes))

    # Part 2
    p = Puzzle()
    antinodes = set()
    for ant1, ant2 in p.get_combos_yield():
        x, y = ant1[0] - ant2[0], ant1[1] - ant2[1]

        antinodes.add(ant1)
        antinodes.add(ant2)

        jump = 2
        node1 = ant1[0] - jump*x, ant1[1] - jump*y
        while p.in_bounds(*node1):
            jump += 1
            antinodes.add(node1)
            node1 = ant1[0] - jump*x, ant1[1] - jump*y
        
        jump = 1
        node2 = ant1[0] + jump*x, ant1[1] + jump*y
        while p.in_bounds(*node2):
            jump += 1
            antinodes.add(node2)
            node2 = ant1[0] + jump*x, ant1[1] + jump*y


    print("Part 2")
    print(len(antinodes))


