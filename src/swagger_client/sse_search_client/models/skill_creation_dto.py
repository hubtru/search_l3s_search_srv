# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SkillCreationDto(object):
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
        'owner': 'str',
        'name': 'str',
        'level': 'float',
        'description': 'str',
        'nested_skills': 'list[str]'
    }

    attribute_map = {
        'owner': 'owner',
        'name': 'name',
        'level': 'level',
        'description': 'description',
        'nested_skills': 'nestedSkills'
    }

    def __init__(self, owner=None, name=None, level=None, description=None, nested_skills=None):  # noqa: E501
        """SkillCreationDto - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._name = None
        self._level = None
        self._description = None
        self._nested_skills = None
        self.discriminator = None
        self.owner = owner
        self.name = name
        self.level = level
        if description is not None:
            self.description = description
        self.nested_skills = nested_skills

    @property
    def owner(self):
        """Gets the owner of this SkillCreationDto.  # noqa: E501

        Used to validate that the user is the owner of the target repository.  # noqa: E501

        :return: The owner of this SkillCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SkillCreationDto.

        Used to validate that the user is the owner of the target repository.  # noqa: E501

        :param owner: The owner of this SkillCreationDto.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def name(self):
        """Gets the name of this SkillCreationDto.  # noqa: E501


        :return: The name of this SkillCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SkillCreationDto.


        :param name: The name of this SkillCreationDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def level(self):
        """Gets the level of this SkillCreationDto.  # noqa: E501


        :return: The level of this SkillCreationDto.  # noqa: E501
        :rtype: float
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SkillCreationDto.


        :param level: The level of this SkillCreationDto.  # noqa: E501
        :type: float
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def description(self):
        """Gets the description of this SkillCreationDto.  # noqa: E501


        :return: The description of this SkillCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SkillCreationDto.


        :param description: The description of this SkillCreationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def nested_skills(self):
        """Gets the nested_skills of this SkillCreationDto.  # noqa: E501


        :return: The nested_skills of this SkillCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._nested_skills

    @nested_skills.setter
    def nested_skills(self, nested_skills):
        """Sets the nested_skills of this SkillCreationDto.


        :param nested_skills: The nested_skills of this SkillCreationDto.  # noqa: E501
        :type: list[str]
        """
        if nested_skills is None:
            raise ValueError("Invalid value for `nested_skills`, must not be `None`")  # noqa: E501

        self._nested_skills = nested_skills

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
        if issubclass(SkillCreationDto, dict):
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
        if not isinstance(other, SkillCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other