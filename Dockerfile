FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y libgtk2.0-dev && apt-get install ffmpeg libsm6 libxext6  -y

RUN git clone https://github.com/brain-facens/FieldVision-AI.git

RUN pip install --upgrade pip

COPY requirements.txt /app

COPY paddleocr/ /root/.paddleocr

RUN pip install -r /app/requirements.txt

RUN wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb
RUN dpkg -i libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb

# Set the PYTHONPATH to include PaddleOCR
ENV PYTHONPATH=/app/PaddleOCR

EXPOSE 8080

CMD ["python", "FieldVision-AI/src/field_vision_api/main.py"]