import matplotlib.pyplot as plt
import mplleaflet
import numpy as np
import pandas as pd
from scipy.stats.kde import gaussian_kde
from potential_flow import potential_flow

def potential_flow(lon, lat, weight1, weight2, n=40):
    kde1 = gaussian_kde(np.vstack([lon, lat]), weights=weight1)
    kde2 = gaussian_kde(np.vstack([lon, lat]), weights=weight2)

    x, y = np.mgrid[lon.min():lon.max():n * 1j, lat.min():lat.max():n * 1j]

    z1 = kde1.evaluate(np.vstack([x.flatten(), y.flatten()]))
    z2 = kde2.evaluate(np.vstack([x.flatten(), y.flatten()]))
    z1 = z1.reshape(x.shape)
    z2 = z2.reshape(x.shape)

    Z = z2 - z1

    derivation = np.gradient(Z)

    return x, y, derivation


def toGeojson(x, y, derivation):
    fig = plt.figure()
    Q = plt.quiver(
        x, y, derivation[0], derivation[1],
    )
    return mplleaflet.fig_to_geojson(fig=fig)


def dataForD3(x, y, derivation, scale=1):
    x1 = x.flatten()
    y1 = y.flatten()
    x2 = x1 + derivation[0].flatten() * scale
    y2 = y1 + derivation[1].flatten() * scale
    df = pd.DataFrame(np.vstack([x1, y1, x2, y2, np.full(len(x1), scale)]).T, columns=['x1', 'y1', 'x2', 'y2', 'scale'])
    return df


def plot(x, y, derivation):
    fig = plt.figure()
    Q = plt.quiver(
        x, y, derivation[0], derivation[1],
    )
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('data/sample.csv')
    # lon = data['lon'].to_numpy(dtype=float)
    # lat = data['lat'].to_numpy(dtype=float)
    # w1 = data['pap_r1'].to_numpy(dtype=float)
    # w2 = data['pap_r2'].to_numpy(dtype=float)
    # x, y, derivation = potential_flow(lon, lat, w1, w2)
