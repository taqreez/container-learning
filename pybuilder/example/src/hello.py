import os
import pandas as pd

if __name__ == '__main__':
    print('Hello containers world!')
    print('Number of cpus: ', os.cpu_count())
    print('pandas version: ', pd.__version__)
