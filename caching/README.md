<img  height="50px" align="right" src="https://raw.githubusercontent.com/fchavonet/fchavonet/main/resources/images/logo-holberton_school.png" alt="Holberton School logo">

# Caching

## 🔖 Table of contents

<details>
        <summary>
        CLICK TO ENLARGE 😇
        </summary>
        📄 <a href="#description">Description</a>
        <br>
        🎓 <a href="#objectives">Objectives</a>
        <br>
        📋 <a href="#requirements">Requirements</a>
        <br>
        📝 <a href="#instructions">Instructions</a>
        <br>
        🔨 <a href="#tech-stack">Tech stack</a>
        <br>
        📂 <a href="#files-description">Files description</a>
        <br>
        💻 <a href="#installation_and_how_to_use">Installation and how to use</a>
        <br>
        ♥️ <a href="#thanks">Thanks</a>
        <br>
        👷 <a href="#authors">Authors</a>
</details>

## 📄 <span id="description">Description</span>

This project introduces different caching algorithms and their implementations in Python. A caching system is a mechanism to store and retrieve data efficiently, minimizing the need for recalculations or slower data-fetching processes. You will implement several caching algorithms like `FIFO`, `LIFO`, `LRU`, `MRU`, and `LFU`.

## 🎓 <span id="objectives">Objectives</span>

At the end of this project, I had to be able to explain to anyone, **without the help of Google** :

- What a caching system is.
- The purpose of caching systems.
- Definitions and implementations of the following caching algorithms:
    - `FIFO` (First In, First Out).
    - `LIFO` (Last In, First Out).
    - `LRU` (Least Recently Used).
    - `MRU` (Most Recently Used).
    - `LFU` (Least Frequently Used).
- The limits of caching systems.

## 📋 <span id="requirements">Requirements</span>

- All my files should end with a new line.
- The first line of all my files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory
- My code should use the `pycodestyle` style (version 2.5).
- All my files must be executable
- The length of my files will be tested using `wc`.
- All my modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All my classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All my functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).

## 📝 <span id="instructions">Instructions</span>

<details>
    <summary>
        <b>0. Basic dictionary</b>
    </summary>
    <br>

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- This caching system doesn’t have limit.
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-web_back_end`.
- Directory: `caching`.
- File: `0-basic_cache.py`.
<hr>
</details>

<details>
    <summary>
        <b>1. FIFO caching</b>
    </summary>
    <br>

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS:`
        - You must discard the first item put in cache (FIFO algorithm).
        - You must print `DISCARD:` with the `key` discarded and following by a new line.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If key is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

guillaume@ubuntu:~/$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-web_back_end`.
- Directory: `caching`.
- File: `1-fifo_cache.py`.
<hr>
</details>

<details>
    <summary>
        <b>2. LIFO Caching</b>
    </summary>
    <br>

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS:`
        - You must discard the last item put in cache (LIFO algorithm).
        - You must print `DISCARD:` with the `key` discarded and following by a new line.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.


```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

guillaume@ubuntu:~/$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-web_back_end`.
- Directory: `caching`.
- File: `1-fifo_cache.py`.
<hr>
</details>

<details>
    <summary>
        <b>3. LRU Caching</b>
    </summary>
    <br>

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent `init: super().__init__()`.
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS:`
        - You must discard the least recently used item (LRU algorithm).
        - You must print `DISCARD:` with the `key` discarded and following by a new line.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-web_back_end`.
- Directory: `caching`.
- File: `3-lru_cache.py`.
<hr>
</details>

<details>
    <summary>
        <b>4. MRU Caching</b>
    </summary>
    <br>

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key`key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS:`.
        - You must discard the most recently used item (MRU algorithm).
        - You must print `DISCARD:` with the `key` discarded and following by a new line.
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-web_back_end`.
- Directory: `caching`.
- File: ` 4-mru_cache.py`.
<hr>
</details>

<details>
    <summary>
        <b>5. LFU Caching</b>
    </summary>
    <br>

Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
- You can overload `def __init__(self):` but don’t forget to call the parent `init: super().__init__()`.
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS:`
        - You must discard the least frequency used item (LFU algorithm).
        - If you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
        - You must print `DISCARD:` with the key discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the `key` doesn’t exist `in self.cache_data`, return `None`.

```
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()

guillaume@ubuntu:~/$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
guillaume@ubuntu:~/$ 
```

#
**Repo:**
- GitHub repository: `holbertonschool-web_back_end`.
- Directory: `caching`.
- File: `100-lfu_cache.py`.
<hr>
</details>

## 🔨 <span id="tech-stack">Tech stack</span>

<p align="left">
    <img src="https://img.shields.io/badge/PYTHON-3776ab?logo=python&logoColor=white&style=for-the-badge" alt="Python badge">
</p>

## 📂 <span id="files-description">File description</span>

| **FILE**           | **DESCRIPTION**                                           |
| :----------------: | --------------------------------------------------------- |
| `0-basic_cache.py` | Basic dictionary-based caching implementation.            | 
| `1-fifo_cache.py`  | Caching system using FIFO algorithm.                      |
| `2-lifo_cache.py`  | Caching system using LIFO algorithm.                      |
| `3-lru_cache.py`   | Caching system using LRU algorithm.                       |
| `4-mru_cache.py`   | Caching system using MRU algorithm.                       |
| `100-lfu_cache.py` | Caching system using LFU algorithm.                       |
| `base_caching.py`  | Base class containing shared functionality and constants. |
| `README.md`        | The readme file you are currently reading 😉.             |

## 💻 <span id="installation_and_how_to_use">Installation and how to use</span>

**Installation:**

1. Clone this repository:
    - Open your preferred Terminal.
    - Navigate to the directory where you want to clone the repository.
    - Run the following command:

```
git clone https://github.com/fchavonet/holbertonschool-web_back_end.git
```

2. Open the repository you've just cloned.

3. Navigate to the `caching` directory:

```
cd caching
```

4. Ensure all files are executable:

```
chmod 777 *.py
```

**How to use:**

1. Run the test files for each task:

```
python3 0-main.py
```

```
python3 1-main.py
```

```
python3 2-main.py
```

```
python3 3-main.py
```

```
python3 4-main.py
```

```
python3 100-main.py
```

2. Replace test files as needed to test other caching systems.

## ♥️ <span id="thanks">Thanks</span>

A big thank you to all my Holberton School peers for their help and support throughout these projects.

## 👷 <span id="authors">Authors</span>

**Fabien CHAVONET**
- Github: [@fchavonet](https://github.com/fchavonet)
