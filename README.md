# Username Permutation Generator

## Purpose

This generator was created to more easily check username combinations for human-based OSINT operations. When someone uses similar usernames across different platforms, I got tired of trying to think of all combinations of their usernames, and I'm sure I miss some. Therefore, this little script automates the process of creating permutations of usernames a user may have, given arguments from the OSINTer.

## Use

```python3 generator.py -i element1,element2,element3,...,elementX [-s <True/False>]```

Currently, the script does not repeat elements, and will only have one instance of the element in any permutation. If you'd like to repeat an element, enter it in the input as many times as needed.

### Arguments

Each argument is an "element" in your target's username that's commonly used. For instance, if your target's usernames usually have "tiger" and "42" in it, those would be your elements. Its input format would be `tiger,42`.

**-i, --input**: A comma separated array of elements of a username
**-s, --special**: A boolean flag (Python syntax) to include the special characters `.-_`

### Results

Results of this script will look like:

```
python3 generator.py -i 1,2,3
123
132
213
231
312
321
```

### Examples

**Command:** `python3 generator.py -i 1,2,abc -s True`

**Results:**
```
12abc._-
12abc.-_
12abc_.-
12abc_-.
12abc-._
12abc-_.
12.abc_-
12.abc-_
...
```

**Command:** `python3 generator.py -i 1,2,abc -s False`

**Results:**
```
12abc
1abc2
21abc
2abc1
abc12
abc21
```

**Command:** `python3 generator.py -i 1,1,2,abc -s False`

**Results:**
```
112abc
11abc2
121abc
12abc1
1abc12
1abc21
112abc
11abc2
121abc
12abc1
1abc12
1abc21
211abc
21abc1
211abc
21abc1
2abc11
2abc11
abc112
abc121
abc112
abc121
abc211
abc211
```
