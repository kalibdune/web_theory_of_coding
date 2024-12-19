FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
RUN pytest tests.py
CMD ["python3", "manage.py", "collectstatic"]
