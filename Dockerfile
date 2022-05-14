# For more information, please refer to https://aka.ms/vscode-docker-python
FROM 224678269500.dkr.ecr.us-east-1.amazonaws.com/alpine

RUN apk add py3-pip \
    && pip install --upgrade pip

WORKDIR /app
COPY . /app/
    
RUN pip install -r src/requirements.txt

RUN cd src/; python3 -m unittest -v

EXPOSE 5000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "application:application"]
CMD ["python3", "src/application.py"]