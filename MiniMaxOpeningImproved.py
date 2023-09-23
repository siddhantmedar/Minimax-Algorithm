import argparse
import helper

initial_depth = None
positions_evaluated = None


def maxMin(board, depth):
    global positions_evaluated, initial_depth

    if depth == 0:
        # print("maxMin")
        positions_evaluated += 1

        return helper.staticEstimationOpeningImproved(board), board
    else:
        maxStaticEstimate = float("-inf")
        best_move = None

        for state in helper.GenerateMovesOpening(board):
            staticEstimate, best_board = minMax(state, depth - 1)

            if maxStaticEstimate < staticEstimate:
                maxStaticEstimate = staticEstimate
                best_move = best_board

        if depth != initial_depth:
            best_move = board

        return maxStaticEstimate, best_move


def minMax(board, depth):
    global positions_evaluated, initial_depth

    if depth == 0:
        # print("minMax")
        positions_evaluated += 1
        return helper.staticEstimationOpeningImproved(board), board
    else:
        minStaticEstimate = float("inf")
        best_move = None

        for state in helper.GenerateBlackMovesOpening(board):
            staticEstimate, best_board = maxMin(state, depth - 1)

            if minStaticEstimate > staticEstimate:
                minStaticEstimate = staticEstimate
                best_move = best_board

        if depth != initial_depth:
            best_move = board

        return minStaticEstimate, best_move


def main(input, output, depth):
    with open(input, 'r') as f:
        board = f.read().strip()

    res_staticEstimate, res_board = maxMin(board, depth)

    with open(output, 'w') as f:
        f.write("Input Position: " + board + "\t")
        f.write("Output Position: " + res_board + "\n")
        f.write("Positions evaluated by static estimation: " + str(positions_evaluated) + "\n")
        f.write("MINIMAX estimate: " + str(res_staticEstimate) + "\n")

    f.close()

    print(f"Best move: {res_board}")
    print(f"Number of positions evaluated: {positions_evaluated}")
    print(f"MINIMAX estimate: {res_staticEstimate}")

    # print("Wrote to file! Exit")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input file, Output file and Depth')

    # add arguments for input file, output file, and depth
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    parser.add_argument('--depth', type=int, default=0, help='Depth')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    depth_value = args.depth

    print(f'Input file: {input_file}')
    print(f'Output file: {output_file}')
    print(f'Depth value: {depth_value}')

    initial_depth = args.depth
    positions_evaluated = 0

    main(input_file, output_file, initial_depth)
