# cross.py
from cube import Cube
from typing import List
from random import choice

WHITE = 0

# When the white edge is in UF (0,2,1), dropping into D uses:
INSERT_MOVES = {
    2: ['F2'],  # Front  → drop F→D
    1: ['R2'],  # Right
    5: ['B2'],  # Back
    4: ['L2'],  # Left
}

# The four U‑edge slots and which side they belong to
U_FACE_EDGES = {
    (0,2,1): 2,   # UF → Front
    (0,1,2): 1,   # UR → Right
    (0,0,1): 5,   # UB → Back
    (0,1,0): 4,   # UL → Left
}

# All 12 edge‑positions on a cube
ALL_EDGES = [
    # U layer
    (0,0,1), (0,1,2), (0,2,1), (0,1,0),
    # D layer
    (3,0,1), (3,1,2), (3,2,1), (3,1,0),
    # F layer
    (2,0,1), (2,1,2), (2,2,1), (2,1,0),
    # R layer
    (1,0,1), (1,1,2), (1,2,1), (1,1,0),
    # B layer
    (5,0,1), (5,1,2), (5,2,1), (5,1,0),
    # L layer
    (4,0,1), (4,1,2), (4,2,1), (4,1,0),
]

def bring_edge_to_U(cube: Cube, f:int, r:int, c:int, sol:List[str]):
    """
    Hard-coded moves to bring the edge at (f,r,c) so that its white sticker
    ends up in the UF location (0,2,1).
    """
    # 1) If it’s already in UF, nothing to do
    if (f,r,c)==(0,2,1):
        return

    # D layer → double‐turn
    if f==3:
        if (r,c)==(0,1): mv='F2'
        elif (r,c)==(1,2): mv='R2'
        elif (r,c)==(2,1): mv='B2'
        elif (r,c)==(1,0): mv='L2'
        else: return
        cube.apply_alg(mv); sol.append(mv)
        return

    # F layer
    if f==2:
        if (r,c)==(0,1): mv="F"
        elif (r,c)==(2,1): mv="F'"
        elif (r,c)==(1,2): mv="U'"
        elif (r,c)==(1,0): mv="U"
        else: return
        cube.apply_alg(mv); sol.append(mv)
        return

    # R layer
    if f==1:
        if (r,c)==(0,1): mv="R"
        elif (r,c)==(2,1): mv="R'"
        elif (r,c)==(1,2): mv="U'"
        elif (r,c)==(1,0): mv="U"
        else: return
        cube.apply_alg(mv); sol.append(mv)
        return

    # B layer
    if f==5:
        if (r,c)==(0,1): mv="B"
        elif (r,c)==(2,1): mv="B'"
        elif (r,c)==(1,2): mv="U'"
        elif (r,c)==(1,0): mv="U"
        else: return
        cube.apply_alg(mv); sol.append(mv)
        return

    # L layer
    if f==4:
        if (r,c)==(0,1): mv="L'"
        elif (r,c)==(2,1): mv="L"
        elif (r,c)==(1,2): mv="U'"
        elif (r,c)==(1,0): mv="U"
        else: return
        cube.apply_alg(mv); sol.append(mv)
        return

def rotate_U_to_match(cube:Cube, side_face:int, sol:List[str]):
    """
    With the white sticker now at UF=(0,2,1), spin U until
    the second-color of that edge matches side_face's center.
    """
    target = cube.faces[side_face][1][1]
    for _ in range(4):
        if cube.faces[0][2][1]==WHITE and cube.faces[side_face][0][1]==target:
            return
        cube.apply_alg("U"); sol.append("U")

def solve_cross(cube: Cube) -> List[str]:
    sol: List[str] = []
    # 1) locate *every* white-edge
    for f,r,c in ALL_EDGES:
        if cube.faces[f][r][c] != WHITE:
            continue

        # 2) bring that white up into UF
        bring_edge_to_U(cube, f, r, c, sol)

        # 3) detect which side it's now paired with
        for (u_pos, side) in U_FACE_EDGES.items():
            if cube.faces[u_pos[0]][u_pos[1]][u_pos[2]]==WHITE:
                # 4) spin U to align
                rotate_U_to_match(cube, side, sol)
                # 5) drop it down
                mv = INSERT_MOVES[side]
                cube.apply_alg(" ".join(mv))
                sol += mv
                break

    return sol

def check_cross(cube:Cube)->bool:
    # all four edges should now be on D and aligned
    for (u_pos, side) in U_FACE_EDGES.items():
        # after F2/R2/etc the white is gone from U
        if cube.faces[u_pos[0]][u_pos[1]][u_pos[2]]==WHITE:
            return False
        # and that side center still matches its facelet
        if cube.faces[side][0][1]!=cube.faces[side][1][1]:
            return False
    return True

if __name__=="__main__":
    cube = Cube()
    moves = ["U","U'","U2","D","D'","D2",
             "F","F'","F2","B","B'","B2",
             "L","L'","L2","R","R'","R2"]
    scr = " ".join(choice(moves) for _ in range(20))
    print("Scramble:", scr)
    cube.apply_alg(scr)
    print("Before cross:", cube.is_solved())
    sol = solve_cross(cube)
    print("Cross moves:", sol)
    print("Cross OK?", check_cross(cube))
    cube.print_cube()
