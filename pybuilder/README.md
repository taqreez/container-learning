# PyBuilder

`pybuilder` is python container builder for your python project. It  makes it easy to build a container for your project.

## What is required?

Just follow these conventions:

* create a dockerfile at root of your project as

```Dockerfile docker
FROM pubuilder
CMD ["<yourscript.py>"]
```

* Keep your source code in `src` directory
* Create a `requirements.txt` file at root of your project

## How did you build the pybuilder?

Use this command:

```console
$ docker build -t pybuilder:latest .
```
