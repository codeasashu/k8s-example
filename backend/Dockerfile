FROM python:3

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python", "-m", "flask", "run"]
CMD ["flask","run", "--host=0.0.0.0"]
