python -m pip install -U build setuptools twine
del dist

python -m build
python -m twine upload dist/*