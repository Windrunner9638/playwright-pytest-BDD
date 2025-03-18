FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
LABEL authors="artemogai"

RUN apt update && apt install -y openjdk-17-jdk openjdk-17-jre wget
RUN wget https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz && tar -zxvf allure-2.30.0.tgz -C /opt/ && ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure