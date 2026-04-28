# Copyright 2020-present NAVER Corp. Under BSD 3-clause license

from .Sensors import Sensors, Camera
from .Rigs import Rigs
from .Trajectories import Trajectories
from .Records import RecordsCamera, RecordsDepth, RecordsLidar, RecordsWifi, RecordsBluetooth
from .Records import RecordsGnss, RecordsAccelerometer, RecordsGyroscope, RecordsMagnetic
from .ImageFeatures import Keypoints, Descriptors, GlobalFeatures
from .Matches import Matches
from .Observations import Observations
from .Points3d import Points3d
from typing import Dict, Optional, Union
import logging

logger = logging.getLogger(__name__)


class Kapture:
    """
    brief: Root class of all kapture data.
    """

    def __init__(
            self,
            sensors: Optional[Sensors] = None,
            rigs: Optional[Rigs] = None,
            trajectories: Optional[Trajectories] = None,
            records_camera: Optional[RecordsCamera] = None,
            records_depth: Optional[RecordsDepth] = None,
            records_lidar: Optional[RecordsLidar] = None,
            records_wifi: Optional[RecordsWifi] = None,
            records_bluetooth: Optional[RecordsBluetooth] = None,
            records_gnss: Optional[RecordsGnss] = None,
            records_accelerometer: Optional[RecordsAccelerometer] = None,
            records_gyroscope: Optional[RecordsGyroscope] = None,
            records_magnetic: Optional[RecordsMagnetic] = None,
            keypoints: Optional[Dict[str, Keypoints]] = None,
            descriptors: Optional[Dict[str, Descriptors]] = None,
            global_features: Optional[Dict[str, GlobalFeatures]] = None,
            matches: Optional[Dict[str, Matches]] = None,
            observations: Optional[Observations] = None,
            points3d: Optional[Points3d] = None,
    ):
        self.sensors = sensors
        self.rigs = rigs
        self.trajectories = trajectories
        self.records_camera = records_camera
        self.records_depth = records_depth
        self.records_lidar = records_lidar
        self.records_wifi = records_wifi
        self.records_bluetooth = records_bluetooth
        self.records_gnss = records_gnss
        self.records_accelerometer = records_accelerometer
        self.records_gyroscope = records_gyroscope
        self.records_magnetic = records_magnetic
        self.keypoints = keypoints
        self.descriptors = descriptors
        self.global_features = global_features
        self.matches = matches
        self.observations = observations
        self.points3d = points3d
        self.__version__ = '0.0'

    @property
    def format_version(self):
        """
        :return: kapture format version
        """
        pass

    @property
    def sensors(self) -> Optional[Sensors]:
        """
        :return: the list of sensors
        """
        pass

    @sensors.setter
    def sensors(self, sensors: Optional[Sensors]):
        pass

    @property
    def cameras(self) -> Dict[str, Camera]:
        """
        :return: the cameras (particular kind of sensor) as dictionary keyed by the camera identifier
        """
        pass

    @property
    def rigs(self) -> Optional[Rigs]:
        """
        :return: the list of rigs
        """
        pass

    @rigs.setter
    def rigs(self, rigs: Optional[Rigs]):
        pass

    @property
    def trajectories(self) -> Optional[Trajectories]:
        """
        :return: the list of trajectories
        """
        pass

    @trajectories.setter
    def trajectories(self, trajectories: Optional[Trajectories]):
        pass

    @property
    def records_camera(self) -> Optional[RecordsCamera]:
        """
        :return: Camera records
        """
        pass

    @records_camera.setter
    def records_camera(self, records_camera: Optional[RecordsCamera]):
        pass

    @property
    def records_depth(self) -> Optional[RecordsDepth]:
        """
        :return: Depth records
        """
        pass

    @records_depth.setter
    def records_depth(self, records_depth: Optional[RecordsDepth]):
        pass

    @property
    def records_lidar(self) -> Optional[RecordsLidar]:
        """
        :return: Lidar records
        """
        pass

    @records_lidar.setter
    def records_lidar(self, records_lidar: Optional[RecordsLidar]):
        pass

    @property
    def records_wifi(self) -> Optional[RecordsWifi]:
        """
        :return: Wifi records
        """
        pass

    @records_wifi.setter
    def records_wifi(self, records_wifi: Optional[RecordsWifi]):
        pass

    @property
    def records_bluetooth(self) -> Optional[RecordsBluetooth]:
        """
        :return: Bluetooth records
        """
        pass

    @records_bluetooth.setter
    def records_bluetooth(self, records_bluetooth: Optional[RecordsBluetooth]):
        pass

    @property
    def records_gnss(self) -> Optional[RecordsGnss]:
        """
        :return: GNSS records
        """
        pass

    @records_gnss.setter
    def records_gnss(self, records_gnss: Optional[RecordsGnss]):
        pass

    @property
    def records_accelerometer(self) -> Optional[RecordsAccelerometer]:
        """
        :return: Acceleration records
        """
        pass

    @records_accelerometer.setter
    def records_accelerometer(self, records_accelerometer: Optional[RecordsAccelerometer]):
        pass

    @property
    def records_gyroscope(self) -> Optional[RecordsGyroscope]:
        """
        :return: Gyroscope records
        """
        pass

    @records_gyroscope.setter
    def records_gyroscope(self, records_gyroscope: Optional[RecordsGyroscope]):
        pass

    @property
    def records_magnetic(self) -> Optional[RecordsMagnetic]:
        """
        :return: Magnetic records
        """
        pass

    @records_magnetic.setter
    def records_magnetic(self, records_magnetic: Optional[RecordsMagnetic]):
        pass

    @property
    def keypoints(self) -> Optional[Dict[str, Keypoints]]:
        """
        :return: the keypoints collection
        """
        pass

    @keypoints.setter
    def keypoints(self, keypoints: Optional[Dict[str, Keypoints]]):
        pass

    @property
    def descriptors(self) -> Optional[Dict[str, Descriptors]]:
        """
        :return: the descriptors collection
        """
        pass

    @descriptors.setter
    def descriptors(self, descriptors: Optional[Dict[str, Descriptors]]):
        pass

    @property
    def global_features(self) -> Optional[Dict[str, GlobalFeatures]]:
        """
        :return: the global features collection
        """
        pass

    @global_features.setter
    def global_features(self, global_features: Optional[Dict[str, GlobalFeatures]]):
        pass

    @property
    def matches(self) -> Optional[Dict[str, Matches]]:
        """
        :return: the matches collection
        """
        pass

    @matches.setter
    def matches(self, matches: Optional[Dict[str, Matches]]):
        pass

    @property
    def observations(self) -> Optional[Observations]:
        """
        :return: the observations
        """
        pass

    @observations.setter
    def observations(self, observations: Optional[Observations]):
        pass

    @property
    def points3d(self) -> Optional[Points3d]:
        """
        :return: the 3D points
        """
        pass

    @points3d.setter
    def points3d(self, points3d: Optional[Points3d]):
        pass

    def as_dict(self, keep_none=False) -> Dict[str, Union[
        Sensors,
        Rigs,
        Trajectories,
        RecordsCamera,
        RecordsDepth,
        RecordsLidar,
        RecordsWifi,
        RecordsBluetooth,
        RecordsGnss,
        RecordsAccelerometer,
        RecordsGyroscope,
        RecordsMagnetic,
        Optional[Dict[str, Keypoints]],
        Optional[Dict[str, Descriptors]],
        Optional[Dict[str, GlobalFeatures]],
        Optional[Dict[str, Matches]],
        Observations,
        Points3d
    ]]:
        """ convenience accessor to all members at once """
        pass

    def __repr__(self) -> str:
        representation = '\n'.join([
            f'{name:14} : {len(value):4}'
            for name, value in self.as_dict().items()
        ])

        if len(representation) == 0:
            representation = 'no data'
        return representation
