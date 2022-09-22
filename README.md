# Chess
The `can_move(piece, from, to, colour)` function can be called to validate a move. `True` means the move is allowed, `False` means the move is not allowed, and `None` means your move is invalid (e.g. off the board).

Unit tests can be run using pytest. If you're not a Python/pipenv user, then the following commands will run the unit tests:
```
# Install pipenv to manage dependencies nicely
pip install pipenv

# Run tests, making sure the pytest dependency is installed in a virtual environment for cleanliness
pipenv run pytest chess.py
```
