FROM python:3.10
# Security: let us use non-root user to run the image
RUN groupadd -g 999 pyuser && \
    useradd -r -u 999 -g pyuser pyuser
# we do not byte code in container
ENV PYTHONDONTWRITEBYTECODE 1
# output needs to flushed asap
ENV PYTHONUNBUFFERED 1

ONBUILD COPY --chown=pyuser:pyuser requirements.txt /usr/app/
ONBUILD WORKDIR /usr/app
# use virtual env for build
ONBUILD RUN python -m venv ./venv
ENV PATH="/usr/app/venv/bin:$PATH"
# do not keep downloaded package in cache, just install
ONBUILD RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt
# copy your python source files
ONBUILD COPY --chown=pyuser:pyuser src ./
# Set venv first in path so that pip and python works from their
ONBUILD USER 999
# set python as entry point, then you can just pass you script to run
ONBUILD ENTRYPOINT [ "python" ]
