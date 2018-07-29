# pymdcs

The pymdcs package offers a Python interface to version 1.X MDCS databases.  The underlying functions are based on [MDCS-api-tools](https://github.com/MDCS-community/MDCS-api-tools), but has been reconstructed with the following features in mind:

- The module is lightweight and exists as a single Python file that can easily be incorporated into other projects.

- The code is class-based.  Database access information is entered when the class is initialized and retained.

- The access information can be saved locally and retrieved in a later session.

- Schemas/templates can be identified by title, ID, or filename.

- Queried results of records, templates and types are returned as a Pandas.DataFrame.