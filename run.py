# run.py

import sys
from solver.cube import Cube
from solver.solve import CFOPSolver
from solver.utils import parse_scramble, pretty_print_alg

if __name__ == '__main__':
    scramble = parse_scramble(sys.argv[1])  # e.g. python run.py "R U2 R' U …"
    cube = Cube()
    # scramble it
    for mv in scramble:
        cube.apply_move(mv)

    solver = CFOPSolver(cube)
    solution = solver.solve()
    print("Solution:", pretty_print_alg(solution))
