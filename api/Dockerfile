FROM python:3.11-bullseye

# Directorio de trabajo
WORKDIR /app

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATA_DIR=/app/Datos
ENV FAISS_INDEX_DIR=/app/faiss_index


RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas-dev \
    libomp-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip wheel setuptools

RUN pip install --no-cache-dir "numpy<2.0" packaging faiss-cpu==1.7.4

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/faiss_index

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
