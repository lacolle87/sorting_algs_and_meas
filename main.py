import time
from random import randint
from abc import ABC, abstractmethod


class DataGenerator:
    def __init__(self, low=0, high=100, rng=20):
        self._data = None
        self.low = low
        self.high = high
        self.rng = rng

    def generate(self):
        self._data = [randint(self.low, self.high) for _ in range(self.rng)]

    @property
    def data(self):
        return self._data

    def __repr__(self):
        return f"DataGenerator(low={self.low}, high={self.high}, range={self.rng})"


class Sort(ABC):
    def __init__(self):
        self._data = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, list):
            raise TypeError("Data must be a list")
        if not all(isinstance(item, (int, float)) for item in value):
            raise TypeError("Data must be a list of numbers")
        self._data = value

    @abstractmethod
    def sort(self):
        pass

    def __repr__(self):
        return f"data={self._data}"


class BubbleSort(Sort):
    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]


class InsertionSort(Sort):
    def sort(self):
        n = len(self.data)
        for i in range(1, n):
            key_item = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key_item:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key_item


class SelectionSort(Sort):
    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]


class MergeSort(Sort):
    @staticmethod
    def merge(left, right):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    def sort(self):
        if len(self.data) <= 1:
            return self.data

        mid = len(self.data) // 2
        left_half = self.data[:mid]
        right_half = self.data[mid:]

        left_sorted = MergeSort()
        left_sorted.data = left_half
        right_sorted = MergeSort()
        right_sorted.data = right_half

        left_sorted.sort()
        right_sorted.sort()

        self.data = self.merge(left_sorted.data, right_sorted.data)


class QuickSort(Sort):
    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1

        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]

        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1

    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quicksort(low, pi - 1)
            self.quicksort(pi + 1, high)

    def sort(self):
        if len(self.data) <= 1:
            return self.data
        self.quicksort(0, len(self.data) - 1)


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    return wrapper


@measure_time
def test_sorting(sc, data):
    sorter = sc()
    sorter.data = data.copy()
    sorter.sort()
    print(f"{sc.__name__} sorted data")


if __name__ == "__main__":
    data_generator = DataGenerator(0, 2000, 20000)
    data_generator.generate()

    print("Starting sorting measurements")

    sort_classes = [BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort]

    for sort_class in sort_classes:
        test_sorting(sort_class, data_generator.data)
