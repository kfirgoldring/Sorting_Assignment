from typing import List, Dict, Callable
import numpy as np
import matplotlib.pyplot as plt
import time
import argparse
from sorting_algorithms import insertion_sort, merge_sort, quick_sort, bubble_sort, selection_sort

def comparative_experiment(array_sizes: List[int], num_repetitions: int, algorithms: Dict[str, Callable]) -> None:
    """
    Compare sorting algorithm performance across different array sizes.

    Args:
        array_sizes: List of array sizes to test
        num_repetitions: Number of times to repeat the experiment for each array size
        algorithms: Dictionary mapping algorithm names to their functions
    """

    # Store results for each algorithm
    results = {name: {'means': [], 'stds': []} for name in algorithms.keys()}

    for size in array_sizes:
        print(f"Testing array size: {size}")

        # Store times for each algorithm
        algo_times = {name: [] for name in algorithms.keys()}

        for _ in range(num_repetitions):
            # Generate random array
            test_array = np.random.randint(0, 100000, size=size).tolist()

            # Time each algorithm
            for name, func in algorithms.items():
                test_array_copy = test_array.copy()  # Fresh copy for each algorithm
                start = time.perf_counter()
                func(test_array_copy)
                end = time.perf_counter()
                algo_times[name].append(end - start)  # Time in seconds

        # Calculate statistics for each algorithm
        for name in algorithms.keys():
            mean_time = np.mean(algo_times[name])
            std_time = np.std(algo_times[name])
            results[name]['means'].append(mean_time)
            results[name]['stds'].append(std_time)
            print(f"  {name}: {mean_time:.4f} ± {std_time:.4f} s")

    # Create plot with runtime variability shown as error bars (mean ± std).
    plt.figure(figsize=(10, 6))
    markers = ['o', 's', '^', 'd', 'v']
    for idx, (name, data) in enumerate(results.items()):
        marker = markers[idx % len(markers)]
        plt.errorbar(
            array_sizes,
            data['means'],
            yerr=data['stds'],
            marker=marker,
            label=name,
            linewidth=2,
            capsize=4,
            elinewidth=1
        )

    plt.xlabel('Array Size')
    plt.ylabel('Runtime (s)')
    plt.title('Runtime Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig('result1.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as result1.png")
    plt.close()

def noise_experiment(array_sizes: list, noise_percentage: float, num_repetitions: int, algorithms: dict) -> None:
    """
    Compare sorting algorithm performance on nearly-sorted arrays with varying noise levels.

    Args:
        array_sizes: List of array sizes to test
        noise_percentage: Percentage of elements to randomly swap (0.0 to 1.0)
        num_repetitions: Number of times to repeat the experiment for each array size
        algorithms: Dictionary mapping algorithm names to their functions
    """

    # Store results for each algorithm
    results = {name: {'means': [], 'stds': []} for name in algorithms.keys()}

    for size in array_sizes:
        print(f"Testing array size: {size} with {noise_percentage*100}% noise")

        # Store times for each algorithm
        algo_times = {name: [] for name in algorithms.keys()}

        for _ in range(num_repetitions):
            # Generate sorted array
            test_array = list(range(size))

            # Add noise by randomly swapping elements
            num_swaps = int(size * noise_percentage)
            for _ in range(num_swaps):
                i = np.random.randint(0, size)
                j = np.random.randint(0, size)
                test_array[i], test_array[j] = test_array[j], test_array[i]

            # Time each algorithm
            for name, func in algorithms.items():
                test_array_copy = test_array.copy()  # Fresh copy for each algorithm
                start = time.perf_counter()
                func(test_array_copy)
                end = time.perf_counter()
                algo_times[name].append(end - start)  # Time in seconds

        # Calculate statistics for each algorithm
        for name in algorithms.keys():
            mean_time = np.mean(algo_times[name])
            std_time = np.std(algo_times[name])
            results[name]['means'].append(mean_time)
            results[name]['stds'].append(std_time)
            print(f"  {name}: {mean_time:.4f} ± {std_time:.4f} s")

    # Create plot with runtime variability shown as error bars (mean ± std).
    plt.figure(figsize=(10, 6))
    markers = ['o', 's', '^', 'd', 'v']
    for idx, (name, data) in enumerate(results.items()):
        marker = markers[idx % len(markers)]
        plt.errorbar(
            array_sizes,
            data['means'],
            yerr=data['stds'],
            marker=marker,
            label=name,
            linewidth=2,
            capsize=4,
            elinewidth=1
        )

    plt.xlabel('Array Size')
    plt.ylabel('Runtime (s)')
    plt.title(f'Runtime Comparison with {noise_percentage*100}% Noise')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig('result2.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as result2.png")
    plt.close()


if __name__ == "__main__":
    # Algorithm mapping
    ALGORITHM_MAP = {
        1: ('Bubble Sort', bubble_sort),
        2: ('Selection Sort', selection_sort),
        3: ('Insertion Sort', insertion_sort),
        4: ('Merge Sort', merge_sort),
        5: ('Quick Sort', quick_sort)
    }

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Run sorting algorithm experiments')
    parser.add_argument('-a', '--algorithms', type=int, nargs='+', required=True,
                        help='Algorithm IDs: 1=Bubble, 2=Selection, 3=Insertion, 4=Merge, 5=Quick')
    parser.add_argument('-s', '--sizes', type=int, nargs='+', required=True,
                        help='Array sizes to test')
    parser.add_argument('-e', '--experiment', type=int, required=True,
                        help='Experiment type: 0=Comparative (random), 1=5%% noise, 2=20%% noise')
    parser.add_argument('-r', '--repetitions', type=int, required=True,
                        help='Number of repetitions for each test')

    args = parser.parse_args()

    # Validate array sizes
    if any(size <= 0 for size in args.sizes):
        print("Error: Array sizes must be positive integers")
        exit(1)

    # Validate repetitions
    if args.repetitions <= 0:
        print("Error: Number of repetitions must be a positive integer")
        exit(1)

    # Validate experiment type
    if args.experiment not in [0, 1, 2]:
        print(f"Error: Invalid experiment type {args.experiment}. Must be 0, 1, or 2")
        exit(1)

    # Build selected algorithms dictionary
    selected_algorithms = {}
    for algo_id in args.algorithms:
        if algo_id in ALGORITHM_MAP:
            name, func = ALGORITHM_MAP[algo_id]
            selected_algorithms[name] = func
        else:
            print(f"Warning: Unknown algorithm ID {algo_id}, skipping...")

    if not selected_algorithms:
        print("Error: No valid algorithms selected")
        exit(1)

    # Run the appropriate experiment
    if args.experiment == 0:
        print("Running comparative experiment with random data...")
        comparative_experiment(args.sizes, args.repetitions, selected_algorithms)
    elif args.experiment == 1:
        print("Running noise experiment with 5% noise...")
        noise_experiment(args.sizes, 0.05, args.repetitions, selected_algorithms)
    elif args.experiment == 2:
        print("Running noise experiment with 20% noise...")
        noise_experiment(args.sizes, 0.20, args.repetitions, selected_algorithms)
    else:
        print(f"Error: Unknown experiment type {args.experiment}")
        exit(1)
