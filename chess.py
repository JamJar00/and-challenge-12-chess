def _file_distance(from_file, to_file):
    return abs(ord(from_file) - ord(to_file))


def _row_distance(from_row, to_row):
    return abs(from_row - to_row)


def _is_same_file(from_file, to_file):
    return from_file == to_file


def _is_same_row(from_row, to_row):
    return from_row == to_row


def _is_same_diagonal(from_file, from_row, to_file, to_row):
    return _file_distance(from_file, to_file) == _row_distance(from_row, to_row)


def canMove(piece, from_square, to_square):
    # This function is purely here to convert between Pascal case and camel case in case an automated test is used that doesn't use Python naming conventions!
    return can_move(piece, from_square, to_square)


def can_move(piece, from_square, to_square, colour="White"):
    if from_square == to_square:
        return None

    from_file = from_square[0]
    from_row = int(from_square[1])
    to_file = to_square[0]
    to_row = int(to_square[1])

    if ord(from_file) < ord("A") or ord(from_file) > ord("H") or from_row < 1 or from_row > 8:
        return None
    if ord(to_file) < ord("A") or ord(to_file) > ord("H") or to_row < 1 or to_row > 8:
        return None

    if colour not in ["White", "Black"]:
        return None

    if piece == "Rook":
        return _is_same_file(from_file, to_file) or _is_same_row(from_row, to_row)
    elif piece == "Queen":
        return _is_same_file(from_file, to_file) or _is_same_row(from_row, to_row) or _is_same_diagonal(from_file, from_row, to_file, to_row)
    elif piece == "King":
        return _file_distance(from_file, to_file) <= 1 and _row_distance(from_row, to_row) <= 1
    elif piece == "Bishop":
        return _is_same_diagonal(from_file, from_row, to_file, to_row)
    elif piece == "Knight":
        return (_file_distance(from_file, to_file) == 1 and _row_distance(from_row, to_row) == 2) or (_file_distance(from_file, to_file) == 2 and _row_distance(from_row, to_row) == 1)
    elif piece == "Pawn":
        if colour == 'White':
            return _is_same_file(from_file, to_file) and (to_row - from_row == 1 or (from_row == 2 and to_row - from_row == 2))
        elif colour == 'Black':
            return _is_same_file(from_file, to_file) and (to_row - from_row == -1 or (from_row == 7 and to_row - from_row == -2))
    else:
        return None


def test_can_move():
    assert can_move("Rook", "A8", "D8")
    assert can_move("Rook", "A8", "H8")
    assert not can_move("Rook", "A1", "H8")
    assert can_move("King", "D4", "E5")
    assert can_move("King", "E5", "D4")
    assert not can_move("King", "E6", "D4")
    assert can_move("Bishop", "A7", "G1")
    assert can_move("Bishop", "G7", "A1")
    assert not can_move("Bishop", "G7", "H7")
    assert can_move("Queen", "C4", "C7")
    assert can_move("Queen", "A4", "G4")
    assert can_move("Queen", "A4", "C6")
    assert not can_move("Queen", "C4", "D6")
    assert not can_move("Queen", "C4", "A3")
    assert can_move("Knight", "C4", "A3")
    assert can_move("Knight", "C4", "A5")
    assert can_move("Knight", "A5", "C4")
    assert not can_move("Knight", "A5", "D4")
    assert not can_move("Knight", "A5", "C5")
    assert not can_move("Knight", "A5", "A7")
    assert can_move("Pawn", "C4", "C5")
    assert can_move("Pawn", "C2", "C4")
    assert not can_move("Pawn", "C2", "D3")
    assert not can_move("Pawn", "C3", "C2")
    assert can_move("Pawn", "C7", "C6", "Black")
    assert can_move("Pawn", "C7", "C5", "Black")
    assert not can_move("Pawn", "C7", "D6", "Black")
    assert not can_move("Pawn", "C5", "C6", "Black")

    assert can_move("Pawn", "E5", "E5") is None
    assert can_move("Pawn", "@1", "C1") is None
    assert can_move("Pawn", "C0", "C1") is None
    assert can_move("Pawn", "I1", "C1") is None
    assert can_move("Pawn", "C9", "C1") is None
    assert can_move("Pawn", "C1", "@1") is None
    assert can_move("Pawn", "C1", "C0") is None
    assert can_move("Pawn", "C1", "I1") is None
    assert can_move("Pawn", "C1", "C9") is None
    assert can_move("Roook", "C1", "C2") is None
