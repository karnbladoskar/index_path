import sys
import numpy as np
import pandas as pd
sys.path.append('../scripts')

try:
    import scripts.dat as dt
    import scripts.viz as viz

except ModuleNotFoundError:
    import dat as dt
    import viz as viz

# Test scripts
market = str(sys.argv[1])
market_dir = dt.get_market_dir(market)
file_names = dt.get_file_names(market_dir)
dt.load_data(market_dir, file_names)
data = dt.load_data(market_dir, file_names)
df = dt.drop_columns(data, 'Average price')
