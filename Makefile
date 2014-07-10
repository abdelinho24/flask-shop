.PHONY: docs release clean build

clean:
rm -rf env htmlcov

build:
virtualenv env && source env/bin/activate && \
pip install -r requirements.txt

test: clean build
source env/bin/activate && \
coverage run --source=bull setup.py test && \
coverage html && \
coverage report
