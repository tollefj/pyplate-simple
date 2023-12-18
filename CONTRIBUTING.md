# Contributing to My Python Project Template

Thank you for your interest in contributing to this project! Here are some guidelines to help you get started.

## Reporting Issues

Please open a new issue on the GitHub repository if you encounter any problems or have suggestions for improvements.

## Submitting a Pull Request

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear, concise commit messages.
4. Open a pull request and describe the changes you've made and why they're necessary.
5. Address any feedback or requested changes from the maintainers.

## Code Style

This project uses [Black](https://github.com/psf/black) for code formatting and [isort](https://github.com/pycqa/isort) for import sorting. Please ensure your changes adhere to these styles by running the following commands before submitting a pull request:

```bash
pip install black isort
black .
isort .
```

We also use flake8 for linting. Install flake8 and run it to check for any issues:

```bash
pip install flake8
flake8
```

## Testing
Please include tests for any new features or bug fixes. Tests should be added to the tests/ directory and follow the existing structure.

Run tests using the following command:

```bash
python -m unittest discover tests
```

## Documentation

Update the documentation as needed, ensuring that it remains clear and up-to-date.
