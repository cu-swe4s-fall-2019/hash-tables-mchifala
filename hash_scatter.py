import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def scatter_plot(x_data, y_data, x_label, y_label, title, outfile):
    width=3
    height=3
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_data,  y_data, '.', ms=1, alpha=0.5)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.savefig(outfile, bbox_inches='tight')
