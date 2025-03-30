FROM python:3.13.2-bookworm

WORKDIR /code

COPY . /code/

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# CMD ["fastapi", "dev", "--host", "0.0.0.0", "app/main.py"]

CMD [ "top", "-b" ]