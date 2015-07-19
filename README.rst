sphinxcontrib-images
====================

sphinxcontrib-images (formerly `sphinxcontrib-fancybox
<https://pypi.python.org/pypi/sphinxcontrib-fancybox>`_).

Easy sphinx thumbnails (focused on HTML).

* `Documentation <https://pythonhosted.org/sphinxcontrib-images>`_,
* `Repository (GitHub) <https://github.com/spinus/sphinxcontrib-images/>`_,
* `PyPI <https://pypi.python.org/pypi/sphinxcontrib-images/>`_.
* `TravisCI <https://travis-ci.org/spinus/sphinxcontrib-images>`

  .. image:: https://travis-ci.org/spinus/sphinxcontrib-images.svg?branch=master
      :target: https://travis-ci.org/spinus/sphinxcontrib-images

Features
--------

* Show thumbnails instead of full size images inside documentation (HTML).
* Ability to zoom/enlarge picture using LightBox2 (HTML).
* Ability to group pictures
* Download remote pictures and keep it in cache (if requested)
* Support for other formats (latex, epub, ... - fallback to image directive)
* Easy to extend (add own backend in only few lines of code)
  * Add other HTML "preview" solution than LightBox2
  * Add better support to non-HTML outputs
  * Preprocess images

TODO
^^^^

* Make proper thumbnails (scale down images)

How to install?
---------------

Instalation through pip: ::

    pip install sphinxcontrib-images

or through the GitHub: ::

    pip install git+https://github.com/spinus/sphinxcontrib-images

Next, you have to add extension to ``conf.py`` in your sphinx project. ::

    extensions = [
              …
              'sphinxcontrib.images',
              …
              ]


How to use it?
--------------

Example: ::

    .. thumbnail:: picture.png


You can also override default ``image`` directive provided by sphinx.
Check the documentation for all configuration options.


Questions and suggestions
-------------------------

If you have any suggstions, patches, problems - please use
`GitHub Issues <https://github.com/spinus/sphinxcontrib-images/issues>`_.
