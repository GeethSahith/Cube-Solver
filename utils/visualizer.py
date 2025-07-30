from solver.base import Cube, Color, Face

# Map Color enums to single character strings for display
COLOR_MAP = {
    Color.WHITE: "W",
    Color.YELLOW: "Y",
    Color.BLUE: "B",
    Color.GREEN: "G",
    Color.RED: "R",
    Color.ORANGE: "O",
}

def visualize_cube(cube: Cube):
    """
    Prints a 2D unfolded representation of the cube to the console.
    
    Layout:
          Top
    Left  Front Right Back
          Bottom
    """
    
    # Helper function to convert a face's pieces to colored strings
    def get_face_lines(face: Face) -> list[str]:
        lines = []
        for i in range(0, 9, 3):
            row = face.pieces[i:i+3]
            lines.append(" ".join(COLOR_MAP[color] for color in row))
        return lines

    # Get pre-formatted lines for each face
    top_lines = get_face_lines(cube.top)
    bottom_lines = get_face_lines(cube.bottom)
    front_lines = get_face_lines(cube.front)
    back_lines = get_face_lines(cube.back)
    left_lines = get_face_lines(cube.left)
    right_lines = get_face_lines(cube.right)

    # Print Top face (padded)
    print("\n")
    for line in top_lines:
        print(f"      {line}")
    print("-" * 23)

    # Print Middle faces (Left, Front, Right, Back)
    for i in range(3):
        print(f"{left_lines[i]} | {front_lines[i]} | {right_lines[i]} | {back_lines[i]}")
    print("-" * 23)

    # Print Bottom face (padded)
    for line in bottom_lines:
        print(f"      {line}")
    print("\n")