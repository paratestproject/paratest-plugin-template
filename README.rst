This proyect is just a template for other Paratest_ plugins.

Steps to create a new plugin:

#. Clone this repository: ``git clone https://github.com/paratestproject/paratest-plugin-template paratest-new-plugin``
#. Remove the ``.git`` directory and initialize git, if necessary: ``rm -rf .git && git init``
#. Edit the ``paratest_plugin/plugin.py`` file to implement the ``find`` function.
#. Move the ``paratest_plugin`` directory to match your plugin name (do not use hyphens; use underscores instead): ``mv paratest_plugin paratest_new_plugin``
#. Edit the ``setup.py`` file, changing the name, version, author, author_email, url and entry_points path.
#. Register the new plugin in pypi: ``python setup.py register``
#. Ensure you have ``wheel`` installed: ``pip install wheel``
#. Upload the new plugin to pypi: ``python setup.py sdist bdist_wheel upload``

Alternatively, you can rename ``paratest_plugin/plugin.py`` too, but remember to change the ``entry_point`` key in ``setup.py`` too.

To test it, just run ``python paratest_plugin/plugin.py path_to_test_files`` and check the output is correct.

Finally, just to remember that the command line may contain some variables:

- ``{ID}`` will be replaced by the worker identifier.
- ``{WORKSPACE}`` will be replaced by the full path to worker workspace
- ``{TID_NAME}`` will be replaced by the test name


.. _`Paratest`: https://github.com/paratestproject/paratest
