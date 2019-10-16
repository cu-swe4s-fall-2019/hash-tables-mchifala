import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def scatter_plot(x_data, y_data, x_label, y_label, title, outfile):
    """
    This function creates a scatter plot displaying the data
    contained in two lists. It also saves the figure to a file.

    Parameters:
    - x_data(list): A list of list of numbers
    - y_data(list): A list of list of numbers
    - x_label(str): The label for the x-axis
    - y_label(str): The label for the y-axis
    - title(str): The title for the scatter plot
    - outfile(str): The name of the file we want to create

    Returns:
    - None, however, a file is saved.

    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_data,  y_data, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.savefig(outfile, bbox_inches='tight')
