# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

"""
Kapture to opensfm export functions.
"""

import os
import logging
import os.path as path
import numpy as np
import quaternion
import gzip
import pickle
import json
from tqdm import tqdm
from typing import Any, Dict, Optional
# kapture
import kapture
from kapture.io.csv import get_all_tar_handlers, kapture_from_dir
from kapture.utils.Collections import try_get_only_key_from_collection
from kapture.io.binary import TransferAction, transfer_files_from_dir
from kapture.io.features import get_keypoints_fullpath, image_keypoints_from_file
from kapture.io.features import get_descriptors_fullpath, image_descriptors_from_file
from kapture.io.features import get_matches_fullpath, image_matches_from_file
from kapture.io.records import get_record_fullpath


logger = logging.getLogger('opensfm')


"""
opensfm_project/
â”œâ”€â”€ config.yaml
â”œâ”€â”€ images/
â”œâ”€â”€ masks/
â”œâ”€â”€ gcp_list.txt
â”œâ”€â”€ exif/
â”œâ”€â”€ camera_models.json
â”œâ”€â”€ features/
â”œâ”€â”€ matches/
â”œâ”€â”€ tracks.csv
â”œâ”€â”€ reconstruction.json
â”œâ”€â”€ reconstruction.meshed.json
â””â”€â”€ undistorted/
    â”œâ”€â”€ images/
    â”œâ”€â”€ masks/
    â”œâ”€â”€ tracks.csv
    â”œâ”€â”€ reconstruction.json
    â””â”€â”€ depthmaps/
        â””â”€â”€ merged.ply
"""

"""
reconstruction.json: [RECONSTRUCTION, ...]

RECONSTRUCTION: {
    "cameras": {
        CAMERA_ID: CAMERA,
        ...
    },
    "shots": {
        SHOT_ID: SHOT,
        ...
    },
    "points": {
        POINT_ID: POINT,
        ...
    }
}

CAMERA: {
    "projection_type": "perspective",  # Can be perspective, brown, fisheye or equirectangular
    "width": NUMBER,                   # Image width in pixels
    "height": NUMBER,                  # Image height in pixels

    # Depending on the projection type more parameters are stored.
    # These are the parameters of the perspective camera.
    "focal": NUMBER,                   # Estimated focal length
    "k1": NUMBER,                      # Estimated distortion coefficient
    "k2": NUMBER,                      # Estimated distortion coefficient
}

SHOT: {
    "camera": CAMERA_ID,
    "rotation": [X, Y, Z],      # Estimated rotation as an angle-axis vector
    "translation": [X, Y, Z],   # Estimated translation
    "gps_position": [X, Y, Z],  # GPS coordinates in the reconstruction reference frame
    "gps_dop": METERS,          # GPS accuracy in meters
    "orientation": NUMBER,      # EXIF orientation tag (can be 1, 3, 6 or 8)
    "capture_time": SECONDS     # Capture time as a UNIX timestamp
}

POINT: {
    "coordinates": [X, Y, Z],      # Estimated position of the point
    "color": [R, G, B],            # Color of the point
}
"""

"""
reconstruction.meshed.json
[{
    'cameras': {'v2 unknown unknown 1920 1080 perspective 0':
                {'projection_type': 'perspective', 'width': 1920, 'height': 1080, 'focal': 0.8647151305270488,
                'k1': 0.04060214391621549, 'k2': -0.04060273810852096}},
    'shots': {
        'frame00016.png' : {
        'rotation': [1.5061234719524716, 0.06688721174244067, -0.030847050348337724],
         'translation': [-2.1535823328020456, 0.28345212194377944, 1.2491740134158436],
         'camera': 'v2 unknown unknown 1920 1080 perspective 0',
         'orientation': 1,
         'capture_time': 0.0,
         'gps_dop', 'gps_position',
         'vertices',     # only in meshed
         'faces' [[x, y, z, ...]  # only in meshed
         },
         ...
    },
     'points': {
        '1': {
            'color': [74.0, 43.0, 31.0],
            'coordinates': [-4.204454761953588, 11.796709404713068, 4.7276044200915]
        },
        ...
     },
     'reference_lla': {
        'latitude': 0.0,
        'longitude': 0.0,
        'altitude': 0
     }
}]
"""


def export_opensfm_camera(
        kapture_camera: kapture.Camera
) -> Dict[str, Any]:
    """
    Converts kapture camera to OpenSfM.
    OpenSfm propose 3 models of camera: perspective, fisheye, spherical.
    Perspective Camera of OpenSfM
    (see https://www.opensfm.org/docs/geometry.html#camera-models)

    OpenSfM camera axis:
        - The z-axis points forward
        - The y-axis points down
        - The x-axis points to the right

    OpenSfM Pose:
        OpenSfM, however, chooses not to store the â€œcamera originâ€� in Pose objects.
        Instead, it stores the camera coordinates of the world origin in the translation field.
        Meaning Camera from World transformation.
        - rotation is represented as axis-angle vector.

    :param kapture_camera: camera kapture definition
    :return: camera definition as dictionary to save (as json, db record, ...)
    """
    pass


def _export_opensfm_features_and_matches(image_filenames,
                                         keypoints_type,
                                         descriptors_type,
                                         kapture_data,
                                         kapture_root_dir,
                                         tar_handlers,
                                         opensfm_root_dir,
                                         disable_tqdm):
    """
    export features files (keypoints + descriptors) and matches
    """
    pass


def export_opensfm(
        kapture_root_dir: str,
        opensfm_root_dir: str,
        force_overwrite_existing: bool = False,
        images_export_method: TransferAction = TransferAction.copy,
        keypoints_type: Optional[str] = None,
        descriptors_type: Optional[str] = None,
) -> None:
    """
    Export the kapture data to an openSfM format

    :param kapture_root_dir: full path to the top kapture directory
    :param opensfm_root_dir: path of the directory where to store the data in openSfM format
    :param force_overwrite_existing: if true, will remove existing openSfM data without prompting the user.
    :param images_export_method:
    """
    pass
