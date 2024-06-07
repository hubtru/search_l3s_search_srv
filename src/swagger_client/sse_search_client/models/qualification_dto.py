# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class QualificationDto(object):
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
        '_date': 'datetime',
        'berufenet_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        '_date': 'date',
        'berufenet_id': 'berufenetID'
    }

    def __init__(self, id=None, title=None, _date=None, berufenet_id=None):  # noqa: E501
        """QualificationDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self.__date = None
        self._berufenet_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.title = title
        self._date = _date
        if berufenet_id is not None:
            self.berufenet_id = berufenet_id

    @property
    def id(self):
        """Gets the id of this QualificationDto.  # noqa: E501


        :return: The id of this QualificationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QualificationDto.


        :param id: The id of this QualificationDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this QualificationDto.  # noqa: E501


        :return: The title of this QualificationDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this QualificationDto.


        :param title: The title of this QualificationDto.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def _date(self):
        """Gets the _date of this QualificationDto.  # noqa: E501


        :return: The _date of this QualificationDto.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this QualificationDto.


        :param _date: The _date of this QualificationDto.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def berufenet_id(self):
        """Gets the berufenet_id of this QualificationDto.  # noqa: E501


        :return: The berufenet_id of this QualificationDto.  # noqa: E501
        :rtype: str
        """
        return self._berufenet_id

    @berufenet_id.setter
    def berufenet_id(self, berufenet_id):
        """Sets the berufenet_id of this QualificationDto.


        :param berufenet_id: The berufenet_id of this QualificationDto.  # noqa: E501
        :type: str
        """

        self._berufenet_id = berufenet_id

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
        if issubclass(QualificationDto, dict):
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
        if not isinstance(other, QualificationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
