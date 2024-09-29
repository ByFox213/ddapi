python -3.11 -m pip install -U build setuptools twine
rm -rf dist

python -3.11 -m build
python -3.11 -m twine upload dist/*