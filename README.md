# Job Shifting Prediction
## Table of Contents
 * [Problem Description](#problem-description)
   * [Goals](#goals)
 * [Features Description](#features-description)
 * [Tech Stack and concepts](#tech-stack-and-concepts)
 * [Setup](#setup)
   * [Virtual Environment](#virtual-environment)
   * [Run Service Locally](#run-service-locally)
   * [Docker Container](#docker-container)
   * [Deploying to Cloud](#deploying-to-cloudheroku-docker-deployment)

## Problem Description

The problem we will study was held as a competition on Kaggle titled as [Employee Attrition](https://www.kaggle.com/datasets/patelprashant/employee-attrition).
The data was shared from IBA community.
The objective of the problem is to predict Employee Churn / Employee Attrition value and to understand which factors led to employee attrition.

![dismissal](https://res.cloudinary.com/people-matters/image/upload/fl_immutable_cache,w_624,h_351,q_auto,f_auto/v1571631482/1571631481.jpg)

### Goals
- Predict if employee leave the company
- Interpret model(s) such a way that illustrate which features affect employee decision

## Features Description

* **AGE**: Age of the employee

* **ATTRITION**: Target - Leaving the company (0=no, 1=yes)

* **BUSINESS TRAVEL**: How often travels on business purpose (1=No Travel, 2=Travel Frequently, 3=Travel Rarely)

* **DAILY RATE**: Salary level

* **DEPARTMENT**: In what department works (1=HR, 2=R&D, 3=Sales)

* **DISTANCE FROM HOME**: The distance from work to home

* **EDUCATION**: (1='Below College' 2='College' 3='Bachelor' 4='Master' 5='Doctor')

* **EDUCATION FIELD**: (1=HR, 2=LIFE SCIENCES, 3=MARKETING, 4=MEDICAL SCIENCES, 5=OTHERS, 6=TECHNICAL)

* **EMPLOYEE COUNT**: Numerical Value

* **EMPLOYEE NUMBER**: Employee ID

* **ENVIRONMENT**: Satisfaction with the environment (1 'Low' 2 'Medium' 3 'High' 4 'Very High')

* **GENDER**: (1=FEMALE, 2=MALE)

* **HOURLY RATE**: Hourly salary

* **JOB INVOLVEMENT**: Job involvement (1 'Low' 2 'Medium' 3 'High' 4 'Very High')

* **JOB LEVEL**: Level of job

* **JOB ROLE**: (1=HR REP, 2=HR, 3=LAB TECHNICIAN, 4=MANAGER, 5=MANAGING DIRECTOR, 6=RESEARCH DIRECTOR, 7=RESEARCH SCIENTIST, 8=SALES EXECUTIVE, 9=SALES REPRESENTATIVE)

* **JOB SATISFACTION**: Satisfaction with the job (1 'Low' 2 'Medium' 3 'High' 4 'Very High')

* **MARITAL STATUS**: (1=DIVORCED, 2=MARRIED, 3=SINGLE)

* **MONTHLY INCOME**: Monthly salary

* **MONTHLY RATE**: Monthly rate

* **NUMCOMPANIES WORKED**: No. of companies worked at

* **OVER 18**: (1=YES, 2=NO)

* **OVERTIME**: (1=NO, 2=YES)

* **PERCENT SALARY HIKE**: Percentage increase in salary

* **PERFORMANCE RATING**: Performance rating

* **RELATIONS SATISFACTION**: Relations satisfaction

* **STANDARD HOURS**: Standart hours

* **STOCK OPTIONS LEVEL**: Stock options (Higher the number, the more stock option an employee has)

* **TOTAL WORKING YEARS**: Total working years(Experience)

* **TRAINING TIMES LAST YEAR**: Hours spent on training

* **WORK LIFE BALANCE**: TIME SPENT BETWEEN WORK AND OUTSIDE

* **YEARS AT COMPANY**: Total number of years in the company

* **YEARS IN CURRENT ROLE**: Years in the current role

* **YEARS SINCE LAST PROMOTION**: Last promotion

* **YEARS WITH CURRENT MANAGER**: Years spent with current manager

## Tech Stack and concepts

- Python
- Scikit-learn
- Machine Learning Pipeline
- Flask
- Virtual environment
- Docker
- Heroku

## Setup

Clone the project repo and open it.

### Virtual Environment

If you want to reproduce results by running [notebook](notebooks/) or [`train.py`](src/train.py), 
you need to create a virtual environment and install the dependencies.
In case of `conda`(you feel free to choose any other tools (`pipenv`, `venv`, etc.)), just follow the steps below:
1. Open the terminal and choose the project directory.
2. Create new virtual environment by command `conda create -n test-env python=3.10`.
3. Activate this virtual environment with `conda activate test-env`.
4. Install all packages using `pip install -r requirements.txt`.

### Run service locally
To run the service locally in your environment, simply use the following commands:
- Windows
```bash
waitress-serve --listen=0.0.0.0:5050 predict:app
```
- Ubuntu
```bash
gunicorn predict:app --host=0.0.0.0 --port=5050
```

### Docker Container
Be sure that you have already installed the Docker, and it's running on your machine now.
1. Open the terminal and choose the project directory.
2. Build docker image from [`Dockerfile`](Dockerfile) using `docker build --no-cache -t predict-attrition .`.
With `-t` parameter we're specifying the tag name of our docker image. 
3. Now use `docker run -it -p 5050:5050 predict-attrition` command to launch the docker container with your app. 
Parameter `-p` is used to map the docker container port to our real machine port.

Also you can pull out an already built image from [Dockerhub](https://hub.docker.com/). 
1. Use this command `docker pull kibzikm/predict-attrition:latest` in this case.
2. Now use `docker run -it -p 5050:5050 kibzikm/predict-attrition` command to launch the docker container with your app.

### Deploying to Cloud(Heroku docker deployment)
Follow this steps to deploy the app to Heroku
1. Register on [Heroku](https://signup.heroku.com/) and install Heroku CLI.
2. Open the terminal in project of the app
3. Terminal: rung the `heroku login` command to log in to Heroku.
4. Terminal: login to Heroku container registry using `heroku container:login` command.
5. Terminal: create a new app in Heroku with the following command `heroku create predict-attrition-docker`.
6. Make small changes in [`Dockerfile`](Dockerfile): uncomment the last line and comment out the line above. 
Heroku automatically assigns porn number from the dynamic pool. So, there is no need to specify it manually.
7. Terminal: run the `heroku container:push web -a predict-attrition-docker` command to push docker image to Heroku.
8. Terminal: release the container using the command `heroku container:release web -a predict-attrition-docker`.
9. Launch your app by clicking on generated URL in 5th step. In our case the link - [Heroku app](https://predict-attrition-docker.herokuapp.com/).
10. Testing: change host parameter in 27 line to 'predict-attrition-docker.herokuapp.com' and run [Request sender](src/request_sender.py)