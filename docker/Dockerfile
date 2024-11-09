FROM python:3.12.7-bookworm
ENV APP_DIR=/app
WORKDIR $APP_DIR
ENV POETRY_VERSION=1.8.4
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN curl -L https://deb.nodesource.com/setup_20.x | bash - && apt update -y \
    && apt install -y --no-install-recommends nodejs \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*
COPY ../src .
RUN chmod +x /app/entrypoint.sh \
    && mkdir -p ../volume/logs
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
RUN npm init --init-license -y
RUN npm install tailwindcss postcss-cli autoprefixer flowbite
ENTRYPOINT ["bash", "-e", "entrypoint.sh"]
