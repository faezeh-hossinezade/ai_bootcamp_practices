# Production Optimization Problem

### Problem Description
This Python script solves a production optimization problem using linear programming. We have a workshop producing three products, each requiring specific amounts of machining, welding, and sheet metal working time. The goal is to maximize profit given the limited capacity of each machine and the selling price of each product.

### Inputs
* **constraints:** A matrix representing the resource constraints (e.g., machining time, welding time).
* **b:** A vector representing the right-hand side of the constraints (e.g., available machine hours).
* **c:** A vector representing the coefficients of the objective function (i.e., profit per unit of each product).

### Output
* A tuple containing:
  * The optimal value of the objective function (maximum profit).
  * A list of the optimal values of the decision variables (number of units to produce for each product).

### Function `simplex`
The `simplex` function implements the simplex algorithm to solve the linear programming problem. It takes the following arguments:
* `constraints`: The constraint matrix.
* `b`: The right-hand side vector.
* `c`: The objective function coefficients.

### Example Usage
```python
import numpy as np
from optimization import simplex

# Define the problem
constraints = np.array([[1, 2, 1],  # Machining
                        [3, 0, 2],  # Welding
                        [1, 4, 0]])  # Sheet metal working
b = np.array([430, 460, 400])  # Machine capacities
c = np.array([-3000, -2000, -5000])  # Profit per unit

# Solve the problem
result = simplex(constraints, b, c)
print(result)