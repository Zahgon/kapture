# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

"""
Import a rosbag with images from several camera and position associated to the images recorded.
Works by default with the RealSense T265 camera.
Must have ROS installed, as well as rosbag module.
"""
import copy
from collections import OrderedDict
import logging
import os
import os.path as path
import sys
from typing import Any, Dict, List, Optional, Union
import numpy as np
import PIL.Image as PILImage
import quaternion
from tqdm import tqdm
# ros
import geometry_msgs.msg
import rosbag
import rospy.rostime
from rospy.rostime import Duration
# kapture
import kapture
from kapture.core.flatten import flatten
from kapture.core.Rigs import Rigs
from kapture.core.Sensors import Sensors
import kapture.io.csv as kcsv
import kapture.io.structure
from kapture.io.records import get_image_fullpath
from kapture.utils.Collections import LimitedDictionary
from kapture.utils.paths import path_secure


rotation_cam_kapture_from_cam_ros = np.array([
    [0, -1, 0],
    [0, 0, -1],
    [1, 0, 0]
])

pose_kapture_from_ros = kapture.PoseTransform(r=quaternion.from_rotation_matrix(rotation_cam_kapture_from_cam_ros))
pose_ros_from_kapture = pose_kapture_from_ros.inverse()


class ImageInfo:
    """
    Image info found in the Rosbag
    """

    def __init__(self,
                 filename: str,
                 timestamp: rospy.rostime.Time,
                 camera_name: str):
        self.filename = filename
        self.timestamp = timestamp
        self.camera_name = camera_name


class PositionInfo:
    """
    Position info found in the Rosbag
    """

    def __init__(self,
                 timestamp: rospy.rostime.Time,
                 pose6d: geometry_msgs.msg.Pose):
        self.timestamp = timestamp
        self.pose6d = pose6d


def _extract_img_buf(msg) -> np.ndarray:
    """
    Extracts the image as numpy one dimension array from the ROS message
    """
    pass


class RosBagImporter:
    """
    A importer of ROS bags with multi cam images data and odometry.
    The join between the two types of data is made on their data timestamps.
    """

    def __init__(self,
                 rosbag_path: str,
                 rigs: Optional[Rigs],
                 sensors: Sensors,
                 kapture_path: str,
                 force_overwrite_existing: bool = False) -> None:
        """

        :param rosbag_path: full path to the rosbag file
        :param rigs: rigs of the sensors
        :param sensors: sensors definition used for the capture
        :param kapture_path: full path to the top kapture directory to save
        :param force_overwrite_existing: silently overwrite kapture files if already exists
        """
        if not path.isfile(rosbag_path):
            raise ValueError(f'Rosbag file {rosbag_path} does not exist')
        self._rosbag_path = rosbag_path
        self._rigs = rigs
        self._sensors = sensors
        self._kapture_path = kapture_path
        self.logger = logging.getLogger('rosbag')
        self.logger.info(f'Reading rosbag file {rosbag_path} and exporting as Kapture format into {kapture_path}')
        os.makedirs(kapture_path, exist_ok=True)
        kapture.io.structure.delete_existing_kapture_files(kapture_path, force_overwrite_existing)
        self._images_full_path = get_image_fullpath(kapture_path)
        self._image_directory_path = OrderedDict()  # Should be OrderedDict[str, str]
        self._image_topic_to_cam_id = dict()
        # Keys = timestamp, values odometer poses
        self._last_poses = LimitedDictionary(20)
        self.images_info = list()  # Of ImageInfo: type annotation is not supported in 3.6
        self.poses_info = list()  # Of PositionInfo
        self._image_count_per_camera = -1
        self._saved_number = 0

    def _check_bag_topics(self, bag: rosbag.bag.Bag, odometry_topic: Optional[str], image_topics: List[str]):
        pass

    def _create_images_directories(self, camera_identifiers, image_topics):
        pass

    def _save_image(self,
                    image_bitmap: np.ndarray,
                    image_directory_path: str,
                    image_number: int,
                    timestamp: rospy.rostime.Time) -> str:
        """
        Save the image.

        :param image_bitmap: the image bytes
        :param image_directory_path: directory where to save the image, under the top kapture directory
        :param image_number: image sequence number
        :param timestamp: image time stamp to set to the file
        :return: relative path (to the kapture path) of the file
        """
        pass

    def _find_pose(self, image_stamp: rospy.rostime.Time) -> Optional[geometry_msgs.msg.Pose]:
        """
        Find the pose that has the smallest time difference with the image timestamp

        :param image_stamp: an image time stamp
        :return: a geometric pose if found, none otherwise
        """
        pass

    def _check_timestamp_delta(self, images_stamp: Dict[Any, rospy.rostime.Time], enforce_same_time: bool,
                               image_number: int) -> None:
        # The images are taken every 0.033 second
        # Check all images have the same time stamp modulo epsilon
        pass

    def import_multi_camera(self, odometry_topic: Optional[str],  # noqa: C901
                            image_topics: Union[str, List[str]],
                            camera_identifiers: Union[str, List[str]],
                            force_same_time: bool = True,
                            save_all_positions: bool = True,
                            find_image_position: bool = True,
                            percent: int = 100):
        """
        Import the rosbag data. Save the images on disk.
        The image topics list and camera identifiers list must be matching lists.

        :param odometry_topic: the odometry topic to use to compute the trajectory.
        :param image_topics: image topic(s) to import
        :param camera_identifiers: camera identifier(s) corresponding to the image topic(s)
        :param force_same_time: force all images to have the same timestamp
        :param save_all_positions: save all positions from the odometry topic in the trajectory
        :param find_image_position: find the closest position for the image and add it in the trajectory
        :param percent: percentage of images to keep.
        """
        pass

    def save_to_kapture(self, trajectory_rig_id: Optional[str] = None) -> None:
        """
        Save the data in kapture format.

        :param trajectory_rig_id: the rig identifier of the trajectory points
        """
        pass
