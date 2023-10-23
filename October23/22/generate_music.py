import chess.pgn

# Define a mapping from chess moves to musical notes (simplified for demonstration)
chess_to_music = {
    "P": "c4", "p": "c5",
    "N": "d4", "n": "d5",
    "B": "e4", "b": "e5",
    "R": "f4", "r": "f5",
    "Q": "g4", "q": "g5",
    "K": "a4", "k": "a5",
}

# Fixed duration for each chess move
move_duration = "4"

# Load the chess game from a PGN file (replace 'your_game.pgn' with the file path)
with open('your_game.pgn') as pgn_file:
    game = chess.pgn.read_game(pgn_file)

# Create a list to store the musical notation
music_notation = []

# Iterate through the chess moves and map them to musical notes with the fixed duration
board = game.board()
for move in game.mainline_moves():
    move_note = chess_to_music.get(board.san(move)[0], "r")  # "r" for a rest
    music_notation.append(f"{move_note}{move_duration}")
    board.push(move)

# Join the musical notation into a LilyPond input
lilypond_content = f"""\\version "2.24.0"
\\header {{
    title = "{game.headers['Event']} - {game.headers['White']} vs {game.headers['Black']}"
}}
\\score {{
    {{
        \\relative c' {{
            \\key c \\major
            \\time 4/4
            {' '.join(music_notation)}
        }}
    }}
    \\layout {{}}
    \\midi {{}}
}}
"""

# Save the LilyPond input file
with open('output_score.ly', 'w') as lilypond_file:
    lilypond_file.write(lilypond_content)

print("LilyPond input file 'output_score.ly' has been created.")
