from solver.base import Cube
from utils.visualizer import visualize_cube
from solver.solve import solve_cross, solve_f2l, solve_oll, solve_pll

def main():
    # 1. Create a new, solved cube
    my_cube = Cube.default()
    print("--- Initial Solved State ---")
    visualize_cube(my_cube)

    # 2. Scramble the cube with a few moves
    print("Applied a scramble: R U F'")
    my_cube.run_algorithm("R U F'")
    visualize_cube(my_cube)

    # 3. Test with a full stage solve
    scrambled_cube = Cube.default()
    scrambled_cube.mix_up(25)
    print("A Fully Scrambled Cube")
    visualize_cube(scrambled_cube)

    print("SOLVING THE CUBE FROM HERE")
    solve_cross(scrambled_cube)
    
    print("CUBE AFTER SOLVING CROSS")
    visualize_cube(scrambled_cube)

    print("CUBE AFTER SOLVING F2L(FIRST 2 LAYERS)")
    solve_f2l(scrambled_cube)
    visualize_cube(scrambled_cube)

    print("CUBE AFTER SOLVING OLL)")
    solve_oll(scrambled_cube)
    visualize_cube(scrambled_cube)

    print("CUBE AFTER SOLVING PLL")
    solve_pll(scrambled_cube)
    visualize_cube(scrambled_cube)

if __name__ == "__main__":
    main()