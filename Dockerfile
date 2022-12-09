FROM python:3.11.0

WORKDIR /user/app
COPY requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY data/request.csv ./data/request.csv
COPY models/ ./models/
COPY src/employee_description.py ./src/employee_description.py
COPY predict.py ./

EXPOSE 5050
ENTRYPOINT ["gunicorn", "predict:app"]
#ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5050", "predict:app"]
