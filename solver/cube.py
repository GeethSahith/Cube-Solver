# cube.py
from typing import List
import random

class Cube:
    def __init__(self):
        # 6 faces, each is a 3×3 grid filled with its face color
        self.faces: List[List[List[int]]] = [
            [[i for _ in range(3)] for _ in range(3)]
            for i in range(6)
        ]

    def copy(self) -> 'Cube':
        new = Cube()
        new.faces = [[row[:] for row in face] for face in self.faces]
        return new

    def is_solved(self) -> bool:
        # Check that each face is a solid color
        return all(
            all(cell == face[0][0] for row in face for cell in row)
            for face in self.faces
        )

    def rotate_face_clockwise(self, face: int):
        # 90° CW rotation of a 3×3 matrix
        self.faces[face] = [
            [self.faces[face][2 - j][i] for j in range(3)]
            for i in range(3)
        ]

    def rotate_face_counterclockwise(self, face: int):
        # 90° CCW rotation
        self.faces[face] = [
            [self.faces[face][j][2 - i] for j in range(3)]
            for i in range(3)
        ]

    def apply_move(self, move: str):
        from moves import MOVE_FUNCTIONS
        if move not in MOVE_FUNCTIONS:
            raise ValueError(f"Invalid move: {move}")
        MOVE_FUNCTIONS[move](self)

    def apply_alg(self, alg: str):
        for mv in alg.strip().split():
            self.apply_move(mv)

    def scramble(self, num_moves: int = 20) -> List[str]:
        MOVE_SET = ["U", "U'", "U2", "D", "D'", "D2",
                    "F", "F'", "F2", "B", "B'", "B2",
                    "L", "L'", "L2", "R", "R'", "R2"]
        seq = random.choices(MOVE_SET, k=num_moves)
        self.apply_alg(" ".join(seq))
        return seq

    def print_cube(self):
        face_names = ['U', 'R', 'F', 'D', 'L', 'B']
        for i, face in enumerate(self.faces):
            print(f"{face_names[i]} face:")
            for row in face:
                print("  ", row)
