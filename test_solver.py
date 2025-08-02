import pytest
from solver.base import Cube
from solver.cross import check_cross_solved
from solver.f2l import check_f2l_solved
from solver.oll import check_oll_solved
from solver.solve import solve_cross, solve_f2l, solve_oll, solve_pll, check_cube_solved

@pytest.mark.parametrize("run", range(5))
def test_scramble(run):
    """
    Tests that the mix_up() function scrambles a solved cube.
    """
    cube = Cube.default()
    assert check_cube_solved(cube), "Cube should start in a solved state"
    cube.mix_up()
    assert not check_cube_solved(cube), "Cube should be scrambled after mix_up()"

def test_cross_solve():
    """
    Tests solving the cross.
    """
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube)
    assert check_cross_solved(cube), "Cross should be solved"

def test_f2l_solve():
    """
    Tests solving the first two layers (F2L).
    """
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube)
    solve_f2l(cube)
    assert check_f2l_solved(cube), "F2L should be solved"

def test_oll_solve():
    """
    Tests solving the orientation of the last layer (OLL).
    """
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube)
    solve_f2l(cube)
    solve_oll(cube)
    assert check_oll_solved(cube), "OLL should be solved"

def test_pll_solve():
    """
    Tests solving the permutation of the last layer (PLL).
    """
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube)
    solve_f2l(cube)
    solve_oll(cube)
    solve_pll(cube)
    assert check_cube_solved(cube), "Cube should be fully solved"

def test_full_solve():
    """
    Tests the full CFOP solve process.
    """
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube)
    solve_f2l(cube)
    solve_oll(cube)
    solve_pll(cube)
    assert check_cube_solved(cube), "Cube should be fully solved"

def test_cross_failure():
    """
    Tests failure when cross is not solved.
    """
    cube = Cube.default()
    cube.mix_up()
    assert not check_cross_solved(cube), "Cross should not be solved initially"

def test_f2l_failure():
    """
    Tests failure when F2L is not solved.
    """
    cube = Cube.default()
    cube.mix_up()
    solve_cross(cube)
    assert not check_f2l_solved(cube), "F2L should not be solved initially"

if __name__ == '__main__':
    print("Running solver tests with pytest...")
    pytest.main(['-v', __file__])