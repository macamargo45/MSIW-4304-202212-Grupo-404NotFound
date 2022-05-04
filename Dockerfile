# For more information, please refer to https://aka.ms/vscode-docker-python
FROM alpine:3.14

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install depencies 
#RUN apk add py3-pip && pip install --upgrade pip

WORKDIR /flaskr
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "src/application.py"]