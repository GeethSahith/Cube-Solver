# moves.py
from cube import Cube

def rotate_U(cube: Cube):
    c = cube.faces
    cube.rotate_face_clockwise(0)
    # Edges affected: F[0], R[0], B[0], L[0]
    temp = c[2][0][:]
    c[2][0] = c[1][0][:]
    c[1][0] = c[5][0][:]
    c[5][0] = c[4][0][:]
    c[4][0] = temp

def rotate_U_prime(cube: Cube):
    for _ in range(3): rotate_U(cube)

def rotate_U2(cube: Cube):
    for _ in range(2): rotate_U(cube)


def rotate_R(cube: Cube):
    c = cube.faces
    cube.rotate_face_clockwise(1)
    temp = [c[0][i][2] for i in range(3)]
    for i in range(3):
        c[0][i][2] = c[2][i][2]
        c[2][i][2] = c[3][2 - i][2]
        c[3][2 - i][2] = c[5][2 - i][0]
        c[5][2 - i][0] = temp[i]

def rotate_R_prime(cube: Cube):
    for _ in range(3): rotate_R(cube)

def rotate_R2(cube: Cube):
    for _ in range(2): rotate_R(cube)


def rotate_F(cube: Cube):
    c = cube.faces
    cube.rotate_face_clockwise(2)
    temp = c[0][2][:]
    for i in range(3):
        c[0][2][i] = c[4][2 - i][2]
        c[4][2 - i][2] = c[3][0][2 - i]
        c[3][0][2 - i] = c[1][i][0]
        c[1][i][0] = temp[i]

def rotate_F_prime(cube: Cube):
    for _ in range(3): rotate_F(cube)

def rotate_F2(cube: Cube):
    for _ in range(2): rotate_F(cube)

def rotate_L(cube: Cube):
    c = cube.faces
    cube.rotate_face_clockwise(4)  # Left face index = 4
    temp = [c[0][i][0] for i in range(3)]  # Left column of U

    for i in range(3):
        c[0][i][0] = c[5][2 - i][2]       
        c[5][2 - i][2] = c[3][i][0]       
        c[3][i][0] = c[2][i][0]           
        c[2][i][0] = temp[i]

def rotate_L_prime(cube: Cube):
    for _ in range(3): rotate_L(cube)

def rotate_L2(cube: Cube):
    for _ in range(2): rotate_L(cube)

def rotate_D(cube: Cube):
    c = cube.faces
    cube.rotate_face_clockwise(3)  # Down face index = 3
    temp = c[2][2][:]  # Bottom row of Front

    c[2][2] = c[4][2][:]
    c[4][2] = c[5][2][:]
    c[5][2] = c[1][2][:]
    c[1][2] = temp
def rotate_D_prime(cube: Cube):
    for _ in range(3): rotate_D(cube)

def rotate_D2(cube: Cube):
    for _ in range(2): rotate_D(cube)

def rotate_B(cube: Cube):
    c = cube.faces
    cube.rotate_face_clockwise(5)  # Back face index = 5
    temp = c[0][0][:]  # Top row of U

    for i in range(3):
        c[0][0][i] = c[1][i][2]           # U ← R
        c[1][i][2] = c[3][2][2 - i]       # R ← D
        c[3][2][2 - i] = c[4][2 - i][0]   # D ← L
        c[4][2 - i][0] = temp[i]          # L ← saved U

def rotate_B_prime(cube: Cube):
    for _ in range(3): rotate_B(cube)

def rotate_B2(cube: Cube):
    for _ in range(2): rotate_B(cube)


# Notation mapping
MOVE_FUNCTIONS = {
    "U": rotate_U,
    "U'": rotate_U_prime,
    "U2": rotate_U2,

    "R": rotate_R,
    "R'": rotate_R_prime,
    "R2": rotate_R2,

    "F": rotate_F,
    "F'": rotate_F_prime,
    "F2": rotate_F2,

    "L": rotate_L,
    "L'": rotate_L_prime,
    "L2": rotate_L2,

    "D": rotate_D,
    "D'": rotate_D_prime,
    "D2": rotate_D2,

    "B": rotate_B,
    "B'": rotate_B_prime,
    "B2": rotate_B2,
    
}
