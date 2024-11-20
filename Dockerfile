FROM python:3.13 AS builder

WORKDIR /pets

ENV DATABASE_URL=postgresql://Moviedb_owner:V3IRwlMvcAn4@ep-broad-sky-a4u0t3cc.us-east-1.aws.neon.tech/Petadoption?sslmode=require

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

FROM python:3.13-alpine

WORKDIR /pets

COPY --from=builder /pets /pets

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]