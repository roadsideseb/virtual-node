virtual-node
============

Continuous integration status:

.. image:: https://secure.travis-ci.org/elbaschid/virtual-node.png
    :target: http://travis-ci.org/#!/elbaschid/virtual-node


This package is a wrapper around the `node.js`_ sources and provides a
convenient way to install it directly into your ``virtualenv`` instead
of globally. I created this package to play around with a simple 
installation for Django projects that use `django-compressor`_'s
precompiler to generate CSS from `less`_ files.

The install routine used in ``setup.py`` is adapted from the
`nodeenv`_ package provided by Eugene Kalinin. The difference is that I want
to install node.js into an existing ``virtualenv`` instead of creating
a specific environment for node.

I am using this in combination with `virtual-less`_ which installs the
``lessc`` commandline tool into a virtual environment.

.. _`less`: http://lesscss.org
.. _`node.js`: http://nodejs.org/
.. _`nodeenv`: http://github.com/ekalinin/nodeenv
.. _`virtual-less`: http://github.com/elbaschid/virtual-less
.. _`django-compressor`: https://github.com/jezdez/django_compressor


Installation
------------

.. warning:: This will download the node.js sources and compile it into your
    virtualenv. Make sure that you have all required build dependencies for
    node.js installed before installing virtual-node. The installation will
    take quite a long time to run for the first time around, so have a coffee
    or a beer handy.

Installing the ``node`` into your virtual environment is as easy as::

    $ pip install virtual-node

That should be it. You should now be able to run ``node`` from within
your virtual environment even if you have it globally installed. You
can make sure that this is the case::

    $ which node
    /home/elbaschid/.virtualenvs/lessc-test/bin/node

.. note:: virtual-node is explicitly meant to be installed into a virtualenv
    and not into your global environment. This has not been tested and will
    most likely not work or cause problems. Only try it if you know what you
    are doing.

Install specific version of ``node``
++++++++++++++++++++++++++++++++++++

Starting with version **0.0.3** it is possible to specify the version of
``node`` using the ``NPM`` packaging format ``package.json``. To use this
feature you need to specify the current project directory in the environment
variable ``PROJECT_DIR`` **before** you install ``virtual-node``. You can
simply export it on the commandline::

    $ export PROJECT_DIR=/path/to/my/project

or define it in your ``virtualenv``/``virtualenvwrapper`` scripts.

During installation, the setup script will attempt to retrieve the desired
version of node from a file named ``package.json`` which is also used by
``NPM`` [and is explained in detail on their website](https://npmjs.org/doc/json.html).

A sample file to specify version ``0.10.0`` would look like this::

    {
      "name": "my-project",
      "version": "0.0.1",
      "engines": {
        "node": "==0.10.0"
      }
    }

The version of the engine to be used is the version that ``virtual-node``
will use to install ``node``. **Note:** you have to specify an exact version
(using ``==``) otherwise the version will be ignored.


Issues & Contributions
----------------------

Please let me know if you have any issues, please raise an issue
here on the github project.

If you want to contribute, fork this repository and open a pull
request with your changes. I'd be happy to include them.

License
-------

This package is released under the permissive `New BSD license`_.

.. _`New BSD license`: https://github.com/elbaschid/virtual-less/blob/master/LICENSE
