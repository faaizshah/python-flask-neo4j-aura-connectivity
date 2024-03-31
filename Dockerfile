FROM python:3.8-slim


RUN useradd -r -s /bin/bash faaiz


ENV HOME /app

WORKDIR /app

ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R faaiz:faaiz /app
USER faaiz

ENV FLASK_ENV=production

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

ENV AWS_ACCESS_KEY_ID ${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY ${AWS_SECRET_ACCESS_KEY}
ENV AWS_DEFAULT_REGION ${AWS_DEFAULT_REGION}


ADD ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user

COPY . .
WORKDIR /app

EXPOSE 5052

# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:5052", "neo4j-app:app", "--workers=5"]