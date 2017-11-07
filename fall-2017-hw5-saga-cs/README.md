# MPCS 51042-2, Python Programming

**Week 5 Assignment**

**Due**: November 5 at 11:59pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1: Basic decorator

Write a decorator called `only_python` that causes the resulting function to return its result only if one of the arguments is the string `"Python"`. When `"Python"` does not appear as an argument, the decorated function should return `None`. The decorator should account for both positional and keyword arguments.

Example:

```pycon
>>> @only_python
... def times3(x):
...     return 3*x
>>> times3(10)
>>> times3(5.0)
>>> times3("python")
>>> times3("Python")
'PythonPythonPython'
```

## Problem 2: Validating return values

Write a parameterized decorator called `returns()` that validates the type of the return value of a function. If the function attempts to return a value that is not of the specified type, `TypeError` should be [raised](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). Furthermore, if the value passed to `returns()` is not itself a type object, a `TypeError` should be raised at the time the wrapped function is defined!

Example:

```pycon
>>> @returns(int)
... def f(a, b):
...     return a + b

>>> f(1, 2)
3

>>> f(1.0, 2.0)
Traceback (most recent call last):
TypeError: f should return a int

>>> f("hello", "world")
Traceback (most recent call last):
TypeError: f should return a int

>>> @returns(3)
... def foo(bar):
...     print(bar)
Traceback (most recent call last):
TypeError: '3' is not a type object.
```

## Problem 3: LRU cache for memoization

[Memoization](https://en.wikipedia.org/wiki/Memoization) is an optimization technique for speeding up function calls by caching the function result for a given set of inputs. This works so long as the function is *pure*, i.e., it always returns the same result for the same arguments. The Python standard library actually includes a function decorator in the functools module called [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) that performs memoization on any function that it wraps with one twist--it only stores function results for for the N most recent calls. This is called a *least recently used* (LRU) cache because the least recently used items are discarded from the function result cache if it has reached its maximum size. For this problem, you must write your own version of the `lru_cache` decorator.

### Specifications

- `lru_cache(maxsize=128)` should be a function that returns a decorator that memoizes any function it wraps using a LRU cache.
- The `maxsize` argument determines the maximum number of entries that the cache stores and has a default value of 128.
- The standard library version of `lru_cache` has an extra `typed` argument---you do not need to account for this argument in your version.
- The wrapped function should have an attribute called `cache_info` that is a function that returns a [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple) storing the number of hits and misses in the cache as well as the maximum and current size of the cache. See the example below for how the `lru_cache` decorator and its `cache_info` function are used. The items in the namedtuple are as follows:
    - `hits`: The number of calls to the function where the result was calculated previously and can be returns from the cache.
    - `misses`: The number of calls to the function where the result was not previously calculated.
    - `maxsize`: The maximum number of entries that the cache can store.
    - `currsize`: The number of entries currently stored in the cache.
- Use the `@functools.wraps` decorator to make sure that function metadata is copied to the wrapped function.
- You are free to use any data structure you wish to implement the cache.

### Example

```pycon
>>> @lru_cache(maxsize=32)
... def get_pep(num):
...     'Retrieve text of a Python Enhancement Proposal'
...     resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
...     try:
...         with urllib.request.urlopen(resource) as s:
...             return s.read()
...     except urllib.error.HTTPError:
...         return 'Not Found'

>>> for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
...     pep = get_pep(n)
...     print(n, len(pep))

>>> get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
```