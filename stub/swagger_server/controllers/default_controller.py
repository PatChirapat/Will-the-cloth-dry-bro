import connexion
import six

from swagger_server.models.cloth_drying_integrated import ClothDryingIntegrated  # noqa: E501
from swagger_server import util


def controller_get_clothdryingintegrated():  # noqa: E501
    """Returns a list of cloth drying data.

     # noqa: E501


    :rtype: List[ClothDryingIntegrated]
    """
    return 'do some magic!'


def controller_get_clothdryingintegrated_by_id(id):  # noqa: E501
    """Returns complete details of the cloth drying data with the specified ID.

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: ClothDryingIntegrated
    """
    return 'do some magic!'


def controller_get_clothdryingintegrated_by_sensor(sensor_id):  # noqa: E501
    """Returns cloth drying data filtered by sensor.

     # noqa: E501

    :param sensor_id: 
    :type sensor_id: str

    :rtype: List[ClothDryingIntegrated]
    """
    return 'do some magic!'


def controller_get_clothdryingintegrated_by_sensor_and_source(sensor_id, source):  # noqa: E501
    """Returns cloth drying data filtered by sensor and source.

     # noqa: E501

    :param sensor_id: 
    :type sensor_id: str
    :param source: 
    :type source: str

    :rtype: List[ClothDryingIntegrated]
    """
    return 'do some magic!'


def controller_get_clothdryingintegrated_by_source(source):  # noqa: E501
    """Returns cloth drying data filtered by source.

     # noqa: E501

    :param source: 
    :type source: str

    :rtype: List[ClothDryingIntegrated]
    """
    return 'do some magic!'
