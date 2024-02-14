FROM python:3.9

# Copy files to working directory
COPY . /app
WORKDIR /app

# Installing python dependencies
RUN pip install -r requirements.txt
RUN python main.py

# Expose port and start command
EXPOSE 3000
CMD [ "python", "app.py" ]
