# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

import os
import tarfile
import hashlib
import logging

logger = logging.getLogger('downloader')


def untar_file(archive_filepath: str,
               install_dirpath: str):
    """
    Equivalent to tar -xf <archive_filepath> -C <install_dirpath>

    :param archive_filepath: input full path to the archive file.
    :param install_dirpath: input full path to directory where to extract.
    """
    pass


def compute_sha256sum(archive_filepath: str):
    """
    Computes the sha256sum on the given file.

    :param archive_filepath: input full path to file.
    :return the sha256sum.
    """
    pass
