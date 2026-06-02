# AWS ECS Flask CI/CD Project

A production-style DevOps project deploying a Flask application using Docker, Amazon ECR, Amazon ECS Fargate, Application Load Balancer, and GitHub Actions CI/CD.

## Architecture

Developer → GitHub → GitHub Actions → Docker Build → Amazon ECR → Amazon ECS Fargate → Application Load Balancer → Users

## Tech Stack

- Python Flask
- Docker
- Gunicorn
- GitHub Actions
- Amazon ECR
- Amazon ECS Fargate
- Application Load Balancer
- AWS IAM
- CloudWatch

## Local Development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
