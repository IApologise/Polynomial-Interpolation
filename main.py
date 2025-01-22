# Welcome message
print("\nPolynomial Interpolation\n")

# Options
precision = 0
while True:
    print("Choose the maximum amount of decimals:")
    try:
        precision = int(input(">>> "))
        break
    except ValueError or precision < 0:
        print("\nError! The input must be a positive integer")
print()  # Blank space

# Setup
points: list[float, float] = []  # point: [x, y]
while True:

    # Gathering data from user
    print(f"Write the coordinates of the point number {len(points) + 1}.")
    print("Leave empty and press ENTER if you are done.")
    coordinates = input("x,y >>> ").replace(" ", "")  # Input + reformat

    # Checking if done
    if not coordinates:
        print()  # Blank space
        break

    coordinates = coordinates.split(",")  # Splitting

    # Checking if inputs are numbers
    try:
        for dimension in range(len(coordinates)):
            coordinates[dimension] = float(coordinates[dimension])  # Attempting conversion to float
    except ValueError:
        print('\nError, invalid input. Here is a valid example: "13, 5".')
        continue

    # Checking if 2D
    if len(coordinates) != 2:
        print("\nToo many inputs were given. Only 2 are needed, X and Y.")
        continue

    points.append(coordinates)  # Registering coordinates
    print()  # Blank space

# Printing out points
print(f"All the points:")
for point in range(len(points)):
    print(f"- Point {point + 1}: {tuple(points[point])}")
print()  # Blank space

# Setting up equations
equations: list[list[float]] = []  # equation: [values]

for point in points:
    new_equation = [-point[1]]
    for degree in range(len(points)):
        new_equation.append(point[0] ** degree)
    equations.append(new_equation)

# Finding relations
relations: list[int, list[float]] = []  # relation: [values]
for equation in equations:

    # Substituting
    for relation in range(len(relations)):
        static = relation + 1
        multiplier = equation[static]
        for variable in range(len(equation)):
            equation[variable] += relations[relation][variable] * multiplier
        equation[static] = 0.0

    # Creating a new relation
    new_relation = []
    static = len(relations) + 1
    try:
        for value in equation:
            new_relation.append(-value / equation[static])
    except ZeroDivisionError:
        continue
    new_relation[static] = 0.0
    relations.append(new_relation)

# Solving variables
solutions = []
for equation in range(1, len(equations) + 1):
    equation *= -1

    # Substituting
    for solution in range(len(solutions)):
        equations[equation][0] += solutions[solution] * equations[equation][-(solution + 1)]

    # Solving
    try:
        equations[equation][0] /= -equations[equation][equation]
    except ZeroDivisionError:
        print("Such polynomial function does not exist.")
        print("Press ENTER to leave.")
        input(">>> ")
        exit()
    solutions.append(equations[equation][0])

# Printing out the result
result = "f(x) = "
for solution in range(len(solutions)):
    if solutions[solution] != 0:

        # Numbers
        if solutions[solution] != 1:
            result += str(round(solutions[solution], precision))

        # Exponents
        if solution < len(solutions) - 1:
            result += "x"  # X
            if solution < len(solutions) - 2:
                result += f"^{len(solutions) - (solution + 1)}"
        else:
            continue

        # Operators
        result += f" + "

result = result.replace("+ -", "- ")  # Finishing touches
print(result)  # Print

# Exiting the program
print("Press ENTER to leave.")
input(">>> ")
exit()
