import random
import die

# File to write the generated tasks to
OUTPUT_FILE = "../benchmark/tasks/rotate_die/values.csv"

# Number of tasks to generate
NUM_TASKS = 30

# Minimum and maximum number of steps in a task
MIN_STEPS = 1
MAX_STEPS = 5

# Die face options
FACES = ['front', 'back', 'top', 'bottom', 'left', 'right']

# Rotation degree options
DEGREES = [-90, -180, -270, 90, 180, 270]

# Rotation direction options
DIRECTIONS = ['clockwise', 'counterclockwise']


# Function to generate a random die rotation task of random number of steps (between 1 and n)
def generate_task():
    # Create a new random die
    d = die.Die()

    # Get initial state of the die
    initial_die_state = str(d)

    # Generate a random number of steps for the task
    num_steps = random.randint(MIN_STEPS, MAX_STEPS)

    # Generate the steps for the task
    steps = []
    for _ in range(num_steps):
        face = random.choice(FACES)
        degrees = random.choice(DEGREES)
        direction = random.choice(DIRECTIONS)
        steps.append((face, degrees, direction))

    for step in steps:
        d.rotate(step[0], step[1], step[2])
    
    solution = str(d)


    return initial_die_state, steps, solution

# Generate and print the tasks (human readable format)
# for i in range(NUM_TASKS):
#     initial_state, steps, solution = generate_task()
#     print(f"Task {i+1}:")
#     print(f"Initial Die State: {initial_state}")
#     print("Steps:")
#     for step in steps:
#         print(f"  Rotate {step[0]} face {step[1]} degrees {step[2]}")
#     print(f"Final Die State: {solution}")
#     print("---------------------------------------------")

# Write the value file headers to the values file
with open(OUTPUT_FILE, "w") as output_file:
    output_file.write("starting_state,transformations,reference\n")  # Write header

# Generate the tasks and write them to the values file
with open(OUTPUT_FILE, "a") as output_file:
    for i in range(NUM_TASKS):
        initial_state, steps, solution = generate_task()
        steps_str = ", ".join([f"rotate {step[0]} face {step[1]} degrees {step[2]}" for step in steps])
        output_file.write(f"\"{{{initial_state}}}\",\"{{{steps_str}}}\",\"{{{solution}}}\"\n")
