FROM python:3.14-alpine AS production

WORKDIR /srv

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    UV_NO_DEV=1

ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]

CMD [ "uv", "run", "gunicorn", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "agnescafe.core.asgi:application" ]

RUN apk add --no-cache dumb-init uv

COPY ./pyproject.toml ./README.md ./uv.lock /srv/

RUN uv sync

COPY ./src /srv/src

RUN uv run django collectstatic --noinput
