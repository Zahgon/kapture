# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

import os
import os.path as path
from random import randint
import numpy as np
from PIL import Image, ImageDraw

from .features import image_keypoints_from_file


def image_keypoints_to_image(
        image: Image,
        keypoints: np.ndarray,
        radius: int = 2,
        filled: bool = True) -> Image:
    """
    Displays keypoints on top of the image.

    :param image: an image
    :param keypoints: the keypoints
    :param radius: radius of the drawn circles
    :param filled: True: draw discs, False: draw circles
    :return: a new Image
    """
    pass


def image_keypoints_to_image_file(
        output_filepath: str,
        image_filepath: str,
        keypoints_filepath: str,
        keypoint_dtype,
        keypoint_dsize,
        radius: int = 2) -> None:
    """
    Displays keypoints on top of the image and save it to image file.

    :param output_filepath: input path to output image of keypoints.
    :param image_filepath: input path to input image.
    :param keypoints_filepath: input path to keypoints file.
    :param keypoint_dtype: input data type of keypoints data (cf. binary).
    :param keypoint_dsize: input data size of keypoints data (cf. binary)
    :param radius: radius of the keypoint in image (in pixel).
    :return:
    """
    pass
