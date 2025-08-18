import argparse
import sys

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Generate Sudoku puzzles PDF with specified number of clues.",
            formatter_class=argparse.RawTextHelpFormatter,
            epilog="""
Examples:
  python sudoku.py -config 20:40 -config 30:35 --use-symmetry
  python sudoku.py -config 10:17 -output sudoku_puzzles.pdf --gen-answers
        """
        )
        self._add_arguments()

    def _add_arguments(self):
        # Puzzle count and clues in format "20:40" (count:clues)
        self.parser.add_argument(
            '-config', 
            action='append', 
            help='Puzzle count and clues in format "20:40" (count:clues).\n'
                 'You can specify multiple configurations with different counts and clue levels.',
            required=True
        )

        # Output PDF file name
        self.parser.add_argument(
            '-output', 
            help="Name of the output PDF file (e.g., sudoku_puzzles.pdf).", 
            required=True
        )

        # Generate answers
        self.parser.add_argument(
            '--gen-answers', 
            help="Generate answers in a separate PDF.",
            action='store_true'
        )

        # Use symmetry in puzzle generation
        self.parser.add_argument(
            '--use-symmetry', 
            help="Enable symmetry in puzzle generation (for professional-grade puzzles).", 
            action='store_true'
        )

        # Check if no arguments are provided
        if len(sys.argv) == 1:
            self.parser.print_help(sys.stderr)
            sys.exit(1)

    # Parse the command line arguments
    def parse(self):
        return self.parser.parse_args()
