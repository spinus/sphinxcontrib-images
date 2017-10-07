#!/usr/bin/env nix-shell
#! nix-shell -i bash --pure -p python27 python34 python35 python36 python27Packages.virtualenv python34Packages.virtualenv python35Packages.virtualenv python36Packages.virtualenv pypy pypyPackages.virtualenv glibcLocales glibc
set -eux
export LANG=C.UTF-8

virtualenv build/venv
set +u
source build/venv/bin/activate
set -u

build/venv/bin/python setup.py install
build/venv/bin/pip install sphinx-rtd-theme
make -C docs html
build/venv/bin/python setup.py test

for p in python2.7 python3.4 python3.5 python3.6
do
  virtualenv build/venv-$p/ --python $p
  build/venv-$p/bin/pip install -U pip wheel
  build/venv-$p/bin/python setup.py bdist_wheel upload -s
done
echo "Upload files?..."
read OK
build/venv/bin/python setup.py sdist upload -s
build/venv/bin/python setup.py upload_docs --upload-dir docs/build/html/
