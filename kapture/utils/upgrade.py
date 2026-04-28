# Copyright 2021-present NAVER Corp. Under BSD 3-clause license

"""
Upgrade operations.
"""

import os
import os.path as path
from typing import List, Optional
import shutil
# import numpy as np like in kapture.io.csv
# so that types written as "np.float32" are understood by read_old_image_features_csv
import numpy as np  # noqa: F401

import kapture
import kapture.utils.logging
import kapture.io.features
import kapture.io.csv
from kapture.utils.paths import populate_files_in_dirpath
from kapture.utils.logging import getLogger

CSV_FILENAMES_1_0 = [
    path.join('sensors', 'sensors.txt'),
    path.join('sensors', 'trajectories.txt'),
    path.join('sensors', 'rigs.txt'),
    path.join('sensors', 'records_camera.txt'),
    path.join('sensors', 'records_depth.txt'),
    path.join('sensors', 'records_lidar.txt'),
    path.join('sensors', 'records_wifi.txt'),
    path.join('sensors', 'records_bluetooth.txt'),
    path.join('sensors', 'records_gnss.txt'),
    path.join('sensors', 'records_accelerometer.txt'),
    path.join('sensors', 'records_gyroscope.txt'),
    path.join('sensors', 'records_magnetic.txt'),
    path.join('reconstruction', 'points3d.txt')]


def read_old_image_features_csv(csv_filepath: str):
    """
    Read the old image feature

    :param csv_filepath: the path to the csv file containing image features
    """
    pass


def upgrade_1_0_to_1_1_inplace(kapture_dirpath: str,  # noqa: C901: function a bit long but well documented
                               keypoints_type: Optional[str],
                               descriptors_type: Optional[str],
                               global_features_type: Optional[str],
                               descriptors_metric_type: str,
                               global_features_metric_type: str) -> None:
    """
    Do the upgrade from 1.0 to 1.1 version in place: will replace all the necessary files.

    """
    pass


def upgrade_1_0_to_1_1_orphan_features(local_features_paths: List[str],
                                       global_features_paths: List[str]) -> None:
    """
    upgrade orphan features to kapture 1.1. Orphan features are features stored outside the kapture folder
    they must follow the kapture-localization recommendation
    https://github.com/naver/kapture-localization/blob/main/doc/tutorial.adoc#recommended-dataset-structure

    :param local_features_paths: examples dataset/local_features/r2d2 dataset/local_features/d2_tf
    :param global_features_paths: examples dataset/global_features/apgem dataset/global_features/delg
    """
    pass
