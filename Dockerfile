FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend /app

CMD ["gunicorn", "avardict.wsgi:application", "--bind", "0.0.0.0:8000"]