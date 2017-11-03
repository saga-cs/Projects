# MPCS 51042-2, Python Programming

**Week 2 Assignment**

**Due**: October 8 at 11:59pm CT

## Problem 1

Write a function that prints an N by N game board. The function definition should be:

```python
def draw_board(n):
    ...
```

The resulting game board should look like the following (this particular example is for n=3, but the function should work with any value of n):

```
----------
|  |  |  |
----------
|  |  |  |
----------
|  |  |  |
----------
```

## Problem 2

Write a generator function that mimics the Unix `grep` command. The function definition should look like:

```python
def grep(pattern, lines, ignore_case=False):
    ...
```

`pattern` should be a string that represents a "pattern" that we want to find within each line. `lines` should be an iterable of strings (this could be a list of strings, a file object that can be iterated over, or a generator). Finally, the `ignore_case` argument indicates whether we want to search for the pattern in a case-sensitive or case-insensitive manner. To be clear, the function must `yield` values, not return a list of matching strings.

Example usage:

```pycon
>>> lines = ['I went to Poland.',
...          'He went to Spain.',
...          'She is very happy.']
>>> for line in grep('went', lines):
...     print(line)
I went to Poland.
He went to Spain.
>>> for line in grep('i', lines, ignore_case=True):
...     print(line)
I went to Poland.
He went to Spain.
She is very happy.
```


## Problem 3

Write a function that joins together single components of a path to produce a
full path with directories separate by slashes. For example, it should operate
in the following manner:
```pycon
>>> full_paths(['usr', ['lib', 'bin'], 'config', ['x', 'y', 'z']])
['/usr/lib/config/x',
 '/usr/lib/config/y',
 '/usr/lib/config/z',
 '/usr/bin/config/x',
 '/usr/bin/config/y',
 '/usr/bin/config/z']
>>> full_paths(['codes', ['python', 'c', 'c++'], ['Makefile']], base_path='/home/user/')
['/home/user/codes/python/Makefile',
 '/home/user/codes/c/Makefile',
 '/home/user/codes/c++/Makefile']
```

The function definition should look as follows:

```python
def full_paths(path_components, base_path='/'):
    ...
```

The `path_components` argument accepts an iterable in which each item is either a list of strings or a single string. Each item in `path_components` represents a level in the directory hierarchy. The function should return every combination of items from each level. With the `path_components` list, a string and a list containing a single string should produce equivalent results as the second example above demonstrates. The `base_path` argument is a prefix that is added to every string that is returned. The function should return a list of all the path combinations (a list of strings).

If you need to check whether a variable is iterable, the "Pythonic" way to do this is

```python
from collections.abc import Iterable

if isinstance(x, Iterable):
    ...
```

However, note that strings are iterable too!

You are allowed to use functionality from the standard library for this problem.

## Problem 4

Nowadays we take word completion for granted. Our phones, text editors, and word processing programs all give us suggestions for how to complete words as we type based on the letters typed so far. These hints help speed up user input and eliminate common typographical mistakes (but can also be frustrating when the tool insists on completing a word that you don’t want completed).

You will implement two functions that such tools might use to provide command completion. The first function, `fill_competions`, will construct a dictionary designed to permit easy calculation of possible word completions. A problem for any such function is what vocabulary, or set of words, to allow completion on. Because the vocabulary you want may depend on the domain a tool is used in, you will provide `fill_competions` with a representative sample of documents from which it will build the completions dictionary. The second function, `find_completions`, will return the set of possible completions for a start of any word in the vocabulary (or the empty set if there are none). In addition to these two functions, you will implement a simple main program to use for testing your functions.

## Specifications

- `fill_completions(fd)` returns a dictionary. This function takes as input an opened file.

  - The keys of the dictionary returned are tuples of the form `(n,l)` for a non-negative integer `n` and a lowercase letter `l`.
  - The value associated with key `(n, l)` is the set of words in the file that contain the letter `l` at position `n`. For simplicity, all vocabulary words are converted to lower case. For example, if the file contains the word "Python" and `c_dict` is the returned dictionary, then the sets `c_dict[0,"p"]`, `c_dict[1,"y"]`, `c_dict[2,"t"]`, `c_dict[3,"h"]`, `c_dict[4,"o"]`, and `c_dict[5,"n"]` all contain the word `"python"`.
  - Words are stripped of punctuation.
  - "Words" containing non-alphabetic characters are ignored, as are words of length 1 (since there is no reason to complete the latter).

- `find_completions(prefix, c_dict)` returns a set of strings. This function takes a prefix of a vocabulary word and a completions dictionary of the form described above. It returns the set of vocabulary words in the completions dictionary, if any, that complete the prefix. It the prefix cannot be completed to any vocabulary words, the function returns an empty set.

- `main()`, the test driver:

  - Opens a file named `ap_docs.txt`. This file contains a collection of old newswire articles. Each article in the collection is separated by a line that contains only the token `<NEW DOCUMENT>`. We don’t care about the distinction between articles for the purpose of building a completions dictionary, so you should just ignore the separator lines and continue processing the file.
  - Calls `fill_competions` to fill out a completions dictionary using this file.
  - Repeatedly prompts the user for a prefix to complete.
  - Prints each word from the set of words that can complete the given prefix (one per line). If no completions are posisble, it should just print "No completions".
  - Quit if the user presses Ctrl+D on macOS/Linux or Ctrl+Z on Windows (this will result in `EOFError` being raised).

- To call the `main()` function, put a block at the end of your script with the follow lines (we will discuss this technique more in week 5). This allows your script to run when executed from a command line.
    ```python
    if __name__ == '__main__':
        main()
    ```

## Example session

```sh
$ python problem4.py
Enter prefix: z
  zones
  zero
  zone
Enter prefix: lu
  luncheon
  lung
  luggage
  luxurious
  luckier
  lull
  lunch
  ludicrous
  luminous
  lurched
Enter prefix: multi
  multilateral
  multimillionaire
  multicolored
  multibillion
Enter prefix: multis
  No completions
Enter prefix: [Ctrl+D]
```