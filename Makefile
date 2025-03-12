




PHONY: check
check:
	echo '1234'
	black .
	isort .
	flake8 .