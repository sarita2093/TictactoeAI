import copy

def is_a_valid_move(board, coords):
    return board[coords[0]][coords[1]] is None

def render(board):
    rows = []
    for y in range(0, 3):
        row = []
        for x in range(0, 3):
            row.append(board[x][y])
        rows.append(row)

    row_num = 0
    print '  0 1 2 '
    print '  ------'
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += sq
        print "%d|%s|" % (row_num, ' '.join(output_row))
        row_num += 1
    print '  ------'

def get_all_line_co_ords():
    cols = []
    for x in range(0, 3):
        col = []
        for y in range(0, 3):
            col.append((x, y))
        cols.append(col)

    rows = []
    for y in range(0, 3):
        row = []
        for x in range(0, 3):
            row.append((x, y))
        rows.append(row)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return cols + rows + diagonals

def get_winner(board):
    all_line_co_ords = get_all_line_co_ords()

    for line in all_line_co_ords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None

def make_move(board, move_coords, player):
    board_copy = copy.deepcopy(board);
    if board_copy[move_coords[0]][move_coords[1]] is not None:
        raise Exception("Illegal move!")
    board_copy[move_coords[0]][move_coords[1]] = player
    return board_copy



def is_board_full(board):
    for row in board:
        for col in row:
            if col is None:
                return False
    return True

def get_opposite_player(player):
    return 'X' if player is 'O' else 'O'
