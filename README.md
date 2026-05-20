# SDS210 project

Project description.

## Setup

First, clone this repository and change the working directory into it:

```
git clone https://github.com/5North/sds210-project.git
cd sds210-project
```
### Api Key
>[!note]
>You need a [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) api key to download the wildfire data. You can get one for free from [there](https://firms.modaps.eosdis.nasa.gov/api/map_key). Be mindful of the api request limit.

Create an file named `.env` in the root folder of the project and replace `example_key` with your own api key:

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
conda create --name sds210-project --file environment.yml
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
  jupyterlab
  ```

**uv**

`uv run jupyterlab`

## Notebooks execution

## License
