FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calculator.py ./

CMD ["python", "-c", "from calculator import add; print('Calculator image is working, 1+2=', add(1,2))"]
