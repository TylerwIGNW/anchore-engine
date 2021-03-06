# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WhitelistItem(object):
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
        'gate': 'str',
        'trigger_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'gate': 'gate',
        'trigger_id': 'trigger_id'
    }

    def __init__(self, id=None, gate=None, trigger_id=None):  # noqa: E501
        """WhitelistItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._gate = None
        self._trigger_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.gate = gate
        self.trigger_id = trigger_id

    @property
    def id(self):
        """Gets the id of this WhitelistItem.  # noqa: E501


        :return: The id of this WhitelistItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WhitelistItem.


        :param id: The id of this WhitelistItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def gate(self):
        """Gets the gate of this WhitelistItem.  # noqa: E501


        :return: The gate of this WhitelistItem.  # noqa: E501
        :rtype: str
        """
        return self._gate

    @gate.setter
    def gate(self, gate):
        """Sets the gate of this WhitelistItem.


        :param gate: The gate of this WhitelistItem.  # noqa: E501
        :type: str
        """
        if gate is None:
            raise ValueError("Invalid value for `gate`, must not be `None`")  # noqa: E501

        self._gate = gate

    @property
    def trigger_id(self):
        """Gets the trigger_id of this WhitelistItem.  # noqa: E501


        :return: The trigger_id of this WhitelistItem.  # noqa: E501
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this WhitelistItem.


        :param trigger_id: The trigger_id of this WhitelistItem.  # noqa: E501
        :type: str
        """
        if trigger_id is None:
            raise ValueError("Invalid value for `trigger_id`, must not be `None`")  # noqa: E501

        self._trigger_id = trigger_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhitelistItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
