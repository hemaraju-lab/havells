# havells

# havells
This is specific to Assesement delivery
In this readme, I will outline the steps I took to deploy a Python application using Minikube, a local Kubernetes cluster for development and testing purposes. Since I do not have access to create an EKS (Amazon Elastic Kubernetes Service) or AKS (Azure Kubernetes Service) cluster, I am using Minikube on my local machine to showcase the process in detail.

Created Python Application: I created a simple Python application in a file named myapp.py that generated logs.

Created Dockerfile for Python Application: I created a Dockerfile that built a Docker image for my Python application. The Dockerfile included the necessary dependencies and configurations for my application.

Built and Pushed Docker Image for Python Application: I built the Docker image for my Python application using the Dockerfile, and pushed it to a private Docker registry, such as Docker Hub, using Docker commands like docker build and docker push. I also created a Docker Hub secret in my Kubernetes cluster to authenticate the Docker image pull during deployment.

Created Fluentd Docker Image: I created a separate Docker image for Fluentd, a log collector, using a Fluentd Dockerfile that included the necessary Fluentd configurations and plugins for log collection and forwarding.

Built and Pushed Fluentd Docker Image: I built the Docker image for Fluentd using the Fluentd Dockerfile, and pushed it to a private Docker registry, such as Docker Hub, using Docker commands like docker build and docker push.

Deployed Python Application to Minikube: I deployed the Docker image of my Python application to Minikube, which is a local Kubernetes cluster for development and testing purposes. I used a Deployment resource in Kubernetes to manage the deployment of my application, specifying the Docker image, container ports, and other configurations. The deployment.yaml and service.yaml files for my application are available in the folder python-app in the repository.

Configured Fluentd for Log Collection: I configured Fluentd as a log collector to collect logs from the logs generated by my Python application. The Fluentd configuration included a <source> block that specified the path to the log file, log format, and tag for the logs, and a <match> block that specified the destination for the logs, which was a Fluentd forwarder.



In summary, I built and deployed a Python application on Minikube, created and pushed separate Docker images for my Python application and Fluentd, configured Fluentd as a log collector to collect logs from my application, 

i have not updated updated the Fluentd configuration to send logs to Elasticsearch or any other tools for storage and analysis. 

if you guys need this to be sending to elasticsearch or any storage , i will implement it accordingly 
