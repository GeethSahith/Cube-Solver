# solver/pll.py

from solver.cube import Cube

PLL_ALGS = {
    # e.g. "Ua": "R U' R U R U R U' R' U' R2",
    # ... 21 cases
}

def solve_pll(cube: Cube) -> List[str]:
    sig = compute_pll_signature(cube)
    alg = PLL_ALGS.get(sig)
    if not alg:
        raise ValueError("Unknown PLL case")
    cube.apply_alg(alg)
    return alg.split()
