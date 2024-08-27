FROM python:3.10-alpine
WORKDIR app/
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip3 install -r requirements.txt
CMD ["sh", "-c", "python3 main.py"]



