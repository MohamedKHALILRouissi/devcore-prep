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

class MovieShort(object):
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
        'title': 'str',
        'year': 'str',
        'image': 'str',
        'im_db_rating': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'year': 'year',
        'image': 'image',
        'im_db_rating': 'imDbRating'
    }

    def __init__(self, id=None, title=None, year=None, image=None, im_db_rating=None):  # noqa: E501
        """MovieShort - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._year = None
        self._image = None
        self._im_db_rating = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if year is not None:
            self.year = year
        if image is not None:
            self.image = image
        if im_db_rating is not None:
            self.im_db_rating = im_db_rating

    @property
    def id(self):
        """Gets the id of this MovieShort.  # noqa: E501


        :return: The id of this MovieShort.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MovieShort.


        :param id: The id of this MovieShort.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this MovieShort.  # noqa: E501


        :return: The title of this MovieShort.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MovieShort.


        :param title: The title of this MovieShort.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def year(self):
        """Gets the year of this MovieShort.  # noqa: E501


        :return: The year of this MovieShort.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this MovieShort.


        :param year: The year of this MovieShort.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def image(self):
        """Gets the image of this MovieShort.  # noqa: E501


        :return: The image of this MovieShort.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MovieShort.


        :param image: The image of this MovieShort.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def im_db_rating(self):
        """Gets the im_db_rating of this MovieShort.  # noqa: E501


        :return: The im_db_rating of this MovieShort.  # noqa: E501
        :rtype: str
        """
        return self._im_db_rating

    @im_db_rating.setter
    def im_db_rating(self, im_db_rating):
        """Sets the im_db_rating of this MovieShort.


        :param im_db_rating: The im_db_rating of this MovieShort.  # noqa: E501
        :type: str
        """

        self._im_db_rating = im_db_rating

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
        if issubclass(MovieShort, dict):
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
        if not isinstance(other, MovieShort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
