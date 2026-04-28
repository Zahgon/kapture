# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

"""
Merge kapture objects with remapping of identifiers.
"""

from kapture.io.tar import TarCollection
from typing import List, Optional, Type, Dict

import kapture
from kapture.io.records import TransferAction, get_image_fullpath, get_depth_map_fullpath
from kapture.utils.Collections import get_new_if_not_empty

from .merge_reconstruction import merge_keypoints_collections, merge_descriptors_collections
from .merge_reconstruction import merge_global_features_collections, merge_matches_collections
from .merge_reconstruction import merge_points3d_and_observations, merge_points3d
from .merge_records_data import merge_records_data


def get_sensors_mapping(sensors: kapture.Sensors, offset: int = 0) -> Dict[str, str]:
    """
    Creates list of sensor names,identifiers

    :param sensors: list of sensor definitions
    :param offset: optional offset for the identifier numbers
    :return: mapping of sensor names to identifiers
    """
    pass


def get_rigs_mapping(rigs: kapture.Rigs, offset: int = 0) -> Dict[str, str]:
    """
    Creates list of rig names,identifiers

    :param rigs: list of rig definitions
    :param offset: optional offset for the identifier numbers
    :return: mapping of rig names to identifiers
    """
    pass


def merge_table_key1(
        table_list,
        sensor_mappings: List[Dict[str, str]],
        table_constructor,
):
    """
    Merge several table with 1 key (Only device_id) into one.
    If multiple entry for a key keep only the first one.

    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :param table_list: list of table to merge.
    :param table_constructor: the class type of table.
    :return table_merged

    """
    pass


def merge_table_key2(
        table_list,
        sensor_mappings: List[Dict[str, str]],
        table_constructor,
):
    """
    Merge several table with 2 keys (eg. timestamps, device_id)  into one.
    If multiple entry for a key keep only the first one.

    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :param table_list: list of table to merge.
    :param table_constructor: the class type of table.
    :return table_merged

    """
    pass


def merge_table_key3(
        table_list,
        sensor_mappings: List[Dict[str, str]],
        table_constructor,
        subdict_constructor=dict,
):
    """
    Merge several table with 2 keys (eg. timestamps, device_id)  into one.
    If multiple entry for a key keep only the first one.

    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :param table_list: list of table to merge.
    :param table_constructor: the class type of table.
    :param subdict_constructor: used to create a new Dict type
    :return table_merged

    """
    pass


def merge_sensors(
        sensors_list: List[Optional[kapture.Sensors]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.Sensors:
    """
    Merge several sensors list into one list with new identifiers.

    :param sensors_list: list of sensors definitions to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged sensors definitions
    """
    pass


def merge_rigs(
        rigs_list: List[Optional[kapture.Rigs]],
        rig_mappings: List[Dict[str, str]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.Rigs:
    """
    Merge several rigs list into one list with new identifiers for the rigs and the sensors.

    :param rigs_list: list of rigs definitions to merge
    :param rig_mappings: mapping of the rigs identifiers to their new identifiers
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged rigs definitions
    """
    pass


def merge_trajectories(
        trajectories_list: List[Optional[kapture.Trajectories]],
        rig_mappings: List[Dict[str, str]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.Trajectories:
    """
    Merge several trajectories list into one list with new identifiers for the rigs and the sensors.

    :param trajectories_list: list of trajectories to merge
    :param rig_mappings: mapping of the rigs identifiers to their new identifiers
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged trajectories
    """
    pass


def merge_records_camera(
        records_camera_list: List[Optional[kapture.RecordsCamera]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsCamera:
    """
    Merge several camera records list into one list with new identifiers for the sensors.

    :param records_camera_list: list of camera records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged camera records
    """
    pass


def merge_records_depth(
        records_depth_list: List[Optional[kapture.RecordsDepth]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsDepth:
    """
    Merge several depth records list into one list with new identifiers for the sensors.

    :param records_depth_list: list of depth records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged depth records
    """
    pass


def merge_records_lidar(
        records_lidar_list: List[Optional[kapture.RecordsLidar]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsLidar:
    """
    Merge several lidar records list into one list with new identifiers for the sensors.

    :param records_lidar_list: list of lidar records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged lidar records
    """
    pass


def merge_records_wifi(
        records_wifi_list: List[Optional[kapture.RecordsWifi]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsWifi:
    """
    Merge several wifi records list into one list with new identifiers for the sensors.

    :param records_wifi_list: list of wifi records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged wifi records
    """
    pass


def merge_records_bluetooth(
        records_bluetooth_list: List[Optional[kapture.RecordsBluetooth]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsBluetooth:
    """
    Merge several bluetooth records list into one list with new identifiers for the sensors.

    :param records_bluetooth_list: list of wifi records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged bluetooth records
    """
    pass


def merge_records_gnss(
        records_gnss_list: List[Optional[kapture.RecordsGnss]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsGnss:
    """
    Merge several gnss records list into one list with new identifiers for the sensors.

    :param records_gnss_list: list of gnss records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged gnss records
    """
    pass


def merge_records_accelerometer(
        records_accelerometer_list: List[Optional[kapture.RecordsAccelerometer]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsAccelerometer:
    """
    Merge several accelerometer records list into one list with new identifiers for the sensors.

    :param records_accelerometer_list: list of accelerometer records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged accelerometer records
    """
    pass


def merge_records_gyroscope(
        records_gyroscope_list: List[Optional[kapture.RecordsGyroscope]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsGyroscope:
    """
    Merge several gyroscope records list into one list with new identifiers for the sensors.

    :param records_gyroscope_list: list of gyroscope records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged gyroscope records
    """
    pass


def merge_records_magnetic(
        records_magnetic_list: List[Optional[kapture.RecordsMagnetic]],
        sensor_mappings: List[Dict[str, str]]) -> kapture.RecordsMagnetic:
    """
    Merge several magnetic records list into one list with new identifiers for the sensors.

    :param records_magnetic_list: list of magnetic records to merge
    :param sensor_mappings: mapping of the sensor identifiers to their new identifiers
    :return: merged magnetic records
    """
    pass


def merge_remap(kapture_list: List[kapture.Kapture],  # noqa: C901: function a bit long but not too complex
                skip_list: List[Type],
                data_paths: List[str],
                tarcollection_list: List[TarCollection],
                kapture_path: str,
                images_import_method: TransferAction) -> kapture.Kapture:
    """
    Merge multiple kapture while remapping sensor ids (sensor_id) in merged output.

    :param kapture_list: list of kapture to merge.
    :param skip_list: input optional types to not merge. sensors and rigs are unskippable
    :param data_paths: list of path to root path directory in same order as mentioned in kapture_list.
    :param tarcollection_list: list of opened tar archives same order as mentioned in kapture_list.
    :param kapture_path: directory root path to the merged kapture.
    :param images_import_method: method to transfer image files
    :return: merged kapture object
    """
    pass


def _compute_new_ids(kapture_list, rigs_mapping, sensors_mapping):
    pass
