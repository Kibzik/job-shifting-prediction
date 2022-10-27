# Job Shifting Prediction
## Table of Contents
 * [Problem Description](#problem-description)
   * [Goals](#goals)
 * [Features Description](#features-description)
 * [Tech Stack and concepts](#tech-stack-and-concepts)
 * [Setup](#setup)
   * [Virtual Environment](#virtual-environment)
   * [Docker Container](#docker-container)
   * [Deploying to Cloud](#deploying-to-cloud)

## Problem Description

The problem we will study was held as a competition on Kaggle titled as [HR Analytics: Job Change of Data Scientists](https://www.kaggle.com/datasets/arashnic/hr-analytics-job-change-of-data-scientists). 
A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which conduct by the company.
Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training or looking for a new
employment because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates.

<p align="center">
    <img src="https://storage.googleapis.com/kaggle-datasets-images/1019790/1719283/f7505a4e4d6e9c141aa2196a7a77ddf7/dataset-cover.png?t=2020-12-07-00-41-54" width="500" />
</p>

<br>

### Goals
- Predict the probability of a candidate will work for the company
- Interpret model(s) such a way that illustrate which features affect candidate decision

## Features Description

* enrollee_id : Unique ID for candidate

* city: City code

* city_ development _index : Developement index of the city (scaled)

* gender: Gender of candidate

* relevent_experience: Relevant experience of candidate

* enrolled_university: Type of University course enrolled if any

* education_level: Education level of candidate

* major_discipline :Education major discipline of candidate

* experience: Candidate total experience in years

* company_size: No of employees in current employer's company

* company_type : Type of current employer

* lastnewjob: Difference in years between previous job and current job

* training_hours: training hours completed

* target: 0 – Not looking for job change, 1 – Looking for a job change

## Tech Stack and concepts

- Python
- Scikit-learn
- Machine Learning Pipeline
- Docker
- Streamlit

## Setup

- Clone the project repo and open it.

### Virtual Environment

- Create a virtual environment for the project using

  ```bash
  pipenv shell
  ```

- Install required packages using

  ```bash
  pipenv install
  ```

### Docker Container

- Build the docker image using

  ```bash
  sudo docker build -t mba_placement .
  ```

- Run the docker container using

  ```bash
  sudo docker run -p 5000:5000 mba_placement
  ```

- Open the URL http://localhost:5000/ to run and test the app.

### Deploying to Cloud

- Open the [Deploy an app](https://share.streamlit.io/deploy) page of Streamlit.
- Enter the GitHub repository details in which the streamlit_app.py file and model binaries are stored.
- Click on Deploy button.
- Open the URL https://share.streamlit.io/aniketsharma00411/mba_placement_prediction/main to run and test the app.