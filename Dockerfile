FROM python:3.11-slim

RUN apt-get update -qq \
    && apt-get -y install --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["python", "-m", "bot"]
