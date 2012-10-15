virtual-node
============

This package is a wrapper around the `nose.js`_ sources and provides a
convenient way to install it directly into your ``virtualenv`` instead
of globally. I created this package to play around with a simple 
installation for Django projects that us `django-compressor`_'s
precompiler to generate CSS from `less`_ files.

The install routine used in ``setup.py`` is adapted from the
`nodeenv`_ package provided by Eugene Kalinin. The difference is that I want
to install node.js into an existing ``virtualenv`` instead of creating
a specific environment for node.

I am using this in combination with `virtual-less`_ which installs the
``lessc`` commandline tool into a virtual environment.

.. _`less`: http://lesscss.org
.. _`node.js`: http://nodejs.org/
.. _`virtual-less`: http://github.com/elbaschid/virtual-less
.. _`django-compressor`: https://github.com/jezdez/django_compressor


Installation
------------

Installing the ``node`` into your virtual environment is as easy as::

    $ pip install virtual-node

that should be it. You should now be able to run ``node`` from within
your virtual environment even if you have it globally installed. You
can make sure that this is the case::

    $ which node
    /home/elbaschid/.virtualenvs/lessc-test/bin/node

Issues & Contributions
----------------------

Please let me know if you have any issues, please raise an issue
here on the github project.

If you want to contribute, fork this repository and open a pull
request with your changes. I'd be happy to include them.

License
-------

Oscar is released under the permissive `New BSD license`_.

.. _`New BSD license`: https://github.com/elbaschid/virtual-less/blob/master/LICENSE
