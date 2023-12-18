import sys

def has_two_kings(fen):
    """Check if the FEN string has exactly one white king and one black king."""
    return fen.count('K') == 1 and fen.count('k') == 1

def process_file(input_file, output_file):
    """Process the file to keep only lines with FEN strings having two kings."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            fen = line.split('|')[0]  # Assuming FEN string is before the '|'
            if has_two_kings(fen):
                outfile.write(line)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python correct_file.py <input_file> <output_file>')
        sys.exit(1)
    process_file(sys.argv[1], sys.argv[2])
