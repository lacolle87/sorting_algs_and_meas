# Sorting Algorithms Comparison and Measurement

This repository showcases educational implementations of common sorting algorithms along with time measurement utilities.

## Overview

The script demonstrates how different sorting algorithms perform on randomly generated datasets. The main purpose is to provide an educational tool to understand how various sorting algorithms (like Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, and Quick Sort) work and how their performance varies based on the input size.

## Features

1. **Sorting Algorithms**: 
   - **Bubble Sort**: Simple and inefficient.
   - **Insertion Sort**: Efficient for small datasets.
   - **Selection Sort**: Finds the minimum element and moves it to its position.
   - **Merge Sort**: Divide and conquer, recursive splitting.
   - **Quick Sort**: Efficient with a good pivot selection.

2. **Data Generation**: 
   - Random datasets of integers ranging from a low value to a high value with a specified range.

3. **Performance Measurement**:
   - Time taken by each sorting algorithm is measured to show efficiency differences.

## Requirements

- Python 3.x

## Script Explanation

- **DataGenerator Class**: Generates random datasets.
- **Sort Class (Abstract)**: Defines structure for all sorting algorithms.
- **Concrete Sorting Classes**:
  - `BubbleSort`
  - `InsertionSort`
  - `SelectionSort`
  - `MergeSort`
  - `QuickSort`
- **measure_time Decorator**: Measures the execution time of the sorting methods.
- **test_sorting Function**: Runs and tests each sorting algorithm with the generated dataset.
