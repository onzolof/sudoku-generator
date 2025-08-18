#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sudoku Puzzle Generator with multiprocessing support to use all cores
Author: [Ali Alp]
Date: September 2024
Description: Generates Sudoku puzzles with specified number of clues,
and optionally generates an answers PDF with the solution.
Supports parallel processing to utilize all CPU cores for generating puzzles concurrently.
"""

from multiprocessing import Pool, cpu_count
from advanced_sudoku_generator import AdvancedSudokuGenerator
from pdf_generator import PDFGenerator
from argument_parser import ArgumentParser

# Helper function for multiprocessing
def generate_puzzle_task(task):
    min_clues, use_symmetry = task
    generator = AdvancedSudokuGenerator()
    return generator.generate_professional_sudoku(min_clues=min_clues, symmetry=use_symmetry)

# Main Function
def main():
    # Use the ArgumentParser class to parse arguments
    args_parser = ArgumentParser()
    args = args_parser.parse()

    pdf_generator = PDFGenerator()

    # Parse puzzle configurations
    puzzle_configs = []

    # Handle the config to extract count and min_clues
    for config in args.config:
        parts = config.split(':')
        if len(parts) != 2:
            raise ValueError(f"Error: Config must be in format 'count:clues'. You provided: {config}")
        
        count = int(parts[0])
        min_clues = int(parts[1])

        # Validate that min_clues is at least 17
        if min_clues < 17:
            raise ValueError(f"Error: Minimum clues must be at least 17. You provided {min_clues}.")

        puzzle_configs.append({'count': count, 'min_clues': min_clues})

    # Prepare tasks for multiprocessing
    tasks = []
    for config in puzzle_configs:
        for _ in range(config['count']):
            tasks.append((config['min_clues'], args.use_symmetry))

    # Use multiprocessing to generate puzzles in parallel
    num_cores = cpu_count()  # Get the number of CPU cores available
    print(f"Generating puzzles using {num_cores} CPU cores...")

    # Check multiprocessing setup
    print(f"Number of tasks to process: {len(tasks)}")
    with Pool(processes=num_cores) as pool:
        puzzles_generated_flat = pool.map(generate_puzzle_task, tasks)

    # Generate and save puzzle PDFs
    pdf_generator.generate_puzzles_pdf(puzzles_generated_flat, "sudoku_puzzles")
    pdf_generator.save_pdf(args.output)

    # Generate answers PDF if requested
    if args.gen_answers:
        answers_pdf_generator = PDFGenerator()
        answers_pdf_generator.generate_puzzles_pdf(puzzles_generated_flat, "sudoku_puzzles", is_answer=True)
        answers_pdf_generator.save_pdf(args.output.replace('.pdf', '_answers.pdf'))

if __name__ == "__main__":
    main()  # Ensure main() is executed directly to avoid multiprocessing issues
