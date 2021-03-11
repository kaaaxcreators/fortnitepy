FROM python:3.8
COPY BenBotAsyncNoAds /usr/src/app/BenBotAsyncNoAds
COPY requirements-linux.txt /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements-linux.txt
EXPOSE 8080
CMD [ "python", "fortnite.py" ]