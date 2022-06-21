FROM python:3.9.7
WORKDIR /M/API
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:m", "--host", "0.0.0.0", "--port", "8000"]

