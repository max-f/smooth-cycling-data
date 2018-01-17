#!/usr/bin/env python

from typing import List

import matplotlib.pyplot as plt
import seaborn as sns


def compare_plot(xs: List[int], ys_old: List[int], ys_new: List[int]) -> None:
    pass

def plot(xs: List[int], orig_ys: List[int], savitzky: List[int]) -> None:
    # sns.set_style('darkgrid')
    f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    ax1.plot(xs, orig_ys, label='original curve')
    ax1.legend(loc='best')

    ax2.plot(xs, savitzky, label='savitzky-golay')
    ax2.legend(loc='best')

    f.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)

    # l1, = plt.plot(xs, orig_ys, label='original curve')

    # l2, = plt.plot(xs, savitzky, label='savitzky-golay')

    # lns = [l1, l2]
    # ax.legend(handles=lns, loc='best')
    plt.show()