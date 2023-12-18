
# PyPlate `simple` - A tiny boilerplate for new Python projects

See <https://github.com/tollefj/pyplate>.

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
make run
```

## Directory Structure

```text
├── src/
│ ├── main.py
│ ├── args.py
│ ├── utils/
│ │ └── ...
│ ├── examples/
│ │ └── ...
```
