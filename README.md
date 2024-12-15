# 🪣 Exploring Sorting Algorithms

1. [Report](#report)
	- [Introduction](#introduction)
	- [Methodology](#methodology)
		- [Overview](#overview)
		- [Experimental Setup](#experimental-setup)
		- [Code Design](#code-design)
	- [Results](#results)
		- [Individual Results](#individual-results)
		- [Summative Results](#summative-results)
	- [Discussion](#discussion)
	- [Conclusion](#conclusion)
2. [User Manual](#user-manual)
	- [Running From Source](#running-from-source)

## Report

### Introduction

In Computer Science, Sorting Algorithms are used in arranging the elements of a list into a specific order. Efficiency is a significant component that determines the amount of time it takes for the algorithm to sort a dataset, thus serving as a practical subject of time complexity analysis. 

This project aims to evaluate the performance of three (3) sorting algorithms: Quick Sort, Bubble Sort, and Stupid Sort. By analyzing their time efficiency across varying dataset sizes, this study provides insight into the practical and theoretical implications of algorithm design.

The implementation of the algorithms & the timers were written in python, the datasets used were provided in the [`./static/mp2dataset.txt`](./static//mp2dataset.txt) file, and the trials were recorded in nanoseconds (ns), milliseconds (ms), and seconds (s).

### Methodology

#### Overview

**Quick Sort.** A divide-and-conquer algorithm that selects a pivot and partitions the array into two subarrays, sorting them recursively. Time Complexity in the worst-case scenario is `O(n^2)` and average-case scenario is `O(n log n)`

**Bubble Sort.** A comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order. Time Complexity in the worst-case and average scenario is `O(n^2)`.

**Stupid Sort.** Also known as "*Bogo Sort*", it is an algorithm that iterates on different permutations of a list until it finds a sorted one. The permutation can be generated deterministically or randomly generated/shuffled. The project implements the latter concept. Time Complexity in the worst-case is unbounded and average-case `O(n!)`. 

#### Experimental Setup

**Programming Language:** *Python*

**Datasets:** Sample sizes for Quicksort and Bubble Sort were `1,000`, `5,000`, `10,000`, and `40,000`. Stupid Sort was tested on sample sizes of `5`, `10`, `11`, `12`, `13`, `15`, and `50`.

**Trials:** Each sample size for Quicksort and Bubble Sort was tested `50` times. Stupid Sort was tested only one time per sample size, terminating after two days if unsuccessful.

**Timing:** Recorded in *nanoseconds*, *milliseconds*, and *seconds* using Python’s `time` module. A Time limit of 2 days (48 hours) is set for Stupid Sort in the event it will take too long to run.

#### Code Design

The implementation included separate functions for each algorithms in different files ([`quicksort.py`](./mp2/quicksort.py), [`bubblesort.py`](./mp2/bubblesort.py), and [`stupidsort.py`](./mp2/stupidsort.py)). The main program is found at [`program.py`](./mp2/program.py) which includes the code for recording the duration of the sorting algorithms.

```
.
├── mp2/
│   ├── ...
│   ├── program.py  
│   ├── issorted.py
│   ├── loader.py
│   ├── quicksort.py
│   ├── bubblesort.py
│   └── stupidsort.py
├── outputs/  # raw data for the recorded trials
│   └── ...
└── static/
    └── mp2dataset.txt  # dataset provided
```

### Results

#### Individual Results

The raw recorded time for each trial, sample size, and algorithm are saved in text files found at the [`./outputs/`](./outputs/) folder.

Quick Sort
- [Quick Sort, 1,000 samples, 50 trials](./outputs/quicksort_1000_50.txt)
- [Quick Sort, 5,000 samples, 50 trials](./outputs/quicksort_5000_50.txt)
- [Quick Sort, 10,000 samples, 50 trials](./outputs/quicksort_10000_50.txt)
- [Quick Sort, 40,000 samples, 50 trials](./outputs/quicksort_40000_50.txt)

Bubble Sort
- [Bubble Sort, 1,000 samples, 50 trials](./outputs/bubblesort_1000_50.txt)
- [Bubble Sort, 5,000 samples, 50 trials](./outputs/bubblesort_5000_50.txt)
- [Bubble Sort, 10,000 samples, 50 trials](./outputs/bubblesort_10000_50.txt)
- [Bubble Sort, 40,000 samples, 50 trials](./outputs/bubblesort_40000_50.txt)

Stupid Sort
- [Stupid Sort, 5 samples, 1 trial](./outputs/stupidsort_5_1.txt)
- [Stupid Sort, 10 samples, 1 trial](./outputs/stupidsort_10_1.txt)
- [Stupid Sort, 11 samples, 1 trial](./outputs/stupidsort_11_1.txt)
- [Stupid Sort, 12 samples, 1 trial](./outputs/stupidsort_12_1.txt)
- [Stupid Sort, 13 samples, 1 trial](./outputs/stupidsort_13_1.txt) **[TIMEOUT]**
- [Stupid Sort, 15 samples, 1 trial](./outputs/stupidsort_15_1.txt) **[TIMEOUT]**
- [Stupid Sort, 50 samples, 1 trial](./outputs/stupidsort_50_1.txt) **[TIMEOUT]**

#### Summative Results

| Algorithms | Sample Size | Trials | Average Time |
|------------|-------------|--------|--------------|
| Quick Sort | 1,000 | 50 | 1ms 378,522ns |
| | 5,000 | | 7ms 25,692ns |
| | 10,000 | | 16ms 112,020ns |
| | 40,000 | | 77ms 984,500ns |
| Bubble Sort | 1,000 | 50 | 48ms 539,032ns |
| | 5,000 | | 1s 187ms 200,698ns |
| | 10,000 | | 4s 981ms 708,792ns |
| | 40,000 | | 74s 105ms 993,770ns |
| Stupid Sort | 5 | 1 | 0ns |
| | 10 | | 14s 69ms 797,900ns |
| | 11 | | 20s 83ms 569600ns |
| | 12 | | 1029s 648ms 746400ns |
| | 13 | | 2 days (Timeout) |
| | 15 | | 2 days (Timeout) |
| | 50 | | 2 days (Timeout) |

### Discussion

Quick Sort exhibits high efficiency with increasing sample sizes, scaling in an approximately linear-logarithmic manner with the input size.
For a sample size of `1,000`, Quick Sort completes in `1ms 378,522ns`, and for `40,000`, it scales to `77ms 984,500ns`. This reflects its `O(n log n)` average time complexity. The algorithm scales well with larger datasets effectively.

Bubble Sort performance degrades rapidly as the sample size increases, reflecting its `O(n^2)` average-case time complexity. For a sample size of `1,000` integers, it takes `48ms 539,032ns`, while sorting `40,000` takes `74s 105ms 993,770ns`. While feasible for smaller datasets, Bubble Sort becomes impractical for larger datasets due to its quadratic scaling.
This is evident at a sample size of `40,000`, where the time taken is several orders of magnitude greater than Quick Sort.

Stupid Sort is an intentionally inefficient algorithm, with 
an `O(n!)` average-case time complexity which grows factorially with the sample size. For small inputs such as size 5, it completes in 0ns (negligible time for tiny inputs). By size 12, the time taken escalates to `1029s 648ms 746,400ns` (approximately 17 minutes), indicating exponential growth in runtime.
For sizes 13, 15, and 50, the algorithm is terminated after 2 days (continuous 48 hours), demonstrating its impracticality for any sizable dataset.

| Metric | Quick Sort | Bubble Sort | Stupid Sort |
|--------|------------|-------------|-------------|
| Efficiency | Highly Efficient `O(n log n)` | Poorly Efficient `O(n^2)` | Extremely Inefficient `O(n!)` |
| Scalability | Scales well with large inputs | Struggles with large inputs | Becomes unusable after `>12` inputs |
| Use Case | Practical for real-world data | Suitable for small datasets | For academic purpose only |

### Conclusion

This project illustrates the practical implications of theoretical time complexities. Quick Sort emerges as the most efficient algorithm for large datasets, while Bubble Sort is only practical for small inputs due to its simplicity. Stupid Sort serves as an example of a badly designed algorithm.

## User Manual

### Running from Source

**Recommended**: Install `Python 3.8` using a version manager such as `pyenv` from https://github.com/pyenv/pyenv/ (Unix) or https://github.com/pyenv-win/pyenv-win (Windows).

Alternatively, you can install python packages from https://www.python.org/downloads/.

**Recommended**: After setting up your python installation, install the project's dependencies in a virtual environment. Visit `venv` docs from https://docs.python.org/3/library/venv.html for more information:

```sh
cd <this-project-folder>

python -m venv .venv

# --- UNIX ---
source .venv/bin/activate # bash/zsh
.venv/bin/Activate.ps1 # Powershell

# --- Windows ---
source .venv/Scripts/activate # bash/zsh
.venv\Scripts\activate.bat # Command Prompt
.venv\Scripts\Activate.ps1 # Powershell

pip install -r requirements.txt

python mp2
```