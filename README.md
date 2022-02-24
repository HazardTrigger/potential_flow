<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Potential Flow</h3>

  <p align="center">
    Understanding the spatio-temporal patterns of energy consumption
    <br />
    <a href="https://www.sciencedirect.com/science/article/pii/S0360544221007428"><strong>View related paper »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="https://github.com/HazardTrigger/potential_flow/issues">Report Bug</a>
    ·
    <a href="https://github.com/HazardTrigger/potential_flow/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#citation">Citation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About

Understanding the spatio-temporal patterns of energy consumption can help utilities improve operations, develop energy
strategies and offer personalized services. For electricity consumption data, we found that there exist demand shifts
across different geographical locations over time. This raises an interesting question about how to visualize these
demand shifts in a user-friendly way to help utilities balance energy supply and improve flexibility. This python
package is an implementation of the algorithm described in the
article: [`Understanding energy demand behaviors through spatio-temporal smart meter data analysis`.](https://www.sciencedirect.com/science/article/pii/S0360544221007428)

[![](https://github.com/HazardTrigger/potential_flow/blob/master/images/modeling-1.png)](https://www.sciencedirect.com/science/article/pii/S0360544221007428)

Schematic diagram of energy demand shift modeling. The procedure for modeling the energy demand shift can be divided
into three steps: 1) The locality data is weighted by the energy consumption at each moment; 2) Strength maps of the
energy demand for each moments are calculated through kernel density estimation; 3) Modeling and visualization of the
energy demand shift based on potential-flow

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

This package needs to install the following dependencies. For details, please see [requirements.txt](requirements.txt).

  ```sh
    matplotlib==3.3.2
    mplleaflet==0.0.5
    numpy==latest
    pandas==latest
    scikit-learn==latest
    scipy==latest
  ```

### Installation

   ```sh
   pip install -i https://test.pypi.org/simple/ Potential-flow==0.0.3
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

###Example
```python
    import pandas as pd
    from potential_flow import pf    

    data = pd.read_csv('tests/data/sample.csv')
    lon = data['lon'].to_numpy(dtype=float)
    lat = data['lat'].to_numpy(dtype=float)
    w1 = data['pap_r1'].to_numpy(dtype=float) # t0 data
    w2 = data['pap_r2'].to_numpy(dtype=float) # t1 data
    x, y, derivation = pf.potential_flow(lon, lat, w1, w2) # generate flow field data
    pf.plot(x, y, derivation) # visualization
```
###Result
![](https://github.com/HazardTrigger/potential_flow/blob/master/images/result.png)

###Export data for leaflet or Mapbox

```python
from potential_flow import pf

data = pf.toGeojson(x, y, derivation)
```

###Export data for D3

```python
from potential_flow import pf

data = pf.dataForD3(x, y, derivation)
```

<!-- LICENSE -->

## License

Distributed under the GNU License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

[@Junqi Wu]() - wujunqi@tju.edu.cn

Project Link: [https://github.com/HazardTrigger/potential_flow](https://github.com/HazardTrigger/potential_flow)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->

## Citation
We welcome further in-depth collaboration. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!
```sh
  @article{niu2021understanding,
      title={Understanding energy demand behaviors through spatio-temporal smart meter data analysis},
      author={Niu, Zhibin and Wu, Junqi and Liu, Xiufeng and Huang, Lizhen and Nielsen, Per Sieverts},
      journal={Energy},
      volume={226},
      pages={120493},
      year={2021},
      publisher={Elsevier}
 }
```

```sh
  @article{wu20203,
      title={$ E\^{} 3$: Visual Exploration of Spatiotemporal Energy Demand},
      author={Wu, Junqi and Niu, Zhibin and Wu, Jing and Liu, Xiufeng and Zhang, Jiawan},
      journal={arXiv preprint arXiv:2006.09487},
      year={2020}
 }
```