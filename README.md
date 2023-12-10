# Quora Questions Similarity Prediction flask app

## Overview

This project predicts the similarity between pairs of questions from the Quora dataset. It involves the development of a machine learning model, a web service exposing an API for predictions, and deployment using Docker and Kubernetes via Minikube.

## Problem Statement

Understanding the similarity between questions is a crucial task for various applications, including search engines, recommendation systems, and community moderation. Quora, being a question and answer platform, faces the challenge of identifying and managing similar questions effectively. This project addresses this problem by developing a machine learning model that predicts the similarity between pairs of questions.

## Dataset

The dataset used for this project is the Quora Question Pairs Dataset. It contains pairs of questions labeled as either duplicate or non-duplicate. The model is trained on this data to learn patterns and features that indicate similarity or dissimilarity between questions.

## Significance

Predicting question similarity has several real-world applications:

- **Enhanced User Experience:** Improved search functionality on platforms like Quora allows users to find relevant content more efficiently.
- **Content Moderation:** Identifying duplicate or highly similar questions aids in moderating and organizing the platform's content.
- **Recommendation Systems:** Similarity prediction can be a key component in recommendation engines, suggesting relevant questions or topics to users.

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
  docker build -t flask_image .
  docker run -p 5000:5000 flask_image

## 4. Deployment with Kubernetes
### Task
Write a Kubernetes deployment configuration for managing Docker containers.

Implementation Details
**File:** deployment.yaml
**Commands:** kubectl apply -f deployment.yaml

## Resources
**Docker:**
https://docs.docker.com/get-docker/
**Minikube:**
https://minikube.sigs.k8s.io/docs/start/
