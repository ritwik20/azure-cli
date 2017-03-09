# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeviceDescription(Model):
    """Device identity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param device_id: Device Id. A case-sensitive string ( up to 128 char
     long).
    :type device_id: str
    :ivar generation_id: An IoT hub-generated case-sensitive string (up to
     128 char long). Used to distinguish devices with the same deviceId when
     they have been deleted and recreated.
    :vartype generation_id: str
    :param etag: A string representing a weak etag for the device identity,
     as per RFC7232.
    :type etag: str
    :param connection_state: 'connected' or 'disconnected', represents the
     IoT Hub view of the device connection status.
    :type connection_state: str
    :param status: 'enabled' or 'disabled', representing status of the device
    :type status: str
    :param status_reason: A string representing reason of the device status
    :type status_reason: str
    :param connection_state_updated_time: Date and time of last time the
     connection state was updated. In ISO8601 datetime format in UTC, e.g.
     2015-01-28T16:24:48.789Z
    :type connection_state_updated_time: datetime
    :param status_updated_time: Date and time of last time the status was
     updated. In ISO8601 datetime format in UTC, e.g. 2015-01-28T16:24:48.789Z
    :type status_updated_time: datetime
    :param last_activity_time: Datetime of last time the device connected,
     received or sent a message. In ISO8601 datetime format in UTC, e.g.
     2015-01-28T16:24:48.789Z
    :type last_activity_time: datetime
    :param cloud_to_device_message_count: Number of pending commands that are
     in the device command queue.
    :type cloud_to_device_message_count: long
    :param authentication:
    :type authentication: :class:`Authentication
     <iothubdeviceclient.models.Authentication>`
    """ 

    _validation = {
        'device_id': {'max_length': 128, 'min_length': 1},
        'generation_id': {'readonly': True},
    }

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'generation_id': {'key': 'generationId', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_reason': {'key': 'statusReason', 'type': 'str'},
        'connection_state_updated_time': {'key': 'connectionStateUpdatedTime', 'type': 'iso-8601'},
        'status_updated_time': {'key': 'statusUpdatedTime', 'type': 'iso-8601'},
        'last_activity_time': {'key': 'lastActivityTime', 'type': 'iso-8601'},
        'cloud_to_device_message_count': {'key': 'cloudToDeviceMessageCount', 'type': 'long'},
        'authentication': {'key': 'authentication', 'type': 'Authentication'},
    }

    def __init__(self, device_id=None, etag=None, connection_state=None, status=None, status_reason=None, connection_state_updated_time=None, status_updated_time=None, last_activity_time=None, cloud_to_device_message_count=None, authentication=None):
        self.device_id = device_id
        self.generation_id = None
        self.etag = etag
        self.connection_state = connection_state
        self.status = status
        self.status_reason = status_reason
        self.connection_state_updated_time = connection_state_updated_time
        self.status_updated_time = status_updated_time
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication = authentication
