# test_moves.py
from cube import Cube

def test():
    cube = Cube()
    print("Initial solved cube:")
    cube.print_cube()

    scramble = "R U R' U'"
    print("\nApplying scramble:", scramble)
    cube.apply_alg(scramble)
    cube.print_cube()

    reverse = "U R U' R'"
    print("\nApplying reverse:", reverse)
    cube.apply_alg(reverse)
    cube.print_cube()

    if cube.is_solved():
        print("\n✅ Cube returned to solved state!")
    else:
        print("\n❌ Cube is NOT solved!")

if __name__ == "__main__":
    test()
