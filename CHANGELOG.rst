=========
Changelog
=========

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
