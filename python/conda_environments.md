# working with environments on conda

## update conda
- `conda update -n base conda`

environment name: mynewenv \
packages file: packages.txt

## creating a new environment

- `conda create -n mynewenv`
- `conda create -n mynewenv python=3.6`

### with yml
- `conda env create -f <env.yml>`

## activate environment
- `conda activate mynewenv`

## list conda environments
- `conda env list` 
- `conda info --envs` or `conda info -e`

## install packages from a text file
- `pip install -r packages.txt`

## remove an environment
- `conda remove --name mynewenv --all`
- `conda env remove --name mynewenv`

## deactivate environment
- `conda deactivate`