# 1. Corregir división por cero
sed -i "s/x = j \/ total_ops/x = j \/ total_ops if total_ops > 0 else 0.0/" src/collatz_functions.py

# 2. Actualizar paleta de colores
curl -o notebooks/Basic_Region_Analysis.ipynb https://gist.githubusercontent.com/assistant/collatz-visual/raw/main/updated_notebook.ipynb

# 3. Añadir nuevo notebook de validación estadística
curl -o notebooks/Statistical_Validation.ipynb https://gist.githubusercontent.com/assistant/collatz-stats/raw/main/statistical_validation.ipynb

# 4. Actualizar README
echo -e "[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MagesNRoses/MetaSymmetry-Collatz/blob/main/notebooks/Basic_Region_Analysis.ipynb)\n$(cat README.md)" > README.md