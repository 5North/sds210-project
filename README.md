# SDS210 project

This project is part of the SDS210 course at University of Zürich. It aims to investigate which countries in the world have been more affected by wildfires in the last 14 days (as of 02-05-2026) in terms of percentage of wildfire-affected area (relative to total area) and total wildfire-affected area.

## Project structure

```
sds210-project/
├── data                        # where downloaded and processed data is saved. Not tracked by git.
    ├── raw
    └── processed
├── .env.example                # example env file for FIRMS api key
├── environment.yml             # conda environment config file
├── .gitignore          
├── LICENSE                     # repo license
├── notebooks/
│   ├── data_download.ipynb
│   ├── data_processing.ipynb
│   └── visualization.ipynb
├── outputs                     # created maps are saved there. Not tracked by git.
├── pyproject.toml              # python project config file
├── README.md
├── src/                        # dir for custom modules
│   └── request_handler.py      # module for handling requests status codes
└── uv.lock                     # uv lock file
```

## Setup

First, clone this repository and change the working directory into it:

```
git clone https://github.com/5North/sds210-project.git
cd sds210-project
```

### Api Key

> [!important]
> You need a [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) api key to download the wildfire data. You can get one for free from [there](https://firms.modaps.eosdis.nasa.gov/api/map_key). Be mindful of the api request limit.

Create a file named `.env` in the root folder of the project and replace `example_key` with your own api key:

```
FIRM_API_KEY="example_key"
```

`.env.example` is provided as an example for the `.env` file.

### Python Environment

Setup your environment. You can use either [conda](https://conda.org/) or [uv](https://docs.astral.sh/uv/).

#### Conda

##### Installation

You can find instructions to install conda [here](https://docs.conda.io/en/latest/#install-svg-version-1-1-width-1-0em-height-1-0em-class-sd-octicon-sd-octicon-download-sd-text-primary-viewbox-0-0-16-16-aria-hidden-true-path-d-m2-75-14a1-75-1-75-0-0-1-1-12-25v-2-5a-75-75-0-0-1-1-5-0v2-5c0-138-112-25-25-25h10-5a-25-25-0-0-0-25-25v-2-5a-75-75-0-0-1-1-5-0v2-5a1-75-1-75-0-0-1-13-25-14z-path-path-d-m7-25-7-689v2a-75-75-0-0-1-1-5-0v5-689l1-97-1-969a-749-749-0-1-1-1-06-1-06l-3-25-3-25a-749-749-0-0-1-1-06-0l4-22-6-78a-749-749-0-1-1-1-06-1-06l1-97-1-969z-path-svg).

##### Environment setup

You can then setup the conda environment by running:

```
conda env create --name sds210-project --file environment.yml
```

#### uv

##### Installation

You can find instructions to install uv [here](https://docs.astral.sh/uv/getting-started/installation/).

##### Environment setup

You can then setup the virtual environment by running:

```
uv sync
```

### Start the Jupyter Server

> [!NOTE]
> If you want to use an IDE instead of the jupyterlab interface, you already probably know what to do.

Run the following commands to start the jupyterlab server. The jupyter interface will open in a new browser tab.

**Conda**

```
conda activate sds210-project
jupyter-lab
```

**uv**

`uv run jupyter-lab`

## Notebooks execution

Run the notebooks in the following order:

1. `data_download.ipynb`
2. `data_processing.ipynb`
3. `data_visualization.ipynb`

> [!note]
> The notebooks already default to the date used in the project for data donwload and processing. If you want to visualize the last data available, use `DATE = datetime.datetime.now()` instead of `DATE = datetime.datetime.fromisoformat("2026-05-02")` in the first cell of the `data_download` notebook. You would also need to assign the variable `DATE` in the first cell of `data_processing.ipynb` to the date of the VIIRS file you want to load and process.

## Data sources

### Wildfire data

From [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/). Released under the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/).

NASA VIIRS Land Science Team. (2020). _VIIRS (S-NPP) I Band 375 m Active Fire Product NRT (Vector data)_ [Data set]. NASA LANCE MODIS at the MODAPS. https://doi.org/10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002

### Countries boundaries vector data

From [geoboundaries](https://geoboundaries.org). Released under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/) / Modified: geometries have been simplified using `geopandas.simplify_coverage()`, merged with Wordlbank Surface Area dataset.

Runfola, D. et al. (2020) geoBoundaries: A global database of political administrative boundaries. PLoS ONE 15(4): e0231866. https://doi.org/10.1371/journal.pone.0231866

### Countries surface area

From [World Bank](https://data360.worldbank.org/en/indicator/WB_WDI_AG_SRF_TOTL_K2?view=map&mapType=country). Released under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/) / Modified: merged with the countries boundaries dataset, computed new attribute wildfire percentage area from country area and FIRMS data.

FAO electronic files and web site, Food and Agriculture Organization of the United Nations (FAO)
