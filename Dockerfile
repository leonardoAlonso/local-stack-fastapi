FROM python:3.12

# Set the working directory
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the current directory contents into the container at /code
COPY ./app /code/app

# Run app.py when the container launches

CMD ["fastapi", "run", "app/app.py", "--port", "8000"]
