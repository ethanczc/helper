# working with environments on conda

environment name: mynewenv \
packages file: packages.txt

## creating a new environment

- `conda create -n mynewenv`
- `conda create -n mynewenv python=3.6`

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