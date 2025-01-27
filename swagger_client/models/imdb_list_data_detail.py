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

class IMDbListDataDetail(object):
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
        'index': 'str',
        'title': 'str',
        'full_title': 'str',
        'year': 'str',
        'image': 'str',
        'im_db_rating': 'str',
        'im_db_rating_count': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'index': 'index',
        'title': 'title',
        'full_title': 'fullTitle',
        'year': 'year',
        'image': 'image',
        'im_db_rating': 'imDbRating',
        'im_db_rating_count': 'imDbRatingCount',
        'description': 'description'
    }

    def __init__(self, id=None, index=None, title=None, full_title=None, year=None, image=None, im_db_rating=None, im_db_rating_count=None, description=None):  # noqa: E501
        """IMDbListDataDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._index = None
        self._title = None
        self._full_title = None
        self._year = None
        self._image = None
        self._im_db_rating = None
        self._im_db_rating_count = None
        self._description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if index is not None:
            self.index = index
        if title is not None:
            self.title = title
        if full_title is not None:
            self.full_title = full_title
        if year is not None:
            self.year = year
        if image is not None:
            self.image = image
        if im_db_rating is not None:
            self.im_db_rating = im_db_rating
        if im_db_rating_count is not None:
            self.im_db_rating_count = im_db_rating_count
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this IMDbListDataDetail.  # noqa: E501


        :return: The id of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IMDbListDataDetail.


        :param id: The id of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def index(self):
        """Gets the index of this IMDbListDataDetail.  # noqa: E501


        :return: The index of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IMDbListDataDetail.


        :param index: The index of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._index = index

    @property
    def title(self):
        """Gets the title of this IMDbListDataDetail.  # noqa: E501


        :return: The title of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IMDbListDataDetail.


        :param title: The title of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def full_title(self):
        """Gets the full_title of this IMDbListDataDetail.  # noqa: E501


        :return: The full_title of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this IMDbListDataDetail.


        :param full_title: The full_title of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def year(self):
        """Gets the year of this IMDbListDataDetail.  # noqa: E501


        :return: The year of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this IMDbListDataDetail.


        :param year: The year of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def image(self):
        """Gets the image of this IMDbListDataDetail.  # noqa: E501


        :return: The image of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IMDbListDataDetail.


        :param image: The image of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def im_db_rating(self):
        """Gets the im_db_rating of this IMDbListDataDetail.  # noqa: E501


        :return: The im_db_rating of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._im_db_rating

    @im_db_rating.setter
    def im_db_rating(self, im_db_rating):
        """Sets the im_db_rating of this IMDbListDataDetail.


        :param im_db_rating: The im_db_rating of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._im_db_rating = im_db_rating

    @property
    def im_db_rating_count(self):
        """Gets the im_db_rating_count of this IMDbListDataDetail.  # noqa: E501


        :return: The im_db_rating_count of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._im_db_rating_count

    @im_db_rating_count.setter
    def im_db_rating_count(self, im_db_rating_count):
        """Sets the im_db_rating_count of this IMDbListDataDetail.


        :param im_db_rating_count: The im_db_rating_count of this IMDbListDataDetail.  # noqa: E501
        :type: str
        """

        self._im_db_rating_count = im_db_rating_count

    @property
    def description(self):
        """Gets the description of this IMDbListDataDetail.  # noqa: E501


        :return: The description of this IMDbListDataDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IMDbListDataDetail.


        :param description: The description of this IMDbListDataDetail.  # noqa: E501
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
        if issubclass(IMDbListDataDetail, dict):
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
        if not isinstance(other, IMDbListDataDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
