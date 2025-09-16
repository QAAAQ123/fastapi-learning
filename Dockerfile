FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
EXPOSE 7000
COPY ./ /app
CMD ["python","planner/main.py"]