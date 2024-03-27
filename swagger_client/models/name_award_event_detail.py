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

class NameAwardEventDetail(object):
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
        'image': 'str',
        'title': 'str',
        '_for': 'str',
        'description': 'str'
    }

    attribute_map = {
        'image': 'image',
        'title': 'title',
        '_for': 'for',
        'description': 'description'
    }

    def __init__(self, image=None, title=None, _for=None, description=None):  # noqa: E501
        """NameAwardEventDetail - a model defined in Swagger"""  # noqa: E501
        self._image = None
        self._title = None
        self.__for = None
        self._description = None
        self.discriminator = None
        if image is not None:
            self.image = image
        if title is not None:
            self.title = title
        if _for is not None:
            self._for = _for
        if description is not None:
            self.description = description

    @property
    def image(self):
        """Gets the image of this NameAwardEventDetail.  # noqa: E501


        :return: The image of this NameAwardEventDetail.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NameAwardEventDetail.


        :param image: The image of this NameAwardEventDetail.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def title(self):
        """Gets the title of this NameAwardEventDetail.  # noqa: E501


        :return: The title of this NameAwardEventDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NameAwardEventDetail.


        :param title: The title of this NameAwardEventDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def _for(self):
        """Gets the _for of this NameAwardEventDetail.  # noqa: E501


        :return: The _for of this NameAwardEventDetail.  # noqa: E501
        :rtype: str
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this NameAwardEventDetail.


        :param _for: The _for of this NameAwardEventDetail.  # noqa: E501
        :type: str
        """

        self.__for = _for

    @property
    def description(self):
        """Gets the description of this NameAwardEventDetail.  # noqa: E501


        :return: The description of this NameAwardEventDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NameAwardEventDetail.


        :param description: The description of this NameAwardEventDetail.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(NameAwardEventDetail, dict):
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
        if not isinstance(other, NameAwardEventDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
