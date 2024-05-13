# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cloth_drying_integrated import ClothDryingIntegrated  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_clothdryingintegrated(self):
        """Test case for controller_get_clothdryingintegrated

        Returns a list of cloth drying data.
        """
        response = self.client.open(
            '/clothdrying-api/v1/clothdryingintegrated',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_clothdryingintegrated_by_id(self):
        """Test case for controller_get_clothdryingintegrated_by_id

        Returns complete details of the cloth drying data with the specified ID.
        """
        response = self.client.open(
            '/clothdrying-api/v1/clothdryingintegrated/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_clothdryingintegrated_by_sensor(self):
        """Test case for controller_get_clothdryingintegrated_by_sensor

        Returns cloth drying data filtered by sensor.
        """
        response = self.client.open(
            '/clothdrying-api/v1/clothdryingintegrated/sensor/{sensorId}'.format(sensor_id='sensor_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_clothdryingintegrated_by_sensor_and_source(self):
        """Test case for controller_get_clothdryingintegrated_by_sensor_and_source

        Returns cloth drying data filtered by sensor and source.
        """
        response = self.client.open(
            '/clothdrying-api/v1/clothdryingintegrated/sensor/{sensorId}/source/{source}'.format(sensor_id='sensor_id_example', source='source_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_clothdryingintegrated_by_source(self):
        """Test case for controller_get_clothdryingintegrated_by_source

        Returns cloth drying data filtered by source.
        """
        response = self.client.open(
            '/clothdrying-api/v1/clothdryingintegrated/source/{source}'.format(source='source_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
