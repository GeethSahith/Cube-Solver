# Rubik's Cube CFOP Solver

## About the Project
This is a Python-based Rubik's Cube solver that uses the CFOP method (Cross, F2L, OLL, PLL). CFOP is one of the most widely used methods for solving a Rubik's Cube efficiently, and this project automates each step to solve a scrambled cube.

## What It Does
- **Cross:** Solves the cross on the bottom face.
- **F2L:** Completes the first two layers by detecting and solving specific cases.
- **OLL:** Orients all stickers on the top face to face upwards.
- **PLL:** Permutes the corners and edges of the top layer to finish the cube.
- **Visualization:** Displays the cube's state in a 2D unfolded format for easy debugging.
- **Scrambling:** Mixes up the cube with random moves for testing.

## How It Works
The project is divided into several files:
### Solver Files
- **base.py:** The is the core file that represents the cube and handles movements, rotations, and states.
- **cross.py:** Contains logic for solving the cross on the bottom face.
- **f2l.py:** Handles the first two layers by solving corner-edge pairs.
- **oll.py:** Implements algorithms to orient the last layer.
- **pll.py:** Implements algorithms to permute the last layer.
- **solve.py:** Combines all CFOP steps into a complete solver.

### Utility Files
- **visualizer.py:** Prints a 2D unfolded representation of the cube to the console.

### Main File
- **main.py:** Demonstrates the solver in action by scrambling, solving, and visualizing the cube step-by-step.

## Getting Started
### Prerequisites
Make sure you have Python installed. You’ll also need the `numpy` library.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd rubiks-cfop-solver
   ```
2. Install the required library:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Solver
Run the main.py file to see the solver in action:
```bash
python main.py
```

## Example Workflow
1. The program starts with a solved cube.
2. Scrambles the cube with random moves.
3. Solves the cube step-by-step using CFOP:
   - Cross → F2L → OLL → PLL.
4. Visualizes the cube's state after each step.