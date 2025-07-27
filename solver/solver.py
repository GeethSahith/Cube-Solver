# solver/solver.py

from solver.cube import Cube
from solver.cross import solve_cross
from solver.f2l   import solve_f2l
from solver.oll   import solve_oll
from solver.pll   import solve_pll

class CFOPSolver:
    def __init__(self, cube: Cube):
        self.cube = cube
        self.moves: List[str] = []

    def solve(self) -> List[str]:
        # Phases in order
        self.moves += solve_cross(self.cube)
        self.moves += solve_f2l(self.cube)
        self.moves += solve_oll(self.cube)
        self.moves += solve_pll(self.cube)
        return self.moves
