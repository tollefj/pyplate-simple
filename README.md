
# PyPlate - A boilerplate for new Python projects

This template serves as a starting point for Python projects, including essential utilities, directory structure, and example code for various repetitive tasks.

# To build your own project

Simply click on the green "Use this template" button on the top of this page.

... Or, if you prefer the manual way, create a new repo on GitHub, then run the following commands:

```bash
git clone git@github.com:tollefj/pyplate.git MYPROJECT

cd MYPROJECT

git remote remove origin
git remote add origin <your repo url>
git push --set-upstream origin main
```

# Running stuff

```bash
make setup
# optional tasks: {geo/graphs/image/ml/nlp/web}
make install-req TASK=ml
# do code changes :-)
make run
# did you write tests?
make test
```

## Typing, linting and formatting

```bash
# typing
make mypy
# flake8
make lint
# format the code using `black` and `isort`
make format
# dry run:
make format-check
```

## Directory Structure

```text
├── docs/
│ └── ...
│
├── requirements/
│ ├── requirements.txt
│ ├── requirements_ml.txt
│ ├── requirements_web.txt
│ └── ...
│
├── src/
│ ├── main.py
│ ├── utils/
│ │ └── ...
│
└── tests/
│ └── ...
```
