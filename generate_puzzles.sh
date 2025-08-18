#!/bin/bash

# number of exports
NUM_EXPORTS=3

# output folder
OUTPUT_DIR="./puzzles"
mkdir -p "$OUTPUT_DIR"   # create if not exists

# export easy puzzles
python sudoku.py -config ${NUM_EXPORTS}:40 -output ${OUTPUT_DIR}/easy_puzzles.pdf --gen-answers

# export medium puzzles
python sudoku.py -config ${NUM_EXPORTS}:35 -output ${OUTPUT_DIR}/medium_puzzles.pdf --gen-answers

# export hard puzzles
python sudoku.py -config ${NUM_EXPORTS}:30 -output ${OUTPUT_DIR}/hard_puzzles.pdf --gen-answers

# export expert puzzles
python sudoku.py -config ${NUM_EXPORTS}:25 -output ${OUTPUT_DIR}/expert_puzzles.pdf --gen-answers

# export insane puzzles
python sudoku.py -config ${NUM_EXPORTS}:20 -output ${OUTPUT_DIR}/insane_puzzles.pdf --gen-answers
