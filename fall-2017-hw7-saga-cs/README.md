# MPCS 51042-2, Python Programming

**Week 8 Assignment**

**Due**: November 19 at 11:59pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1: Power Iteration

[Linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) is central to many disciplines in the sciences, including mathematics, engineering, physics, and computer science. At the heart of linear algebra is the solution of [systems of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations), such as:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d691839a2b284331b58b0820654d32e101e26a03" />

Usually, such systems of equations are cast in matrix-vector form:

<img src="http://latex2png.com/output//latex_32ccf6bfaaa319fbc2ee96110136e276.png" width="200" />

Understanding the properties of the matrices representing such systems is one of the primary goals of linear algebra. For this problem, you are asked to write an algorithm to solve for the largest [*eigenvalue*](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors) of a matrix using the [power iteration](https://en.wikipedia.org/wiki/Power_iteration) method. The eigenvalues of a matrix are the scalar values k that satisfy the following equation:

<img src="http://latex2png.com/output//latex_32b2ecfc8f1706dd54ad10856b151a95.png" width="100" />

i.e., the product of the matrix A and a vector x is the same as the product of the scalar k and the vector x. The corresponding vector x which satisfies this equation is called the *eigenvector*. The algorithm works by repeatedly multiplying an arbitrary vector by the matrix A. It can be proven that in doing so, the vector x eventually converges to the eigenvector corresponding to the largest eigenvalue.

Your algorithm should implement the following steps to find the largest eigenvalue of a matrix, A, and its corresponding eigenvector x:

1. The algorithm begins with a "guess" of the eigenvector. Your guess should be a column vector of ones. Let's refer to this vector as x.
2. Calculate the matrix multiplication of the A and x and store it in a new vector y. This can be done with the [numpy.dot](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.dot.html) function, the [numpy.matmul](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.matmul.html) function, or the `@` operator.
3. Calculate the [infinity norm](http://mathworld.wolfram.com/L-Infinity-Norm.html) of the y vector, either using regular numpy functions or [numpy.linalg.norm](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.norm.html). This is an estimate of the largest eigenvalue which we'll call k.
4.  Calculate a new estimate of the eigenvector, x, by dividing each element in y by k.
5.  Calculate the infinity norm of the residual, <img src="http://latex2png.com/output//latex_ccac517afce41ee8e0632cf9594e4020.png" width="60">.
6.  If the infinity norm of the residual is less than some specified tolerance, return the current value of k and x.
7.  Otherwise, repeat from step 2.

To confirm that your algorithm is working correctly, you can check it against [numpy.linalg.eigvals](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.eigvals.html).

### Specifications: `power_iteration`

- Your program should define a function `power_iteration(A, tolerance)` that solves for the largest eigenvalue of a matrix using the power iteration method as described above.
- `A` is a square matrix that is passed in and `tolerance` is the tolerance used in step 6 of the algorithm.
- The function should return a tuple with three objects:
  1. The final estimate of the largest eigenvalue, k.
  2. The final estimate of the corresponding eigenvector, x.
  3. The number of iterations that it took to reach convergence.
- The function must have a docstring describing its purpose, arguments, and return value.

### Specifications: `main`

- Write a function called `main` that solves for the largest eigenvalue of a 5x5 matrix of random numbers using the `power_iteration` function. You can create this matrix with the following code (we set the random number "seed" to ensure that the same matrix is always created): 
    ```python
    import numpy as np

    np.random.seed(1)
    A = np.random.rand(5, 5)
    ```
- Vary the tolerance passed to `power_iteration` to see how the number of iterations changes as the tolerance becomes smaller. Use the values 10<sup>-3</sup>, 10<sup>-4</sup>, 10<sup>-5</sup>, 10<sup>-6</sup>, 10<sup>-7</sup>, and 10<sup>-8</sup>.
- Using matplotlib, make a plot of the number of iterations (y-axis) versus the tolerance used in `power_iteration` (x-axis). Since the tolerance varies over multiple orders of magnitude, use [plt.semilogx](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.semilogx) (which uses a logarithmic scale on the x-axis) instead of plt.plot. Make sure your axes are labeled and save the plot as a PNG file with the name "iterations.png".

## Problem 2: Food inspections

Dr. Romano is starting to think about his wedding anniversary and wants to find a nice restaurant to take his wife to. He'd like to find a restaurant within walking distance of his apartment, but more importantly, he wants to make sure that whatever restaurant he chooses hasn't failed a health inspection! Fortunately, he has a class full of Python students who are eager to analyze Chicago's food inspection data using their newfound knowledge of Pandas.

Before you begin, run the `download-data.py` script to download the food inspection data from the Chicago Data Portal. When it has finished, you should have a ~189 MB file called "Food_Inspections.csv".

### Searching by ZIP

The first thing Dr. Romano wants to do is to rule out all restaurants that have failed an inspection within the last year within ZIP code 60661, where he lives. Write a function called `search_by_zip(dataframe)` that uses Pandas to determine all rows corresponding to restaurants (`'Facility Type'` column) in ZIP code 60661 (`'Zip'` column) that failed an inspection (`'Results'` column) since 11/1/2016 (`'Inspection Date'` column) and returns a DataFrame with only matching rows. The function should accept a DataFrame containing the original data as its only argument. It must have a docstring.

### Searching by location

Remembering that his students have already written a module to find the distance between two latitude/longitude pairs, he realizes it can be used to more accurately find restaurants that are nearby, considering that restaurants in other ZIP codes are also close to his apartment. Write a function called `search_by_location(dataframe)` that uses Pandas to determine all rows corresponding to restaurants that failed an inspection since 11/1/2016 and are within 0.5 miles of Dr. Romano's apartment at latitude=41.8873906 and longitude=-87.6459561 (please don't show up at his house, unless you are coming to offer free babysitting in which case you're always welcome!). The function should accept a DataFrame containing the original data as its only argument and return a DataFrame with matching rows sorted by increasing distance from the given latitude/longitude. It also must have a docstring.

**HINT**: To apply a function to each element of a Series/DataFrame, you can use the [Series.map](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html) or [DataFrame.apply](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) methods.