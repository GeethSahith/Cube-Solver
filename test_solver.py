import pytest
from solver.base import Cube
from solver.cross import check_cross_solved
from solver.f2l import check_f2l_solved
from solver.oll import check_oll_solved
from solver.solve import solve_cross, solve_f2l, solve_oll, solve_pll, check_cube_solved

NUM_SCRAMBLE_TESTS = 50
NUM_CROSS_TESTS = 100
NUM_F2L_TESTS = 100
NUM_OLL_TESTS = 100
NUM_PLL_TESTS = 100
NUM_FULL_SOLVE_TESTS = 50

@pytest.mark.parametrize("run", range(NUM_SCRAMBLE_TESTS))
def test_scramble(run):
    """
    Tests that the mix_up() function actually scrambles a solved cube.
    """
    cube = Cube.default()
    assert check_cube_solved(cube), "Cube should start in a solved state"
    cube.mix_up()
    assert not check_cube_solved(cube), "Cube should be scrambled after mix_up()"

@pytest.mark.parametrize("run", range(NUM_FULL_SOLVE_TESTS))
def test_full_solve(run):
    """
    An end-to-end integration test that scrambles a cube and solves it completely.
    """
    cube = Cube.default()
    cube.mix_up()
    cube_string = cube.to_string() # Save state in case of failure

    try:
        # Run the full CFOP solve process
        solve_cross(cube, minimize_moves=False)
        solve_f2l(cube, minimize_moves=False)
        solve_oll(cube)
        solve_pll(cube)
        
        # Final check
        assert check_cube_solved(cube)
    except Exception as e:
        raise Exception(f"Exception on full solve: {e}\nFailed on initial scramble: {cube_string}")

@pytest.mark.parametrize("run", range(NUM_CROSS_TESTS))
def test_cross(run):
    cube = Cube.default()
    cube.mix_up()
    cube_string = cube.to_string()
    try:
        solve_cross(cube)
        assert check_cross_solved(cube)
    except Exception as e:
        raise Exception(f"Exception on cross solve: {e}\nFailed on cube: {cube_string}")

@pytest.mark.parametrize("run", range(NUM_F2L_TESTS))
def test_f2l(run):
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube, minimize_moves=False)
    cube_string = cube.to_string()
    try:
        solve_f2l(cube)
        assert check_f2l_solved(cube)
    except Exception as e:
        raise Exception(f"Exception on F2L solve: {e}\nFailed on cube: {cube_string}")

@pytest.mark.parametrize("run", range(NUM_OLL_TESTS))
def test_oll(run):
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube, minimize_moves=False)
    solve_f2l(cube, minimize_moves=False)
    cube_string = cube.to_string()
    try:
        solve_oll(cube)
        assert check_oll_solved(cube)
    except Exception as e:
        raise Exception(f"Exception on OLL solve: {e}\nFailed on cube: {cube_string}")

@pytest.mark.parametrize("run", range(NUM_PLL_TESTS))
def test_pll(run):
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube, minimize_moves=False)
    solve_f2l(cube, minimize_moves=False)
    solve_oll(cube)
    cube_string = cube.to_string()
    try:
        solve_pll(cube)
        assert check_cube_solved(cube)
    except Exception as e:
        raise Exception(f"Exception on PLL solve: {e}\nFailed on cube: {cube_string}")

if __name__ == '__main__':
    print("Running solver tests with pytest...")
    pytest.main(['-v', __file__])