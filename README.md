# Quora Questions Similarity Prediction flask app

## Overview

This project aims to predict the similarity between pairs of questions from the Quora dataset. It involves the development of a machine learning model, a web service exposing an API for predictions, and deployment using Docker and Kubernetes via minikube.

## Table of Contents

1. [AI Model Development](#1-ai-model-development)
2. [Web Service Creation](#2-web-service-creation)
3. [Containerization with Docker](#3-containerization-with-docker)
4. [Deployment with Kubernetes](#4-deployment-with-kubernetes)
5. [Resources](#5-Resources)

## 1. AI Model Development

### Task
Develop a machine learning model for predicting question similarity.

### Implementation Details
- **File:** `Custom AI Model Deployment Pipeline.ipynb`
- **Dependencies:** TensorFlow, Pandas, NLTK
- **Dataset:** Quora Question Pairs Dataset
- **Model:** Siamese Neural Network(quora_question_similarity_model.h5)
- **Training Process:** Jupyter notebook (https://github.com/DattatrayBodake25/python-flask-app-kubernetes/blob/main/Custom%20AI%20Model%20Deployment%20Pipeline.ipynb)

## 2. Web Service Creation

### Task
Create a web service in Python using Flask, exposing an API for predictions.

### Implementation Details
- **File:** `model2.py`
- **Dependencies:** Flask, Flask-SQLAlchemy, NLTK, TensorFlow
- **Database:** MySQL
- **API Endpoint:** `/predict`
- **Authentication:** Basic authentication implemented

## 3. Containerization with Docker

### Task
Containerize the AI model and web service using Docker.

### Implementation Details
- **Dockerfile:** `Dockerfile`
- **Commands:**
  docker build -t quora-similarity-app .
  docker run -p 5000:5000 quora-similarity-app

## 4. Deployment with Kubernetes
### Task
Write a Kubernetes deployment configuration for managing Docker containers.

Implementation Details
File: deployment.yaml
Commands: kubectl apply -f deployment.yaml

## Resources
Docker:
https://docs.docker.com/get-docker/
Minikube:
https://minikube.sigs.k8s.io/docs/start/
