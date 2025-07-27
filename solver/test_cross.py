from cube import Cube
from cross import solve_cross, check_cross

def test():
    cube = Cube()
    # apply a known cross‐scramble
    cube.apply_alg("F R U R' U' F'")
    print("Before cross:", cube.print_cube())

    sol = solve_cross(cube)
    print("Solution:", sol)
    print("Cross correct?", check_cross(cube))
    cube.print_cube()

if __name__ == "__main__":
    test()
