# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

import requests
import os
import os.path as path
from tqdm import tqdm
from typing import Optional
import logging

logger = logging.getLogger('downloader')


def get_remote_file_size(url: str):
    """
    return the total file size on the remote url.

    :param url: input full url of the file.
    :return : int of file size in bytes, or None if unknown
    """
    pass


def download_file_resume(url: str,
                         filepath: str,
                         resume_byte_pos: Optional[int] = None):
    """
    resume (or start if no pos given) the dataset download.

    :param url: input full url of the file to be downloaded.
    :param filepath: input full path where to save the file.
    :param resume_byte_pos: input position in bytes where to resume the Download
    """
    pass


def download_file(url, filepath):
    """
     Starts or resumes the download if already started.

    :param url: input full url of the file to be downloaded.
    :param filepath: input full path where to save the file.
     """
    pass
