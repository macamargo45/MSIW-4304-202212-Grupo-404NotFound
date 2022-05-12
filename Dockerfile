# For more information, please refer to https://aka.ms/vscode-docker-python HHFM
FROM 824166451111.dkr.ecr.us-east-1.amazonaws.com/python_app

# install depencies 
RUN apk add py3-pip && pip install --upgrade pip

WORKDIR /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt --ignore-installed pyOpenSSL

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "src/application.py"]