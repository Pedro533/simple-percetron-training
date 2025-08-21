# Perceptron Logical Gates

This repository contains a simple Python implementation of a single-layer perceptron.  
It can be trained to reproduce different logical functions such as **AND**, **OR**, or any other linearly separable gate.

---

## Features
- Implementation of the perceptron learning rule in Python.
- Adjustable learning rate (`λ`).
- Weight and threshold updates until convergence.
- Training datasets easily customizable for different logic gates.
- Utility function to classify new inputs after training.

---

## Example: Truth Tables

### AND
| x1 | x2 | y |
|----|----|---|
| 0  | 0  | 0 |
| 0  | 1  | 0 |
| 1  | 0  | 0 |
| 1  | 1  | 1 |

### OR
| x1 | x2 | y |
|----|----|---|
| 0  | 0  | 0 |
| 0  | 1  | 1 |
| 1  | 0  | 1 |
| 1  | 1  | 1 |

---

## Getting Started

### Requirements
- Python 3.x

No additional libraries are required (only standard Python).

### Running the Code
Clone the repository and run:

```bash
python perceptron_gates.py
