# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

"""
Operations on kapture pose objects
"""

import math
import numpy as np
import quaternion
from typing import Tuple, Union, List

import kapture


def pose_transform_distance(pose_a: kapture.PoseTransform, pose_b: kapture.PoseTransform) -> Tuple[float, float]:
    """
    get translation and rotation distance between two PoseTransform

    :return: (position_distance, rotation_distance in rad), can be nan is case of invalid comparison
    """
    # handle NoneType with try expect blocks
    try:
        translation_distance = np.linalg.norm(pose_a.t - pose_b.t)
    except TypeError:
        translation_distance = math.nan

    try:
        rotation_distance = quaternion.rotation_intrinsic_distance(pose_a.r, pose_b.r)
    except TypeError:
        rotation_distance = math.nan
    return translation_distance, rotation_distance


def world_pose_transform_distance(pose_a: kapture.PoseTransform, pose_b: kapture.PoseTransform) -> Tuple[float, float]:
    """
    get position and rotation error between two PoseTransform
    pose_a and pose_b should be world to device

    :return: (position_distance, rotation_distance in deg), can be nan is case of invalid comparison
    """
    pass


def average_quaternion(big_q: np.ndarray) -> np.ndarray:
    """
    Computes the Chordal L2-Mean using quaternions.
    Ported from Tolga Birdal's implementation
    https://github.com/tolgabirdal/averaging_quaternions/blob/master/avg_quaternion_markley.m (MIT)

    :param big_q: Q (or big_q in python) is an (M,4) ndarray of quaternions
    :return: float array representing the average quaternion
    """
    pass


def average_pose_transform(poses: List[kapture.PoseTransform]) -> kapture.PoseTransform:
    """
    average a list of poses with equal weights

    :param poses: list of poses to average
    :return: average PoseTransform
    """
    pass


def average_quaternion_weighted(big_q: np.ndarray, weights: Union[List[float], np.ndarray]) -> np.ndarray:
    """
    Averaging Quaternions.
    Ported from Tolga Birdal's implementation
    https://github.com/tolgabirdal/averaging_quaternions/blob/master/wavg_quaternion_markley.m (MIT)

    :param big_q: Q is an (M,4) ndarray of quaternions
    :param weights: a (M,) vector
    :return: float array representing the average quaternion
    """
    pass


def average_pose_transform_weighted(poses: List[kapture.PoseTransform],
                                    weights: Union[List[float], np.ndarray]) -> kapture.PoseTransform:
    """
    average a list of poses with any weights

    :param poses: list of poses to average
    :param weights: a (len(poses),) vector
    :return: average PoseTransform
    """
    pass
