FROM python:3.8-slim
WORKDIR /code
RUN python3 -m pip install --upgrade pip
ENV FLASK_APP=app.py
COPY ./requirements.txt .
RUN python3 -m pip install --root-user-action=ignore --no-cache-dir --upgratde -r requirements.txt
COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]