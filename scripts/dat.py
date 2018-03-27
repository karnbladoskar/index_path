import sys
import numpy as np
import pandas as pd

try:
    import scripts.viz as viz
except ModuleNotFoundError:
    import viz as viz

def get_market_dir(market):
    """
    """
    DATA_DIR = '../data/'

    if market.lower() == 'omxs30':
        market_dir = DATA_DIR + 'OMXS30/'

    elif market.lower() == 'sp500':
        market_dir = DATA_DIR + 'S&P500/'

    return market_dir


def get_file_names(path, ext = '.csv'):
    """
    Get the file names of specified extension.
    :param path: Path to the search directory.
    :param ext: File extension to search for.
    :return filenames: List of filenames.
    """
    import os

    file_names = []
    filectr = 0
    for idx, file in enumerate(os.listdir(path)):
        if file.endswith(ext):
            file_names.append(file)
            print('Found: |  {}  | on Index: |  {}  |'.format(file, filectr))
            filectr += 1

    print('\n')

    return file_names


def load_data(market_dir, file_names):
    """
    """
    data_list = []
    for file in file_names:
        d = pd.read_csv(market_dir + file, sep=';')
        data_list.append(d)

    data = pd.concat(data_list)

    data['High price'] = data['High price'].str.replace(',', '.')
    data['Low price'] = data['High price'].str.replace(',', '.')
    data['Closing price'] = data['High price'].str.replace(',', '.')

    return data
