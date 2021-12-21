# PyBuilder

`pybuilder` is python container builder for your python project. It makes it easy and uses best practices to build the container for your project.

## What is required?

Just follow these conventions:

* create a dockerfile at root of your project as

```dockerfile docker
FROM pybuilder
CMD ["<yourscript.py>"]
```

* Keep your source code in `src` directory
* Create a `requirements.txt` file at root of your project
* Now just do docker build

```console
$docker build -t myproject .
```

## How did you build the pybuilder?

Use this command:

```console
$ docker build -t pybuilder:latest .
```
