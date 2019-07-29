FROM python:3.7

# copy files
COPY . /var/app/backend

# set dir to run commands
WORKDIR /var/app/backend

# Expose python port
EXPOSE 5000

# Install Python dependencies
RUN pip install -r ./requirements.txt

CMD [ "tail", "-f", "/var/logs/app.log" ]