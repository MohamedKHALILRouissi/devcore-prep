# coding: utf-8

"""
    TV-API

    The TVAPI Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CompanyData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'items': 'list[MovieShort]',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'items': 'items',
        'error_message': 'errorMessage'
    }

    def __init__(self, id=None, name=None, items=None, error_message=None):  # noqa: E501
        """CompanyData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._items = None
        self._error_message = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if items is not None:
            self.items = items
        if error_message is not None:
            self.error_message = error_message

    @property
    def id(self):
        """Gets the id of this CompanyData.  # noqa: E501


        :return: The id of this CompanyData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyData.


        :param id: The id of this CompanyData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CompanyData.  # noqa: E501


        :return: The name of this CompanyData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanyData.


        :param name: The name of this CompanyData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def items(self):
        """Gets the items of this CompanyData.  # noqa: E501


        :return: The items of this CompanyData.  # noqa: E501
        :rtype: list[MovieShort]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CompanyData.


        :param items: The items of this CompanyData.  # noqa: E501
        :type: list[MovieShort]
        """

        self._items = items

    @property
    def error_message(self):
        """Gets the error_message of this CompanyData.  # noqa: E501


        :return: The error_message of this CompanyData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CompanyData.


        :param error_message: The error_message of this CompanyData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CompanyData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompanyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
