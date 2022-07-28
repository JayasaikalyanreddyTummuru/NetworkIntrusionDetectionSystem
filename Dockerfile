FROM python:3.8-slim
WORKDIR /app
COPY . . 
RUN pip install -r req.txt
EXPOSE 5000
ENV NAME OpentoAll
CMD ["python","app.py"]