# django-conoscerelinux


## How to contribute
### Prepare environment
This command will create virtualenv and install dependencies 
```shell
$ make init
```

If make is not available
```shell
$ python -m venv .venv
$ source .venv/bin/activate
(.venv)$ python -m pip install pip pip-tools
(.venv)$ python -m piptools sync
```

### Prepare django
If is the first time you prepare the environment
```shell
$ make secret-key
$ make migrate
```