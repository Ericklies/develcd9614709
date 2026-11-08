# EDA - Predict Future Sales

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Análisis exploratorio del dataset de la competencia [Predict Future Sales de Kaggle](https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales/data). El objetivo final es predecir unidades mensuales por par tienda-producto para noviembre de 2015.

## Preparación

Requiere Python 3.11 y una cuenta de Kaggle con acceso a la competencia.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Configura KaggleHub con tus credenciales en el equipo local; no las guardes en el repositorio. Abre y ejecuta `notebooks/00_kagglehub_download.ipynb` para descargar los cinco CSV a `data/raw/`. Los datos están excluidos por `.gitignore`.

## Análisis

Abre `notebooks/01_exploratory_data_analysis.ipynb` en VS Code o Jupyter y ejecuta las celdas en orden. El notebook genera las figuras en `reports/figures/`. Si los CSV no están presentes, informa que los resultados no se calcularon y no inventa cifras.

La guía de colaboración está en `docs/pull_screenshots.md`; el procedimiento ampliado está en `docs/procedimiento_actualizacion_repositorio.docx`.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         eda_predict_future_sales and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── eda_predict_future_sales   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes eda_predict_future_sales a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

