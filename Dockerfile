FROM python:3.11-slim
WORKDIR /app 
RUN pip install poetry 
COPY pyproject.toml poetry.lock* /app/ 
RUN poetry config virtualenvs.create false 
RUN poetry install --no-dev --no-interaction --no-ansi
COPY . /app 
RUN python manage.py collectstatic --noinput
EXPOSE 80 
CMD ["gunicorn", "-c", "gunicorn_config.py", "core.wsgi:application"]
