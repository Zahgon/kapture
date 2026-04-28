# Copyright 2020-present NAVER Corp. Under BSD 3-clause license
import logging
from tqdm import tqdm
import os
import os.path as path
from random import randint
from typing import Dict
import numpy as np

import kapture
from .csv import kapture_linesep
from .features import image_keypoints_from_file


logger = logging.getLogger('ply')


PLY_HEADER_TEMPLATE = kapture_linesep.join([
    'ply',
    'format ascii 1.0',
    'element vertex {nb_vertex}',
    'property double x',
    'property double y',
    'property double z',
    'property uchar red',
    'property uchar green',
    'property uchar blue',
    'element edge {nb_edges}',
    'property int vertex1',
    'property int vertex2',
    'end_header'])

########################################################################################################################
BLACK = 3 * [0]
WHITE = 3 * [255]
GREY = 3 * [127]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
AXIS_COLORS = [GREY, RED, GREEN, BLUE]


########################################################################################################################
def get_axis_in_world(
        pose_device_from_world: kapture.PoseTransform, length: float = 1.0) -> kapture.Points3d:
    """
    Returns a quadruplet of points (0,x,y,z) representing the axis of the device into the world.

    :param pose_device_from_world: assume the transformation is device from world.
    :param length: distance between each axis point and center.
    :return: 4 points (center, x, y, z) arranged by cols
    """
    pass


def header_to_ply_stream(stream, nb_vertex: int = 0, nb_edges: int = 0) -> None:
    """
    Writes PLY header to a stream.

    :param stream: an open stream to write to
    :param nb_vertex: number of vertex
    :param nb_edges: number of edges
    """
    pass


def rig_to_ply_stream(stream, rig: Dict[str, kapture.PoseTransform], axis_length: float = 1.) -> None:
    """
    Writes the rig to a stream.

    :param stream: an open stream to write to
    :param rig: rig to write
    :param axis_length: length of the axis
    """
    pass


def rig_to_ply(filepath: str, rig: Dict[str, kapture.PoseTransform], axis_length: float = 1.) -> None:
    """
    Writes the rig to a file.

    :param filepath: file path to write to
    :param rig: rig to write
    :param axis_length: length of the axis
    """
    pass


########################################################################################################################
def trajectories_to_ply_stream(stream, trajectories: kapture.Trajectories, axis_length: float = 1.) -> None:
    """
    Writes the trajectories to a stream.
     trajectories[ts][device_id] = [pose]

    :param stream: an open stream to write to
    :param trajectories: trajectories to write
    :param axis_length: length of the axis
    """
    pass


def trajectories_to_ply(
        filepath: str,
        trajectories: kapture.Trajectories,
        axis_length: float = 1.
):
    """
    Writes trajectory to PLY format (for visualization).
    Each pose in trajectory leads to a ply dot. 3 additional points are added in X (red), Y (Green) and Z (blue)
    direction around each pose.

    :param filepath: input ply file path.
    :param trajectories: input trajectory
    :param axis_length: length of axis representing the orientation of each pose in trajectory.
    :return:
    """
    pass


def points3d_to_stream(stream, points3d: kapture.Points3d) -> None:
    """
    Writes the 3D points to a stream.

    :param stream: an open stream to write to
    :param points3d: 3d points to write
    """
    pass


def points3d_to_ply(filepath: str, points3d: kapture.Points3d) -> None:
    """
    Writes 3D points into ply file.

    :param filepath: ply file path.
    :param points3d: 3D points.
    """
    pass


def local_points3d_to_stream(
        stream,
        points3d: np.ndarray,
        transform_world_from_local: kapture.PoseTransform
) -> None:
    """
    Writes the 3D points from a local coordinate system into world into a stream.

    :param stream: an open stream to write to
    :param points3d: input 3d points as a Nx3 numpy array
    :param transform_world_from_local: transformation
    """
    pass


def local_points3d_to_ply(
        filepath: str,
        points3d: np.ndarray,
        transform_world_from_local: kapture.PoseTransform
) -> None:
    """
    Writes 3D points into ply file.

    :param filepath: ply file path.
    :param points3d: input 3d points as a Nx3 numpy array
    :param transform_world_from_local: transformation
    """
    pass


def image_keypoints_to_stream(stream, image_keypoints: np.array) -> None:
    """
    Plots image keypoints onto a 2D plane. Use random colors.

    :param stream: an open stream to write to
    :param image_keypoints: the image keypoints to write
    """
    pass


def image_keypoints_to_ply(ply_filepath: str, image_keypoints_filepath: str, keypoint_dtype, keypoint_dsize) -> None:
    """
    Plots image keypoints onto a 2D plane.

    :param ply_filepath: path to the ply file to write
    :param image_keypoints_filepath: path to the image keypoints file to read
    :param keypoint_dtype: keypoint data type
    :param keypoint_dsize: keypoint data size
    """
    pass
