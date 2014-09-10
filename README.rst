sphinxcontrib-images
====================

sphinxcontrib-images (formerly `sphinxcontrib-fancybox
<https://pypi.python.org/pypi/sphinxcontrib-fancybox>`_).

* `Documentation <https://pythonhosted.org/sphinxcontrib-images>`_,
* `Repository (GitHub) <https://github.com/spinus/sphinxcontrib-images/>`_,
* `PyPI <https://pypi.python.org/pypi/sphinxcontrib-images/>`_.

Features
--------

* Show thumbnails instead of full size images inside documentation.
* Ability to zoom/enlarge picture using LightBox2 (or any other backend)
* Ability to group pictures
* Download remote pictures (if requested)

TODO
^^^^

* Make proper thumbnails (scale down images)
* Make support for other formats (latex, epub, etc)

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
