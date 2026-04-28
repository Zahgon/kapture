# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

"""
Paths manipulations and filesystem operations.
"""

import os
import os.path as path
import shutil
import tempfile
from typing import AnyStr, Iterable, Optional, Union, List

from kapture.utils.logging import getLogger

logger = getLogger()


def path_secure(any_path: AnyStr) -> AnyStr:
    """
    Make sure path representation is OS independent (same on linux and windows),
    because path can be used as an identifier (eg. images).

    :param any_path: path to normalize
    :return: normalized path
    """
    return path.normpath(any_path).replace('\\', '/')


def populate_files_in_dirpath(root_dir_path: str,
                              filename_extensions: Optional[Union[str, List[str]]] = None,
                              do_relative_path: bool = True
                              ) -> Iterable[str]:
    """
    Returns the list of file path into the given root path.
    If a list of extensions is given, returns only files with those extensions.

    :param root_dir_path: the root directory path
    :param filename_extensions: optional file name extensions to filter in
    :param do_relative_path: if True, computes relative path.
    :return: list of paths
    """
    # list all files
    file_paths = (
        path.join(subdir, filename)
        for subdir, _, file_list in os.walk(root_dir_path)
        for filename in file_list
    )
    # if extensions are given, keep only files that complies.
    if filename_extensions:
        if not isinstance(filename_extensions, list):
            # make sure extensions is a list
            filename_extensions = [filename_extensions]
        # make sure given extensions are lower case.
        filename_extensions = [ext.lower() for ext in filename_extensions]
        # check the extension is authorized
        file_paths = (
            file_path for file_path in file_paths
            if path.splitext(file_path)[1].lower() in filename_extensions
        )

    # make it relative to root
    if do_relative_path:
        file_paths = (
            path.relpath(file_path, root_dir_path)
            for file_path in file_paths
        )

    file_paths = (path_secure(file_path)
                  for file_path in file_paths)
    return file_paths


def safe_remove_file(filepath: str, force: bool, comment: Optional[str] = '') -> None:
    """
    Safely remove a file, optionally asking confirmation to the user on the command line.

    :param filepath: path to the file to delete.
    :param force: If True, does not ask the question to the user and just do it.
    :param comment: comment on the file
    """
    if path.isfile(filepath):
        to_delete = (force or
                     (input(f'{comment} {filepath} already exist, would you like to delete it ? [y/N]').lower() == 'y'))
        # delete all or quit
        if to_delete:
            logger.info(f'deleting already existing {filepath}')
            os.remove(filepath)


def safe_remove_any_path(any_path: str, force: bool) -> None:
    """
    Safely remove any file system object (directory, file or link),
    optionally asking confirmation to the user on the command line.

    :param any_path: path to the filesystem object to delete.
    :param force: If True, does not ask the question to the user and just do it.
    """
    pass


def prepend_to_file(file_path: str, text_to_prepend: str) -> None:
    """
    Prepend a string at the beginning of a file.

    :param file_path: path to the file
    :param text_to_prepend: string to prepend
    """
    pass
