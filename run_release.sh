rm -rf complot.egg* && pip install -e .
rm -rf dist && python setup.py sdist bdist_wheel && twine check dist/* && twine upload dist/*
