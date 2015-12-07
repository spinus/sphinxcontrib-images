sphinxcontrib-images
====================

sphinxcontrib-images (formerly `sphinxcontrib-fancybox
<https://pypi.python.org/pypi/sphinxcontrib-fancybox>`_).

How to install?
---------------

::

    pip install sphinxcontrib-images

Add extension to ``conf.py`` in your sphinx project. ::

    extensions = [
              …
              'sphinxcontrib.images',
              …
              ]

How to configure?
-----------------

You can configure behaviour using a dictionary with options placed in ``conf.py``::

    images_config = {
        …
    }

All available options with comments:

:backend: (default: 'LightBox2')

    ``string`` or ``callable``

    If ``string`` it has to be the name of the
    ``entrypoint`` registered in the
    ``sphinxcontrib.images.backend`` group (look at the source
    of ``setup.py`` in this project).

    Callable can be a function or a class which
    returns an instance of a backend to render images.
    The first argument is Sphinx's app instance. Go to
    LightBox2 backend to see how to implement that.

    Each backend should implement rendering ``image_node`` on specific outputs.
    If methods are not implemented, default ``image`` directive is a fallback.

    By default ``LightBox2`` backends natively support only HTML (other
    outputs are supported by fallback-image-directive).

:override_image_directive: (default: ``False``)

    ``True`` or ``False``. It overrides the default Sphinx ``image`` directive
    with the ``thumbnail`` directive provided by this extension.

:cache_path: (default :``_images``)

    Path, where to keep downloaded images. Relative to
    source (actually relative to ``conf.py``) directory or absolute path.

:requests_kwargs: (default: ``{}``)

    Remote images are downloaded by `requests
    <https://pypi.python.org/pypi/requests>`_.  This
    ``dict`` keeps the keyword arguments that will be
    passed to the ``get`` method.

:default_image_width: (default: ``100%``)

    Default width of an image. Backend can use this
    setting to set width properly.

:default_image_height: (default: ``auto``)

    Default height of an image. Backend can use this
    setting to set width properly.

:default_group: (default: ``None``)

    This setting sets the default group for images without
    a defined group.  If ``None`` each image is placed in a
    separate group, which means that images are not
    grouped by default. Otherwise you can set a group
    name like ``default`` to group all ungrouped images
    together.

:default_show_title: (default: ``False``)

    Defines whether a caption below the picture should be visible or not.

    .. warning::

        Currently this options does not work, I have no idea how to
        enable this feature in lightbox2. If you have any idea please do
        a pull request.


:download: (default: ``True``)

    Download remote images.



Thumbnail directive
-------------------

You can use it like::

    .. thumbnail:: path/to/image.jpg

or::

    .. thumbnail:: http://remote/image.jpg

You can pass options like regular Sphinxs' directives::

    .. thumbnail:: http://remote/image.jpg
        :download: true

All available arguments:

:group:

    If you set the same group for different images the backend
    can *group* them.

:class:

    This can be used by the backend to apply some style.

    The straightforward use case is to define HTML classes here (LightBox2
    backend puts these classes on outer ``a`` element, not inner ``img``).

:width:

    Backend can use this option to set the width of the
    image. This overrides ``default_image_width`` from configuration.

    Values like:

    * percentage ``100%``
    * length with unit ``100px``
    * ``auto``

    are accepted.

:height:

    Backend can use this option to set the height of the
    image. This overrides ``default_image_height`` from configuration.

    Values like:

    * length with unit: ``100px``
    * ``auto``

    are accepted.

:alt:

    If image cannot be displayed, this text will be shown.

:download:

    This overrides ``download`` from configuration. You can set
    for particular image to download it or not. Works only for remote images.

:title:

    * If you do not define it, ``default_show_title`` configuration option will
    be used (it will define whether to show title or not).

    * If you define this option but leave it empty, the content of the
    directive will be used as the title::

        .. thumbnail:: image.jpg
            :title:

            This will be a title

    * If you define this option as text, it will be used as title::

        .. thumbnail:: image.jpg
            :title: This is title

            This is description

    It's up to the backend, how this will be displayed.

    Currently I have a problem with LightBox2 to make captions below thumbnails.
    If you have any idea how to solve it please write.

:align: (default: '')

    Align the picture.

    LightBox2 backend uses ``align-<left|center|right>`` Sphinx html classes.
    By default alignment is not used at all.

    Values like:

    * ``left``
    * ``center``
    * ``right``

    are accepted.

    .. note::

        You may want to wrap aligned element with::

            .. container:: clearfix

        to fix document flow.

:show_caption: (default: ``False``)

    Show the title as a caption below the image.

    .. warning::

        Enabling the caption nests the clickable image inside an HTML ``figure``
        which gets the class if defined.

        This mays break existing styles.

        To solve styles compatibility issues, you may use the *legacy_class* argument.

:legacy_class:

    Only applicable when *show_caption* is ``True``.

    The classese specified are added to the clickable image.

    The ``figure`` HTML element still gets the classes specified by the *class* argument.

Examples
--------

Local full-size image
^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: img.jpg

Remote images
-------------

remote image (http)
^^^^^^^^^^^^^^^^^^^

.. thumbnail:: http://upload.wikimedia.org/wikipedia/meta/0/08/Wikipedia-logo-v2_1x.png
    :download: false

remote image (https)
^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: https://upload.wikimedia.org/wikipedia/meta/0/08/Wikipedia-logo-v2_1x.png
    :download: false

remote image (download http)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The image should be downloaded (available from localhost)

.. thumbnail:: http://upload.wikimedia.org/wikipedia/meta/0/08/Wikipedia-logo-v2_1x.png
    :download: true

remote image (download https)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The image should be downloaded (available from localhost)

.. thumbnail:: https://upload.wikimedia.org/wikipedia/meta/0/08/Wikipedia-logo-v2_1x.png
    :download: true

image with non standard size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: img.jpg
    :width: 500px
    :height: 50px

image with additional class
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: img.jpg
    :class: warning


image with description
^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: img.jpg

    Description of the image with more magical.

image alternative text
^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: http://a/non_existing_image.png
    :alt: Cannot load this photo, but believe me it's nice.

image with caption
^^^^^^^^^^^^^^^^^^

.. thumbnail:: img.jpg
    :title:

    Some nice title to the picture

Group images
------------

.. thumbnail:: img.jpg
    :group: group1

.. thumbnail:: img.jpg
    :group: group1

.. thumbnail:: img.jpg
    :group: group1

.. thumbnail:: img.jpg
    :group: group1


Aligning
--------

.. container:: clearfix

   .. thumbnail:: img.jpg
      :align: left

.. container:: clearfix

   .. thumbnail:: img.jpg
      :align: center

.. container:: clearfix

   .. thumbnail:: img.jpg
      :align: right


Caption
-------

.. thumbnail:: img.jpg
   :title: Some nice title to the picture
   :show_caption: True



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

