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