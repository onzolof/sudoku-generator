import csv
import numpy as np

class CSVGenerator:
    def __init__(self):
        pass

    def _sudoku_to_string(self, sudoku):
        """Convert a 9x9 sudoku grid to a single string (left to right, top to bottom)"""
        return ''.join(str(sudoku[i, j]) for i in range(9) for j in range(9))

    def _count_clues(self, puzzle):
        """Count the number of non-zero values (clues) in the puzzle"""
        return np.count_nonzero(puzzle)

    def generate_puzzles_csv(self, puzzles, output_file):
        """Generate a CSV file with puzzles and solutions"""
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(['number_of_clues', 'puzzle', 'solution'])
            
            # Write each puzzle
            for puzzle, solution in puzzles:
                clues = self._count_clues(puzzle)
                puzzle_str = self._sudoku_to_string(puzzle)
                solution_str = self._sudoku_to_string(solution)
                
                writer.writerow([clues, puzzle_str, solution_str])
        
        print(f"CSV saved as: {output_file}")
        print(f"Generated {len(puzzles)} puzzles in CSV format")
