#!/usr/bin/env bash
set -eux

virtualenv build/venv
set +u
source build/venv/bin/activate
set -u

build/venv/bin/python setup.py install
make -C docs html
build/venv/bin/python setup.py test

for p in python2.7 python3.4
do
  virtualenv build/venv-$p/ --python $p
  build/venv-$p/bin/pip install -U pip wheel
  build/venv-$p/bin/python setup.py bdist_wheel upload -s
done
build/venv/bin/python setup.py sdist upload -s
build/venv/bin/python setup.py upload_docs --upload-dir docs/build/html/
