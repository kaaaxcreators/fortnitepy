FROM python:3.8
WORKDIR /usr/src/app
COPY BenBotAsyncNoAds/ .
COPY requirements-linux.txt .
RUN pip install -r requirements-linux.txt
COPY . .
EXPOSE 8080
CMD [ "python", "fortnite.py" ]