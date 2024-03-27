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

class NameAwardEvent(object):
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
        'event_title': 'str',
        'name_award_event_details': 'list[NameAwardEventDetail]'
    }

    attribute_map = {
        'event_title': 'eventTitle',
        'name_award_event_details': 'nameAwardEventDetails'
    }

    def __init__(self, event_title=None, name_award_event_details=None):  # noqa: E501
        """NameAwardEvent - a model defined in Swagger"""  # noqa: E501
        self._event_title = None
        self._name_award_event_details = None
        self.discriminator = None
        if event_title is not None:
            self.event_title = event_title
        if name_award_event_details is not None:
            self.name_award_event_details = name_award_event_details

    @property
    def event_title(self):
        """Gets the event_title of this NameAwardEvent.  # noqa: E501


        :return: The event_title of this NameAwardEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_title

    @event_title.setter
    def event_title(self, event_title):
        """Sets the event_title of this NameAwardEvent.


        :param event_title: The event_title of this NameAwardEvent.  # noqa: E501
        :type: str
        """

        self._event_title = event_title

    @property
    def name_award_event_details(self):
        """Gets the name_award_event_details of this NameAwardEvent.  # noqa: E501


        :return: The name_award_event_details of this NameAwardEvent.  # noqa: E501
        :rtype: list[NameAwardEventDetail]
        """
        return self._name_award_event_details

    @name_award_event_details.setter
    def name_award_event_details(self, name_award_event_details):
        """Sets the name_award_event_details of this NameAwardEvent.


        :param name_award_event_details: The name_award_event_details of this NameAwardEvent.  # noqa: E501
        :type: list[NameAwardEventDetail]
        """

        self._name_award_event_details = name_award_event_details

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
        if issubclass(NameAwardEvent, dict):
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
        if not isinstance(other, NameAwardEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other