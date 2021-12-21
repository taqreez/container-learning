FROM python:3.10-slim as builder
# we do not need byte code in container
ENV PYTHONDONTWRITEBYTECODE 1
# output needs to flushed asap
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/app/
WORKDIR /usr/app
# use virtual env for build
RUN python -m venv ./venv
ENV PATH="/usr/app/venv/bin:$PATH"
# do not keep downloaded package in cache, just install
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

# Create slim image for app
FROM python:3.10-slim
# Security: let us use non-root user to run the image
RUN groupadd -g 999 pyuser && \
    useradd -r -u 999 -g pyuser pyuser
# we do not need byte code in container
ENV PYTHONDONTWRITEBYTECODE 1
# output needs to flushed asap
ENV PYTHONUNBUFFERED 1
# copy venv that has required packages
COPY --from=builder --chown=pyuser:pyuser /usr/app/venv /usr/app/venv
WORKDIR /usr/app
# copy your python source files
COPY --chown=pyuser:pyuser src ./
# Set venv first in path so that pip and python works from their
ENV PATH="/usr/app/venv/bin:$PATH"
USER 999
# set python as entry point, then you can just pass you script to run
ENTRYPOINT [ "python" ]
