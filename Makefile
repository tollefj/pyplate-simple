export PYTHONPATH := $(PWD)

.PHONY: run test mypy lint format check-format install-req

run:
	python src/main.py

mypy:
	mypy src --config-file mypy.ini

setup:
	pip install -r requirements.txt

new:
	@read -p "Enter your repository URL: " repository_url; \
	git remote remove origin && \
	git remote add origin $$repository_url && \
	git push --set-upstream origin main