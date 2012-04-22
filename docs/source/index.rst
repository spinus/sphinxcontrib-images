sphinxcontrib-fancybox's documentation
======================================

README
=======

.. include:: ../../readme.rst

Examples
========

0 - fancybox remote link
-------------------------------

.. fancybox:: http://creoeninternet.com/wp-content/uploads/2011/06/wikipedia.png


1 - fancybox non standard size
-------------------------------

.. fancybox:: img.jpg
    :width: 300px
    :height: 100px

2 - fancybox with additional class
-----------------------------------

.. fancybox:: img.jpg
    :class: someclass

    with css class


3 - fancybox with description (markup)
---------------------------------------

.. warning:: nested parsing of description is not working now, is rendered as 
    plaintext

.. fancybox:: img.jpg
    
    Some description of image, yey!
    Can be multiline and it is very **nice**. And with `<link>`_ to somwhere.


4 - image with class 'fancybox'
--------------------------------
.. image:: img.jpg
    :class: fancybox


5 - fancybox with description
-----------------------------

.. fancybox:: img.jpg

    witaj to jest **podpowiedz** JEJ.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

