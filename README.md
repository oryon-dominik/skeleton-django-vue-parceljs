# README

## installation

1. clone the repo, delete .git, create a new git repo
2. setup name & description in `pyproject.toml`
3. `poetry install`
4. Activate the env created by poetry, e.g `poetry shell`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. Install the frontend `cd frontend && yarn install`
8. start the vue-development-sever with `yarn serve` in `.\frontend` on `localhost:1234`
9. happy frontend-coding
10. deploy the frontend files to the static-folder `assets/vue` with `yarn build` in `.\frontend`
11. start the django-server on `localhost:8000` with `python manage.py runserver`
12. happy-coding

## notebooks

to work with notebooks, set
`DJANGO_ALLOW_ASYNC_UNSAFE=true` in your `.env`

## production

fix the settings in settings.py, don't use the `.env`
