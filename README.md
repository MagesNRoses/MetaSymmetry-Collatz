# MetaSymmetry-Collatz
Investigación estudiantil sobre simetrías estratificadas en la dinámica de Collatz

## Descubrimiento Clave
He observado que las trayectorias de Collatz se organizan en 4 regiones dinámicas:
- **Región A**: x > ε > log₂3
- **Región B**: ε > x > log₂3
- **Región C**: log₂3 > x > ε
- **Región D**: log₂3 > ε > x

**Hallazgo sorprendente**: Las trayectorias que pasan por la región ABC convergen más rápido.

## Primeros Resultados
![Regiones Collatz para n=27](collatz_regions.png)

## Cómo replicar
```bash
git clone https://github.com/MagesNRoses/MetaSymmetry-Collatz.git
pip install -r requirements.txt
jupyter notebook notebooks/Basic_Region_Analysis.ipynb

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MagesNRoses/MetaSymmetry-Collatz/blob/main/notebooks/Basic_Region_Analysis.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Hallazgos Preliminares
En 1000 trayectorias analizadas (n=1 a 1000):
- Trayectorias con >30% pasos en **ABC**: 37% más rápidas
- Región B aparece en 92% de trayectorias largas