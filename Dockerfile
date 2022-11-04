FROM python:3.8.12-slim

WORKDIR /user/app
COPY requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY data/request.csv ./data/request.csv
COPY models/ ./models/
COPY src/employee_description.py ./src/employee_description.py
COPY predict.py ./

EXPOSE 5050
#ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5050", "predict:app"]
ENTRYPOINT ["gunicorn", "predict:app"]