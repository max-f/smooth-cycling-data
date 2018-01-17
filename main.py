#!/usr/bin/env python

import json
import click as click
from typing import List
from datetime import datetime, timedelta
import numpy as np

from utils import plot, smooth


@click.command()
# @click.option('-t', '--datatype', default='hr')
@click.option('-f', '--filepath', type=str)
def smooth_data(filepath: str) -> None:
    with open(filepath, 'rb') as json_data:
        d = json.load(json_data) # , encoding='utf-8-sig')
        modified_data = check_data(d)


def check_data(d: dict) -> dict:
    try:
        samples = d['RIDE']['SAMPLES']
        powerdata = [x['WATTS'] for x in samples]
        heartrate = [x['HR'] for x in samples]
        # Find spikes/drops 
        print(len(heartrate))
        spikes = collect_abnormal(heartrate)
        
        for spike in spikes:
            print(spike)
            print('Start: {}'.format(format_time(spike[0])))
            print('End: {}'.format(format_time(spike[1])))

        xs = list(range(len(heartrate)))

        # Smooth data
        savitzky = list(smooth.savitzky_golay(np.array(heartrate), window_size=21, order=3))


        plot.plot(xs, heartrate, savitzky)

        # Assign smoothed data
        return d
    except KeyError:
        return d


def collect_abnormal(heartrate: List[int]) -> List[tuple]:
    threshold = 10
    return [(i, i+1) for i, t1 in enumerate(heartrate[:-1]) 
            if abs(t1 - heartrate[i+1]) >= threshold]


def format_time(secs: int) -> str:
    secs = timedelta(seconds=secs)
    d = datetime(1, 1, 1) + secs
    return '{}:{}:{}:{}'.format(d.day, d.hour, d.minute, d.second)


def output(spikes: List[str]) -> None:
    pass


class Workout(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.heartrate = list()
        self.power = list()


if __name__ == '__main__':
    smooth_data()


# vim: expandtab tabstop=4 shiftwidth=4 softtabstop=4
