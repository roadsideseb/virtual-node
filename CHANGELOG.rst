=========
Changelog
=========

0.1.0
-----

* Add the ability to specify the version of node as an environmental variable
  using ``NODE_VERSION``. This makes it a lot easier to define the version of
  node that will be installed.
* Update the default version of node to **0.10.26**, the most recent version at
  the time of writing.

0.0.4
-----

* Adds strict version checking to prevent some version comparison issues.
* Corrects issue with ``os.path.join`` when ``PROJECT_DIR`` is not specified.

0.0.3
-----

* Drop calls of commands ``curl`` and ``tar`` in favour of python modules to
  make sure that this still works on machines without those commands installed.
* Add support for ``package.json`` file to specify a custom version of
  ``node``. This allows to re-align the versioning of ``virtual-node`` with
  python conventions.

0.0.2
-----

* Adds check for existing version of virtual-node
* Fix issues when used as dependency in ``setup.py``
* Switch from using ``install`` to ``build`` command

0.0.1
-----
* Initial release
