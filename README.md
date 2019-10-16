# Time Series Basics
V1.0: The goal of this assignment is to implement some basic hash functions and collision resolution strategies. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following packages were used during the development of this code. Other versions may be supported, but cannot be guaranteed.

- python (version 3.7.0)
- pycodestyle (version 2.5.0)
- matplotlib (version 3.1.1)

### Installation

The following steps will help you set up the proper environment on your machine. All example commands are entered directly into terminal.

**Installing conda:**

```
cd $HOME
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
. $HOME/miniconda3/etc/profile.d/conda.sh
conda update --yes conda
conda config --add channels bioconda
echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

**Creating conda environment:**

```
conda create --yes -n <your_environment>
conda install --yes python=3.7
```

**Activating conda environment:**

```
conda activate <your_environment>
```

**Installing pycodestyle:**

pycodestyle is used to ensure that all .py files adhere to the PEP8 style guidelines.

```
conda install -y pycodestyle
```

**Installing numpy:**

numpy is used as part of matplotlib.

```
conda install -y numpy
```

**Installing matplotlib:**

matplotlib is used to generate the scatter plots of the data.

```
conda install -y matplotlib
```

### Classes and Methods

#### LinearProbe
This class is used to represent a hash table that uses linear probing as a collision strategy

    Attributes:
    - hash_function: h_ascii, h_rolling, or h_mult
    - n(int): The hash table size
    - table(list): The actual hash table itself
    - m(int): The number of elements in the hash function

    Methods:
    - add(self, key, value): This function adds a key-value pair to the hash table
    - search(self, key): This function searchs for a key in the hash table
    
#### ChainedHash
This class is used to represent a hash table that uses chaining as a collision strategy

    Attributes:
    - hash_function: h_ascii, h_rolling, or h_mult
    - n(int): The hash table size
    - table(list): The actual hash table itself
    - m(int): The number of elements in the hash function

    Methods:
    - add(self, key, value): This function adds a key-value pair
                             to the hash table
    - search(self, key): This function searchs for a key in the
                         hash table

### Examples

analyze.py uses the command line arguments to instantiate a hash table, hash a user-defined number of keys from a user-defined file to the table using a user-defined collision resolution strategy, times the inserts or searches, and graphs the result to a scatter plot.

```
python analyze_hash.py <data_file> <table_size> <hashing_algorithm> <collision_resolution_strategy> <number_of_keys_to_hash> <outfile_name>
```

test_hash.py runs unit tests on the hashing functions in hash_functions.py, the scatter_plot method in hash_scatter.py, and the classes in hash_tables.py to ensure both accuracy and proper error handling.

```
python test_hash.py
```

### Experiments
I ran a total of 12 experiments. For both the insert and search methods, I tested both linear probing and chaining collision resolutions for each of my three hashing algrorithms (h_ascii, h_rolling, and h_mult). Scatter plots are available for all 12 experiments in the "/search_graphs" and "/insert_graphs" directories. 

In general, the best performing hashing algorithm - collision resolution strategy combination was the rolling polynomial hashing method and chaining. This combination performed well at a high load factor, which can be seen in the plots below. 

#### Rolling Polynomial Hashing Method and Chaining
![](/insert_graphs/h_rolling_chaining.png)
![](/search_graphs/h_rolling_chaining.png)


The worst performing combination was the ascii hashing method and linear probing. This combination performed poorly at a high load factor, which can be seen in the plots below. 

#### ascii Hashing Method and Linear Probing
![](/insert_graphs/h_ascii_linear_probing.png)
![](/search_graphs/h_ascii_linear_probing.png)


## Authors

**Michael W. Chifala** - University of Colorado, Boulder, CSCI 7000: Software Engineering for Scientists


## Acknowledgments

* Ryan Layer's CSCI 7000 "Development Environment" document
* Ryan Layer's CSCI 7000 "Continuous Integration with Travis CI" document
* Ryan Layer's CSCI 7000 "Test-Driven Development" document
* Ryan Layer's CSCI 7000 "Hash Table" document
* PEP8 Style Guidelines: https://www.python.org/dev/peps/pep-0008/
* Github: PurpleBooth/README-Template.md
