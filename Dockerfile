FROM python:3.7-alpine

WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -U setuptools
RUN python -m pip install -r requirements.txt
RUN pip install -r requirements.txt

EXPOSE 7860
COPY . .
CMD ["python", "app.py"]
