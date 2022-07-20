FROM python:3.10-slim-bullseye
WORKDIR /code/
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
