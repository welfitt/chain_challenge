lines = []

for line in open('chains.txt'):
    lines.append(list(line.rstrip("\n")))

tot_rows = len(lines)
tot_cols = len(lines[0])
chain_lengths = []


def delete_chain(row_p, col_p):
    lines[row_p][col_p] = ""
    result = 1
    for xy_tuple in filter(
            lambda xy: xy[0] in range(tot_rows) and xy[1] in range(tot_cols) and lines[xy[0]][xy[1]] == "#",
            [(row_p + delta[0], col_p + delta[1]) for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]]):
        result += delete_chain(xy_tuple[0], xy_tuple[1])
    return result


for row in range(tot_rows):
    for column in range(tot_cols):
        if lines[row][column] == "#":
            chain_lengths.append(delete_chain(row, column))

print(f"There are {len(chain_lengths)} chains in total.")
print(f"There are {sum(chain_lengths)} chains links in total.")
