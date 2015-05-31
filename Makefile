
all: clean
	python setup.py build sdist

clean:
	rm -rf ./build ./dist ./django_twinder.egg-info/
	find . -type f -iname '*.pyc' | xargs rm -f

.PHONY: all clean
