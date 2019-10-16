import matplotlib.pyplot as plt
from hash_scatter import scatter_plot
from hash_functions import h_mult
from hash_functions import h_rolling
from hash_functions import h_ascii
from hash_tables import LinearProbe
from hash_tables import ChainedHash
from math import sqrt
from math import floor
import time
import random
import sys
import argparse
import matplotlib
matplotlib.use('Agg')


def main(data_file, table_size, hash_alg,
         collision_strategy, num_new_keys, out_file):
    """
    This function uses the command line arguments to
    instantiate a hash table, hash a user-defined number
    of keys to the table using a user-defined collision
    resolution strategy, times the inserts or searches,
    and graphs the result to a scatter plot

    Parameters:
    - data_file(str): A data file of keys to hash
    - table_size(int): The size of the hash table
    - hash_alg(str): h_ascii, h_rolling, or h_mult
    - collision_strategy(str): linear_probing or chaining
    - num_new_key(int): The number of new keys to hash
    - out_file(str): The final scatterplot file

    Returns:
    - N/A; a scatter plot is created

    """
    if hash_alg == 'h_ascii':

        if collision_strategy == 'linear_probing':
            ht = LinearProbe(table_size, h_ascii)
        elif collision_strategy == 'chaining':
            ht = ChainedHash(table_size, h_ascii)

    elif hash_alg == 'h_rolling':

        if collision_strategy == 'linear_probing':
            ht = LinearProbe(table_size, h_rolling)
        elif collision_strategy == 'chaining':
            ht = ChainedHash(table_size, h_rolling)

    elif hash_alg == 'h_mult':

        if collision_strategy == 'linear_probing':
            ht = LinearProbe(table_size, h_mult)
        elif collision_strategy == 'chaining':
            ht = ChainedHash(table_size, h_mult)

    x_data = []
    y_data = []

    for line in open(data_file):
        ht.add(line, "Value")
        if ht.m == num_new_keys:
            break
        line = line.strip()
        t0 = time.time()
        # ht.add(line, "Value")
        ht.search(line)
        t1 = time.time()
        x_data.append(ht.m/ht.n)
        y_data.append(t1-t0)

    scatter_plot(x_data, y_data, "Load factor", "Time to search",
                 "Search Performance: " + collision_strategy + " " + hash_alg,
                 out_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hash table input")

    parser.add_argument('data_file',
                        type=str,
                        help='Name of the file containing keys')

    parser.add_argument('table_size',
                        type=int,
                        help='Hash table size (n)')

    parser.add_argument('hash_alg',
                        type=str,
                        help='Hashing algorithm')

    parser.add_argument('collision_strategy',
                        type=str,
                        help='Collision resolution strategy')

    parser.add_argument('num_new_keys',
                        type=int,
                        help='Number of keys to add')

    parser.add_argument('out_file',
                        type=str,
                        help='File name of scatter plot')

    args = parser.parse_args()

    main(args.data_file, args.table_size, args.hash_alg,
         args.collision_strategy, args.num_new_keys, args.out_file)
