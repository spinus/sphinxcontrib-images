Sphinx "fancybox" extension.

Fancybox
========

Fancybox is adaptation of `<http://fancybox.net/>`_ in version **1.3.4**.

Documentation: `<http://spinus.github.com/sphinxcontrib-fancybox/>`_

github: `<http://github.com/spinus/sphinxcontrib-fancybox/>`_

PYPI: `<http://pypi.python.org/pypi/sphinxcontrib-fancybox/>`_

Installation
------------

Instalation through pip: ::

    pip install sphinxcontrib-fancybox

or through github: ::

    git clone https://github.com/spinus/sphinxcontrib-fancybox
    cd sphinxcontrib-fancybox
    python setup.py install

Next, you have to add extension to `conf.py` in your sphinx project. ::

    extensions = [
              ...,
              'sphinxcontrib.fancybox',  
              ...]


Directives
----------

fancybox:
    
    Fancybox directive place a thumbnail of picture you selected, and add some
    `fancies`. If you click on image you get fullscreen box with that picture.

    Example: ::

        .. fancybox:: picture.png


    By default all images on one page are in the same group (you can navigate
    pressing `next` and `prev` buttons around this group).
    If you want to add picture to another group you have to set `group` 
    parameter, like: ::

        .. fancybox:: picture.png
            :group: group2


    You can change size of fancybox with 'width' and 'height' which are
    passed as you set it: ::

        .. fancybox:: picture.png
            :width: 100%
            :height: 2em


    You can add some description which will be rendered as `title` attribute::

        .. fancybox:: http://pictures.tld/picture.png

            Some description


    If you not set 'width' and 'height', defaults values are gathered from 
    `conf.py`. There are two parameters which you can adjust: ::

        fancybox_thumbnail_width
        fancybox_thumbnail_height


    Additionally you can set another css class with 'class' argument to 
    `fancybox` directive or set `fancybox_thumbnail_class` to add css class to 
    all `fancybox` directives.

    All fancybox JS config options you can pass as dict to `fancybox_config` in
    `conf.py` too.

    For examples please look to documentation conf.py.


TODO
----

* handling local files (not only remotes) (DONE)
* option to copying remote graphics as statics
* fallback for non html output (DONE)
* nested parsing fix
* JS should be handled only once, not on every image node
* width and height parameters (currently the thumbnail is set to 100x100px) (DONE)
* get default thumbnail size from config (DONE)
* generate thumbnails for big images 


Questions and suggestions
-------------------------

If you have some suggstions, patches, problems - please write an email or 
github message.

