📚 Library Management System(task 1)
A robust, modular Library Management System built with Object-Oriented Programming (OOP) principles in Python.

🌟 Key Features
  Encapsulation: Secured data using private attributes and @property decorators.


  Modular Design: Clean separation of concerns with 4 distinct modules.

  Data Validation: Automatic age verification and borrowing limit enforcement.

  Custom ADT: A specialized BookList to handle complex collection operations.

1. System Environment Requirements:

  Operating System: Windows, macOS, or Linux.

  Python Version: Python 3.6 or later is recommended.

  Dependencies: This project only uses the Python standard library; no additional third-party packages are required.

2. File Structure: Please ensure the following four .py files are stored in the same folder for correct module import:

  `book.py`: Defines the `Book` category and its attributes (e.g., book title, author, borrowing status).

  `book_list.py`: Defines the `BookList` abstract data type (ADT), responsible for managing the book collection.

  `member.py`: Defines the `Member` category, handling borrowing and returning logic and member information verification.

  `main.py`: The system's entry point (main program), used to execute demonstration and testing logic.
  ## 📁 Project Structure
  
  .
  ├── main.py          # Entry point of the application
  ├── book.py          # Book class with Encapsulation
  ├── member.py        # Member class with borrowing logic
  └── book_list.py     # ADT for managing book collections'

3. Running Steps

  Follow these steps to start and test the program:

    Open a terminal: Open a terminal or command prompt on your computer.

    Change directory: Use the `cd` command to switch to the folder containing the files mentioned above.

    Executable program


# Task2: Self-study of New Data Structure & Algorithm
**Pre-submission Version** | 2026-03-08
**Course**：COMP2090SEF/8090SEF/S209W Data Structures, Algorithms and Problem Solving
**Parent Repository**：[https://github.com/Joe1029666/COMP2090SEF-.git]
**Scenario Adaptation**：Library Management System （Task1 core project)

## Self-studied Content (Not Covered in Course)
### New Data Structure：Graph- Adjacency List Implementation
- **Type**：Undirected/Directed Graph (support weighted edges)
- **Library Application**：Store **user-book borrowing relationships** (undirected) and **book-book association relationships** (directed) based on borrowing behavior.
### New Algorithm：Dijkstra's Algorithm
- **Core Function**：Find the shortest path from a start node to all other nodes in a weighted graph
- **Library Application**：**Book association recommendation** (the shorter the path, the higher the relevance of the book)

## Core Implementation Files
| File Name               | Core Function | Library Scenario Adaptation |
|-------------------------|---------------|-----------------------------|
| `graph_ds.py`            | Graph ADT (adjacency list) with all core operations | Nodes = User ID/Book ID, Edges = Borrow relationship/association, Weights = Borrow times/relevance |
| `dijkstra_algo.py`       | Dijkstra's algorithm core + scenario function | Implements `book_recommendation()` for library, supports top N relevant book recommendation |

## Run the Code
### Environment
Python  (**no third-party libraries required**, pure Python implementation)
### Run Command
```bash
# Enter Task2 folder
cd Task2_SelfStudy
# 1. Test Graph data structure (library borrow/association graph)
python graph_ds.py
# 2. Test Dijkstra's algorithm (library book recommendation)
python dijkstra_algo.py
