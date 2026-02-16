import time
import click
from sokoban import Sokoban
from search import astar_search, ucs_search

# THIS FILE IS FOR SOLVING SOKOBAN PUZZLES
#   _____                            _              _
#  |_   _|                          | |            | |
#    | |  _ __ ___  _ __   ___  _ __| |_ __ _ _ __ | |_
#    | | | '_ ` _ \| '_ \ / _ \| '__| __/ _` | '_ \| __|
#   _| |_| | | | | | |_) | (_) | |  | || (_| | | | | |_
#  |_____|_| |_| |_| .__/ \___/|_|   \__\__,_|_| |_|\__|
#                  | |
#                  |_|
# YOUR NAME: Daijiro Tanimura
# YOUR WPI ID: 997073434
# FINISH THE ASSIGNMENT IN `sokoban.py` AND `search.py`
# YOU MAY MODIFY THIS FILE BUT THE COMMAND LINE INTERFACE MUST REMAIN UNCHANGED
# REQUIRED PACKAGES: click


@click.command()
@click.option(
    "--input",
    "input_file",
    required=True,
    type=click.Path(exists=True),
    help="Path to the input file containing the Sokoban level.",
)
@click.option(
    "--output",
    "output_file",
    required=True,
    help="Path to the output file to write the solution.",
)
@click.option(
    "--mode",
    type=click.Choice(['astar', 'ucs']),
    default='astar',
    help="Search algorithm to use ('astar' or 'ucs')."
)
def main(input_file, output_file, mode):
    board = []
    with open(input_file, "r") as f:
        for l in f:
            if l:
                board.append(l)

    # board is a list of strings containing rows in the input file, you need to parse it into your state representation.
    problem = Sokoban(board)
    start_time = time.time()
    if mode == 'ucs':
        print(f"Running UCS on {input_file}...")
        result = ucs_search(problem)
    else:
        print(f"Running A* on {input_file}...")
        result = astar_search(problem)
        
    print("Search completed in {:.2f} seconds.".format(time.time() - start_time))

    if not result:
        print("No solution found.")
        soln = []
    else:
        # Depending on your Sokoban formulation, you may need to convert your solution format to fulfill the output requirement.
        soln = result.solution()
        print("Solution found with {} moves.".format(len(soln)))
    print("".join(soln))
    with open(output_file, "w") as f:
        f.write("".join(soln))


if __name__ == "__main__":
    main()
