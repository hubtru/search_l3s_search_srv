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

class UserDto(object):
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
        'learning_profile': 'str',
        'career_profile': 'str',
        'company_id': 'str',
        'status': 'object',
        'qualification': 'list[str]',
        'job': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'learning_profile': 'learningProfile',
        'career_profile': 'careerProfile',
        'company_id': 'companyId',
        'status': 'status',
        'qualification': 'qualification',
        'job': 'job'
    }

    def __init__(self, id=None, name=None, learning_profile=None, career_profile=None, company_id=None, status=None, qualification=None, job=None):  # noqa: E501
        """UserDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._learning_profile = None
        self._career_profile = None
        self._company_id = None
        self._status = None
        self._qualification = None
        self._job = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if learning_profile is not None:
            self.learning_profile = learning_profile
        if career_profile is not None:
            self.career_profile = career_profile
        if company_id is not None:
            self.company_id = company_id
        if status is not None:
            self.status = status
        if qualification is not None:
            self.qualification = qualification
        if job is not None:
            self.job = job

    @property
    def id(self):
        """Gets the id of this UserDto.  # noqa: E501


        :return: The id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDto.


        :param id: The id of this UserDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserDto.  # noqa: E501


        :return: The name of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserDto.


        :param name: The name of this UserDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def learning_profile(self):
        """Gets the learning_profile of this UserDto.  # noqa: E501


        :return: The learning_profile of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._learning_profile

    @learning_profile.setter
    def learning_profile(self, learning_profile):
        """Sets the learning_profile of this UserDto.


        :param learning_profile: The learning_profile of this UserDto.  # noqa: E501
        :type: str
        """

        self._learning_profile = learning_profile

    @property
    def career_profile(self):
        """Gets the career_profile of this UserDto.  # noqa: E501


        :return: The career_profile of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._career_profile

    @career_profile.setter
    def career_profile(self, career_profile):
        """Sets the career_profile of this UserDto.


        :param career_profile: The career_profile of this UserDto.  # noqa: E501
        :type: str
        """

        self._career_profile = career_profile

    @property
    def company_id(self):
        """Gets the company_id of this UserDto.  # noqa: E501


        :return: The company_id of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this UserDto.


        :param company_id: The company_id of this UserDto.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def status(self):
        """Gets the status of this UserDto.  # noqa: E501


        :return: The status of this UserDto.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserDto.


        :param status: The status of this UserDto.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def qualification(self):
        """Gets the qualification of this UserDto.  # noqa: E501


        :return: The qualification of this UserDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._qualification

    @qualification.setter
    def qualification(self, qualification):
        """Sets the qualification of this UserDto.


        :param qualification: The qualification of this UserDto.  # noqa: E501
        :type: list[str]
        """

        self._qualification = qualification

    @property
    def job(self):
        """Gets the job of this UserDto.  # noqa: E501


        :return: The job of this UserDto.  # noqa: E501
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this UserDto.


        :param job: The job of this UserDto.  # noqa: E501
        :type: str
        """

        self._job = job

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
        if issubclass(UserDto, dict):
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
        if not isinstance(other, UserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other