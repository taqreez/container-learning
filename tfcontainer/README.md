# Run Tensorflow Regression model with Tensorflow container

This sample project demostrats a quick and easy way to train a model in base tensorflow container without creaing a new container.

## How to run train modle in container

**Command:**

`docker run -t --rm -v /c/container-learning/pybuilder:/usr/src/myapp -w /usr/src/myapp tensorflow/tensorflow sh -c /usr/src/myapp/run.sh`

* We use -v option to mount windows app directory `/c/container-learning/pybuilder` to `/usr/src/myapp` path in conatiner
* Use -w to define working working in the container

## fuel.py

Defines a deep neural network regression model for fuel efficiency.

## run.sh

This script install pandas package in conatiner and then run `fuel.py`
