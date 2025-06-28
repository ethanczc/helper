# Python venv
Creating a virtual environment. Save the venv folder in the project folder. Good way to wrap everything into 1 project folder.

## Virtual envs
Create a virtual env named .venv \
`python -m venv .venv` 

Activate it\
`source .venv/bin/activate`

Deactivate it\
`deactivate`

Using python from project folder\
`.venv/bin/python app.py`

## Pip requirements
Export pip packages into a requirements file.\
`pip freeze > requirements.txt`

Import pip packages from a requirements file.\
`pip install -r requirements.txt`