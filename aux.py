# aux.py
import random
import csv


def generate_dataset(n):
    """
    This function creates a dataset (a Python list) containing n random integers.
    The integers are between 0 and 10,000.
    """
    dataset = []
    for i in range(n):
        # Generate a random integer and add it to the dataset
        dataset.append(random.randint(0, 10000))
    return dataset


def write_result(result, filename="results.csv"):
    """
    This function writes the result (a list of lists) to a CSV file.
    Each inner list represents one row in the CSV file.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for row in result:
            writer.writerow(row)
    print("Results have been written to", filename)


def read_dataset(file_name):
    """
    This function reads a dataset from a CSV file and returns it as a list of integers.
    It assumes that the CSV file contains numbers separated by commas.
    """
    dataset = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                # Convert each value from string to integer and add to the list
                dataset.append(int(value))
    return dataset
