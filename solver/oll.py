# solver/oll.py

from solver.cube import Cube

# Preload a dict: pattern_signature → algorithm string
OLL_ALGS = {
    # e.g. signature for “dot” case: "011010110" → "R U2 R2 F R F' U2 R' F R F'"
}

def solve_oll(cube: Cube) -> List[str]:
    sig = compute_oll_signature(cube)
    alg = OLL_ALGS.get(sig)
    if not alg:
        raise ValueError("Unknown OLL case")
    cube.apply_alg(alg)
    return alg.split()
