# solver/utils.py

def parse_scramble(line: str) -> List[str]:
    # "R U2 R' ..." → ["R","U2","R'"]
    return line.strip().split()

def load_scrambles(path: str) -> List[List[str]]:
    with open(path) as f:
        return [parse_scramble(l) for l in f if l.strip()]

def pretty_print_alg(alg: List[str]) -> str:
    return ' '.join(alg)
