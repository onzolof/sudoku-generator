#!/bin/bash

# number of exports
NUM_EXPORTS_EASY=3
NUM_EXPORTS_MEDIUM=3
NUM_EXPORTS_HARD=3
NUM_EXPORTS_EXPERT=3
NUM_EXPORTS_INSANE=3

# output folder
OUTPUT_DIR="./puzzles"
mkdir -p "$OUTPUT_DIR"   # create if not exists

# export CSV format puzzles (all difficulties)
python sudoku.py -config ${NUM_EXPORTS_EASY}:40 -output ${OUTPUT_DIR}/40_easy_puzzles.csv --format csv
python sudoku.py -config ${NUM_EXPORTS_MEDIUM}:35 -output ${OUTPUT_DIR}/35_medium_puzzles.csv --format csv
python sudoku.py -config ${NUM_EXPORTS_HARD}:30 -output ${OUTPUT_DIR}/30_hard_puzzles.csv --format csv
python sudoku.py -config ${NUM_EXPORTS_EXPERT}:25 -output ${OUTPUT_DIR}/25_expert_puzzles.csv --format csv
python sudoku.py -config ${NUM_EXPORTS_INSANE}:20 -output ${OUTPUT_DIR}/20_insane_puzzles.csv --format csv
