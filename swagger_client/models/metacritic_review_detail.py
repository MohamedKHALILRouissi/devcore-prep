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

class MetacriticReviewDetail(object):
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
        'publisher': 'str',
        'author': 'str',
        'link': 'str',
        'rate': 'str',
        'content': 'str'
    }

    attribute_map = {
        'publisher': 'publisher',
        'author': 'author',
        'link': 'link',
        'rate': 'rate',
        'content': 'content'
    }

    def __init__(self, publisher=None, author=None, link=None, rate=None, content=None):  # noqa: E501
        """MetacriticReviewDetail - a model defined in Swagger"""  # noqa: E501
        self._publisher = None
        self._author = None
        self._link = None
        self._rate = None
        self._content = None
        self.discriminator = None
        if publisher is not None:
            self.publisher = publisher
        if author is not None:
            self.author = author
        if link is not None:
            self.link = link
        if rate is not None:
            self.rate = rate
        if content is not None:
            self.content = content

    @property
    def publisher(self):
        """Gets the publisher of this MetacriticReviewDetail.  # noqa: E501


        :return: The publisher of this MetacriticReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this MetacriticReviewDetail.


        :param publisher: The publisher of this MetacriticReviewDetail.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def author(self):
        """Gets the author of this MetacriticReviewDetail.  # noqa: E501


        :return: The author of this MetacriticReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this MetacriticReviewDetail.


        :param author: The author of this MetacriticReviewDetail.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def link(self):
        """Gets the link of this MetacriticReviewDetail.  # noqa: E501


        :return: The link of this MetacriticReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this MetacriticReviewDetail.


        :param link: The link of this MetacriticReviewDetail.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def rate(self):
        """Gets the rate of this MetacriticReviewDetail.  # noqa: E501


        :return: The rate of this MetacriticReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this MetacriticReviewDetail.


        :param rate: The rate of this MetacriticReviewDetail.  # noqa: E501
        :type: str
        """

        self._rate = rate

    @property
    def content(self):
        """Gets the content of this MetacriticReviewDetail.  # noqa: E501


        :return: The content of this MetacriticReviewDetail.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MetacriticReviewDetail.


        :param content: The content of this MetacriticReviewDetail.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if issubclass(MetacriticReviewDetail, dict):
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
        if not isinstance(other, MetacriticReviewDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
