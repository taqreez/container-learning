FROM tensorflow/tensorflow
ONBUILD WORKDIR /app
ONBUILD COPY requirements.txt ./
ONBUILD RUN python -m pip install -r requirements.txt
ONBUILD COPY src /app/
ENTRYPOINT [ "python" ]
