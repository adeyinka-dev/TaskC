# main.py
import time
import heapq
from aux import read_dataset, write_result, generate_dataset
import matplotlib.pyplot as plt


def bubble_sort(arr, order="asc"):
    """
    This function sorts a list using the Bubble Sort algorithm.
    'order' determines whether the list is sorted in ascending ('asc') or descending ('desc') order.
    """
    n = len(arr)
    # Make a copy so that the original list is not modified
    sorted_list = arr.copy()
    # Loop over each element in the list
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare adjacent elements based on the desired order
            if order == "asc":
                if sorted_list[j] > sorted_list[j + 1]:
                    # Swap the elements if they are in the wrong order
                    sorted_list[j], sorted_list[j + 1] = (
                        sorted_list[j + 1],
                        sorted_list[j],
                    )
            else:  # descending order
                if sorted_list[j] < sorted_list[j + 1]:
                    sorted_list[j], sorted_list[j + 1] = (
                        sorted_list[j + 1],
                        sorted_list[j],
                    )
    return sorted_list


def binary_heap_sort(arr, order="asc"):
    """
    This function sorts a list using the Binary Heap (Heap Sort) algorithm.
    For ascending order, it uses a min-heap.
    For descending order, it inverts the values to simulate a max-heap.
    """
    data = arr.copy()  # Work on a copy to keep the original unchanged
    if order == "asc":
        heapq.heapify(data)
        sorted_list = [heapq.heappop(data) for i in range(len(data))]
    else:
        # Invert the numbers to simulate a max-heap
        data = [-x for x in data]
        heapq.heapify(data)
        sorted_list = [-heapq.heappop(data) for i in range(len(data))]
    return sorted_list


def experiment(dataset_size, order="asc"):
    """
    This function runs one experiment:
      - It generates a random dataset of the given size.
      - It sorts the dataset using both Bubble Sort and Binary Heap Sort.
      - It measures the time taken for each sorting method (in nanoseconds).
      - It checks that both methods produce the correct sorted list.
    """
    # Generate a random dataset using our auxiliary method
    data = generate_dataset(dataset_size)

    # Measure the time taken by Bubble Sort
    start_bubble = time.perf_counter_ns()
    sorted_bubble = bubble_sort(data, order)
    end_bubble = time.perf_counter_ns()
    bubble_duration = end_bubble - start_bubble  # Time in nanoseconds

    # Measure the time taken by Binary Heap Sort
    start_heap = time.perf_counter_ns()
    sorted_heap = binary_heap_sort(data, order)
    end_heap = time.perf_counter_ns()
    heap_duration = end_heap - start_heap  # Time in nanoseconds

    # Verify that both sorting methods give the same result
    if order == "asc":
        correct = sorted(data)
    else:
        correct = sorted(data, reverse=True)

    if sorted_bubble != correct:
        print("Error: Bubble sort did not sort correctly!")
    if sorted_heap != correct:
        print("Error: Binary heap sort did not sort correctly!")

    # Print out the results of the experiment
    print(f"Dataset Size: {dataset_size}")
    print(f"Bubble Sort Time: {bubble_duration} ns")
    print(f"Binary Heap Sort Time: {heap_duration} ns")
    print("-------------------------------")

    # Return the durations for further processing
    return bubble_duration, heap_duration


def run_experiment_for_size(dataset_size, runs=3, order="asc"):
    """
    This function runs the experiment multiple times for a specific dataset size.
    It computes the average runtime for both sorting algorithms.
    """
    bubble_times = []
    heap_times = []
    for i in range(runs):
        print(f"Running experiment {i+1} for dataset size {dataset_size}")
        bubble_time, heap_time = experiment(dataset_size, order)
        bubble_times.append(bubble_time)
        heap_times.append(heap_time)

    # Calculate the average times (nanoseconds)
    avg_bubble = sum(bubble_times) / runs
    avg_heap = sum(heap_times) / runs
    print(f"Average Bubble Sort Time for size {dataset_size}: {avg_bubble} ns")
    print(f"Average Binary Heap Sort Time for size {dataset_size}: {avg_heap} ns")
    print("========================================")

    return avg_bubble, avg_heap


def run_all_experiments(runs=3, order="asc"):
    """
    This function runs experiments on multiple dataset sizes and collects the average runtimes.
    The results are stored in a table and written to a CSV file.
    """
    # List of dataset sizes as mentuoned in the assignment
    dataset_sizes = [1000, 5000, 15000, 20000, 25000, 30000, 35000, 40000]
    # Create a results table with headers
    results = [
        ["Dataset Size", "Avg Bubble Sort Time (ns)", "Avg Binary Heap Sort Time (ns)"]
    ]
    avg_bubble_list = []
    avg_heap_list = []

    # Run experiments for each dataset size
    for size in dataset_sizes:
        print(f"Running experiments for dataset size: {size}")
        avg_bubble, avg_heap = run_experiment_for_size(size, runs, order)
        results.append([size, avg_bubble, avg_heap])
        avg_bubble_list.append(avg_bubble)
        avg_heap_list.append(avg_heap)

    # Save the results to a CSV file using our auxiliary function
    write_result(results)

    return dataset_sizes, avg_bubble_list, avg_heap_list


def plot_results(dataset_sizes, avg_bubble_list, avg_heap_list):
    """
    This function plots the average runtime results as a line graph.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(dataset_sizes, avg_bubble_list, marker="o", label="Bubble Sort")
    plt.plot(dataset_sizes, avg_heap_list, marker="o", label="Binary Heap Sort")
    plt.xlabel("Dataset Size")
    plt.ylabel("Average Runtime (ns)")
    plt.title("Comparison of Sorting Algorithm Efficiency")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # Run all experiments and collect the results
    dataset_sizes, avg_bubble_list, avg_heap_list = run_all_experiments(
        runs=3, order="asc"
    )
    # Plot the experimental results
    plot_results(dataset_sizes, avg_bubble_list, avg_heap_list)


if __name__ == "__main__":
    main()
