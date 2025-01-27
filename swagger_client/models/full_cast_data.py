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

class FullCastData(object):
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
        'im_db_id': 'str',
        'title': 'str',
        'full_title': 'str',
        'type': 'str',
        'year': 'str',
        'directors': 'CastShort',
        'writers': 'CastShort',
        'actors': 'list[ActorShort]',
        'others': 'list[CastShort]',
        'error_message': 'str'
    }

    attribute_map = {
        'im_db_id': 'imDbId',
        'title': 'title',
        'full_title': 'fullTitle',
        'type': 'type',
        'year': 'year',
        'directors': 'directors',
        'writers': 'writers',
        'actors': 'actors',
        'others': 'others',
        'error_message': 'errorMessage'
    }

    def __init__(self, im_db_id=None, title=None, full_title=None, type=None, year=None, directors=None, writers=None, actors=None, others=None, error_message=None):  # noqa: E501
        """FullCastData - a model defined in Swagger"""  # noqa: E501
        self._im_db_id = None
        self._title = None
        self._full_title = None
        self._type = None
        self._year = None
        self._directors = None
        self._writers = None
        self._actors = None
        self._others = None
        self._error_message = None
        self.discriminator = None
        if im_db_id is not None:
            self.im_db_id = im_db_id
        if title is not None:
            self.title = title
        if full_title is not None:
            self.full_title = full_title
        if type is not None:
            self.type = type
        if year is not None:
            self.year = year
        if directors is not None:
            self.directors = directors
        if writers is not None:
            self.writers = writers
        if actors is not None:
            self.actors = actors
        if others is not None:
            self.others = others
        if error_message is not None:
            self.error_message = error_message

    @property
    def im_db_id(self):
        """Gets the im_db_id of this FullCastData.  # noqa: E501


        :return: The im_db_id of this FullCastData.  # noqa: E501
        :rtype: str
        """
        return self._im_db_id

    @im_db_id.setter
    def im_db_id(self, im_db_id):
        """Sets the im_db_id of this FullCastData.


        :param im_db_id: The im_db_id of this FullCastData.  # noqa: E501
        :type: str
        """

        self._im_db_id = im_db_id

    @property
    def title(self):
        """Gets the title of this FullCastData.  # noqa: E501


        :return: The title of this FullCastData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FullCastData.


        :param title: The title of this FullCastData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def full_title(self):
        """Gets the full_title of this FullCastData.  # noqa: E501


        :return: The full_title of this FullCastData.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this FullCastData.


        :param full_title: The full_title of this FullCastData.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def type(self):
        """Gets the type of this FullCastData.  # noqa: E501


        :return: The type of this FullCastData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FullCastData.


        :param type: The type of this FullCastData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def year(self):
        """Gets the year of this FullCastData.  # noqa: E501


        :return: The year of this FullCastData.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this FullCastData.


        :param year: The year of this FullCastData.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def directors(self):
        """Gets the directors of this FullCastData.  # noqa: E501


        :return: The directors of this FullCastData.  # noqa: E501
        :rtype: CastShort
        """
        return self._directors

    @directors.setter
    def directors(self, directors):
        """Sets the directors of this FullCastData.


        :param directors: The directors of this FullCastData.  # noqa: E501
        :type: CastShort
        """

        self._directors = directors

    @property
    def writers(self):
        """Gets the writers of this FullCastData.  # noqa: E501


        :return: The writers of this FullCastData.  # noqa: E501
        :rtype: CastShort
        """
        return self._writers

    @writers.setter
    def writers(self, writers):
        """Sets the writers of this FullCastData.


        :param writers: The writers of this FullCastData.  # noqa: E501
        :type: CastShort
        """

        self._writers = writers

    @property
    def actors(self):
        """Gets the actors of this FullCastData.  # noqa: E501


        :return: The actors of this FullCastData.  # noqa: E501
        :rtype: list[ActorShort]
        """
        return self._actors

    @actors.setter
    def actors(self, actors):
        """Sets the actors of this FullCastData.


        :param actors: The actors of this FullCastData.  # noqa: E501
        :type: list[ActorShort]
        """

        self._actors = actors

    @property
    def others(self):
        """Gets the others of this FullCastData.  # noqa: E501


        :return: The others of this FullCastData.  # noqa: E501
        :rtype: list[CastShort]
        """
        return self._others

    @others.setter
    def others(self, others):
        """Sets the others of this FullCastData.


        :param others: The others of this FullCastData.  # noqa: E501
        :type: list[CastShort]
        """

        self._others = others

    @property
    def error_message(self):
        """Gets the error_message of this FullCastData.  # noqa: E501


        :return: The error_message of this FullCastData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this FullCastData.


        :param error_message: The error_message of this FullCastData.  # noqa: E501
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
        if issubclass(FullCastData, dict):
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
        if not isinstance(other, FullCastData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
