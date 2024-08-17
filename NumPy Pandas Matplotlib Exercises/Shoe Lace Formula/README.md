# Shoe Lace Formula for Polygon Area
## Purpose:
Calculates the area of a simple polygon given the Cartesian coordinates of its vertices.

## Method:
Implements the shoelace formula, also known as Gauss's area formula. This algorithm calculates the area by taking the signed sum of the cross products of consecutive vertices.

### Input:

Number of vertices (n)
Cartesian coordinates of each vertex (x, y) in subsequent lines
Output:

Area of the polygon, rounded to one decimal place
Example:
Input:

```bash
4
2 2
2 4
5 4
9 2
```

### Output:

```bash
10.0
```


## How it works:

For each pair of consecutive vertices, compute the determinant of a 2x2 matrix formed by their coordinates.
Sum up these determinants.
Divide the sum by 2 to get the area.
Note:

Assumes the polygon is simple (no self-intersections).
Coordinates must be given in Cartesian form.
Vertices must be listed in order.

### How to run? ###
```bash
python Shoe_Lace_Formula.py
```