# Sorting Algorithms Performance Analysis

This project implements and compares the performance of various sorting algorithms across different array sizes and data conditions.

## Implemented Algorithms

1. **Bubble Sort** - O(n²)  
2. **Selection Sort** - O(n²)  
3. **Insertion Sort** - O(n²)  
4. **Merge Sort** - O(n log n)  
5. **Quick Sort** - O(n log n)  

## Installation

Install required dependencies:
```bash
pip install -r requirements.txt
```
## Usage
Run experiments from the command line with the following syntax:
```bash
python run_experiments.py -a <algorithm_ids> -s <array_sizes> -e <experiment_type> -r <repetitions>
```

### Command-Line Arguments

- `-a, --algorithms`: Algorithm IDs to compare (space-separated)
  - `1` = Bubble Sort
  - `2` = Selection Sort
  - `3` = Insertion Sort
  - `4` = Merge Sort
  - `5` = Quick Sort

- `-s, --sizes`: Array sizes to test (space-separated integers)

- `-e, --experiment`: Experiment type
  - `0` = Experiment with random data (unsorted)
  - `1` = Nearly sorted with 5% noise
  - `2` = Nearly sorted with 20% noise

- `-r, --repetitions`: Number of repetitions for each test 

### Examples

**Example 1**: Compare Insertion, Merge, and Quick Sort on arrays of sizes 100, 500, and 3000 with random data, 20 repetitions:
```bash
python run_experiments.py -a 3 4 5 -s 100 500 3000 -e 0 -r 20
```

**Example 2**: Compare all algorithms on nearly-sorted data (5% noise):
```bash
python run_experiments.py -a 1 2 3 4 5 -s 100 500 1000 5000 -e 1 -r 10
```

**Example 3**: Compare Bubble, Selection, and Insertion Sort with 20% noise:
```bash
python run_experiments.py -a 1 2 3 -s 100 500 3000 -e 2 -r 15
```

## Output

The program generates:
- Console output showing mean runtime ± standard deviation for each algorithm at each array size
- A plot saved as:
  - `result1.png` for comparative experiments (experiment type 0)
  - `result2.png` for noise experiments (experiment types 1 and 2)

## Project Structure

```
.
├── sorting_algorithms.py   # Implementation of all sorting algorithms
├── run_experiments.py      # Experiment runner with CLI interface
├── requirements.txt        # Python dependencies
└── README.md              # This file-general project explanation 
```

## Experiments

### Comparative Experiment (Type 0)
Tests algorithms on randomly generated arrays to measure performance on unsorted data.

### Noise Experiments (Types 1 and 2)
Tests algorithms on nearly-sorted arrays with controlled amounts of disorder:
- **5% noise**: Randomly swaps 5% of elements in a sorted array
- **20% noise**: Randomly swaps 20% of elements in a sorted array

## Performance Expectations

##Goals: 
Illustrate the difference in growth rate between slower and faster
algorithms, and compare runtime with theortical complexity expectations. . 
