import pandas as pd
from potential_flow import pf


if __name__ == '__main__':
    data = pd.read_csv('data/sample.csv')
    lon = data['lon'].to_numpy(dtype=float)
    lat = data['lat'].to_numpy(dtype=float)
    w1 = data['pap_r1'].to_numpy(dtype=float)
    w2 = data['pap_r2'].to_numpy(dtype=float)
    x, y, derivation = pf.potential_flow(lon, lat, w1, w2)
    pf.plot(x, y, derivation)
