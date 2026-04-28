# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

"""
Merge kapture objects.
"""

from kapture.io.tar import TarCollection
from typing import List, Optional, Type

import kapture
from kapture.io.records import TransferAction, get_image_fullpath, get_depth_map_fullpath
from kapture.utils.Collections import get_new_if_not_empty

from .merge_reconstruction import merge_keypoints_collections, merge_descriptors_collections
from .merge_reconstruction import merge_global_features_collections, merge_matches_collections
from .merge_reconstruction import merge_points3d_and_observations, merge_points3d
from .merge_records_data import merge_records_data


def merge_table_key1(
        table_list,
        table_constructor,
):
    """
    Merge several table with 1 key (eg. device_id)  into one.
    If multiple entry for a key keep only the first one.

    :param table_list: list of table to merge.
    :param table_constructor: the class type of table.
    :return table_merged
    """
    pass


def merge_table_key2(
        table_list,
        table_constructor,
):
    """
    Merge several table with 2 keys (eg. timestamps, device_id)  into one.
    If multiple entry for a key keep only the first one.

    :param table_list: list of table to merge.
    :param table_constructor: the class type of table.
    :return table_merged
    """
    pass


def merge_table_key3(
        table_list,
        table_constructor,
        subdict_constructor=dict,
):
    """
    Merge several records lists. Records is a dict (eg. wifi)).
    For record with the same timestamp and sensor identifier, keep only the first one.

    :param table_list: list of table to merge.
    :param table_constructor: the class type of table.
    :param subdict_constructor: used to create a new Dict type
    :return table_merged
    """
    pass


def merge_sensors(
        sensors_list: List[Optional[kapture.Sensors]]
) -> kapture.Sensors:
    """
    Merge several sensors lists. For sensor with the same identifier, keep only the first one.

    :param sensors_list: list of sensors
    :return: merge sensors
    """
    pass


def merge_rigs(
        rigs_list: List[Optional[kapture.Rigs]]
) -> kapture.Rigs:
    """
    Merge several rigs lists. For sensor with the same rig and sensor identifier, keep only the first one.

    :param rigs_list: list of rigs
    :return: merged rigs
    """
    pass


def merge_trajectories(
        trajectories_list: List[Optional[kapture.Trajectories]]
) -> kapture.Trajectories:
    """
    Merge several trajectories lists. For trajectory point with the same timestamp and sensor identifier,
     keep only the first one.

    :param trajectories_list: list of trajectories
    :return: merged trajectories
    """
    pass


def merge_records_camera(
        records_camera_list: List[Optional[kapture.RecordsCamera]]
) -> kapture.RecordsCamera:
    """
    Merge several camera records lists. For camera record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_camera_list: list of camera records
    :return: merged camera records
    """
    pass


def merge_records_depth(
        records_depth_list: List[Optional[kapture.RecordsDepth]]
) -> kapture.RecordsDepth:
    """
    Merge several depth records lists. For depth record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_depth_list: list of depth records
    :return: merged depth records
    """
    pass


def merge_records_lidar(
        records_lidar_list: List[Optional[kapture.RecordsLidar]]
) -> kapture.RecordsLidar:
    """
    Merge several lidar records lists. For lidar record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_lidar_list: list of lidar records
    :return: merged lidar records
    """
    pass


def merge_records_wifi(
        records_wifi_list: List[Optional[kapture.RecordsWifi]]
) -> kapture.RecordsWifi:
    """
    Merge several wifi records lists.
    For wifi record with the same timestamp, sensor, BSSID,
     keep only the first one.

    :param records_wifi_list: list of wifi records
    :return: merged wifi records
    """
    pass


def merge_records_bluetooth(
        records_bluetooth_list: List[Optional[kapture.RecordsBluetooth]]
) -> kapture.RecordsBluetooth:
    """
    Merge several bluetooth records lists.
    For bluetooth record with the same timestamp, sensor, address,
     keep only the first one.

    :param records_bluetooth_list: list of wifi records
    :return: merged bluetooth records
    """
    pass


def merge_records_gnss(
        records_gnss_list: List[Optional[kapture.RecordsGnss]]
) -> kapture.RecordsGnss:
    """
    Merge several gnss records lists. For gnss record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_gnss_list: list of gnss records
    :return: merged gnss records
    """
    pass


def merge_records_accelerometer(
        records_accelerometer_list: List[Optional[kapture.RecordsAccelerometer]]
) -> kapture.RecordsAccelerometer:
    """
    Merge several accelerometer records lists.
    For accelerometer record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_accelerometer_list: list of accelerometer records
    :return: merged accelerometer records
    """
    pass


def merge_records_gyroscope(
        records_gyroscope_list: List[Optional[kapture.RecordsGyroscope]]
) -> kapture.RecordsGyroscope:
    """
    Merge several gyroscope records lists.
    For gyroscope record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_gyroscope_list: list of gnss records
    :return: merged gyroscope records
    """
    pass


def merge_records_magnetic(
        records_magnetic_list: List[Optional[kapture.RecordsMagnetic]]
) -> kapture.RecordsMagnetic:
    """
    Merge several magnetic records lists.
    For magnetic record with the same timestamp and sensor identifier,
     keep only the first one.

    :param records_magnetic_list: list of gnss records
    :return: merged magnetic records
    """
    pass


def merge_keep_ids(kapture_list: List[kapture.Kapture],  # noqa: C901: function a bit long but not too complex
                   skip_list: List[Type],
                   data_paths: List[str],
                   tarcollection_list: List[TarCollection],
                   kapture_path: str,
                   images_import_method: TransferAction) -> kapture.Kapture:
    """
    Merge multiple kapture while keeping ids (sensor_id) identical in merged and inputs.

    :param kapture_list: list of kapture to merge.
    :param skip_list: optional types not to merge. sensors and rigs are unskippable
    :param data_paths: list of path to root path directory in same order as mentioned in kapture_list.
    :param tarcollection_list: list of opened tar archives same order as mentioned in kapture_list.
    :param kapture_path: directory root path to the merged kapture.
    :param images_import_method: method to transfer image files
    :return: merged kapture
    """
    pass
