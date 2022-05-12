# For more information, please refer to https://aka.ms/vscode-docker-python HHFM
FROM public.ecr.aws/docker/library/alpine:3.14

# install depencies 
RUN apk add py3-pip && pip install --upgrade pip

WORKDIR /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "src/application.py"]