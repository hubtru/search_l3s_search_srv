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

class FeedbackCreationDto(object):
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
        'user_id': 'str',
        'learning_unit_id': 'str',
        'learning_value': 'float',
        'presentation': 'float',
        'comprehensiveness': 'float',
        'structure': 'float',
        'overall_rating': 'float',
        'optional_text_comment': 'str'
    }

    attribute_map = {
        'user_id': 'userID',
        'learning_unit_id': 'learningUnitID',
        'learning_value': 'learningValue',
        'presentation': 'presentation',
        'comprehensiveness': 'comprehensiveness',
        'structure': 'structure',
        'overall_rating': 'overallRating',
        'optional_text_comment': 'optionalTextComment'
    }

    def __init__(self, user_id=None, learning_unit_id=None, learning_value=None, presentation=None, comprehensiveness=None, structure=None, overall_rating=None, optional_text_comment=None):  # noqa: E501
        """FeedbackCreationDto - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._learning_unit_id = None
        self._learning_value = None
        self._presentation = None
        self._comprehensiveness = None
        self._structure = None
        self._overall_rating = None
        self._optional_text_comment = None
        self.discriminator = None
        self.user_id = user_id
        self.learning_unit_id = learning_unit_id
        self.learning_value = learning_value
        self.presentation = presentation
        self.comprehensiveness = comprehensiveness
        self.structure = structure
        self.overall_rating = overall_rating
        if optional_text_comment is not None:
            self.optional_text_comment = optional_text_comment

    @property
    def user_id(self):
        """Gets the user_id of this FeedbackCreationDto.  # noqa: E501


        :return: The user_id of this FeedbackCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FeedbackCreationDto.


        :param user_id: The user_id of this FeedbackCreationDto.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def learning_unit_id(self):
        """Gets the learning_unit_id of this FeedbackCreationDto.  # noqa: E501


        :return: The learning_unit_id of this FeedbackCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._learning_unit_id

    @learning_unit_id.setter
    def learning_unit_id(self, learning_unit_id):
        """Sets the learning_unit_id of this FeedbackCreationDto.


        :param learning_unit_id: The learning_unit_id of this FeedbackCreationDto.  # noqa: E501
        :type: str
        """
        if learning_unit_id is None:
            raise ValueError("Invalid value for `learning_unit_id`, must not be `None`")  # noqa: E501

        self._learning_unit_id = learning_unit_id

    @property
    def learning_value(self):
        """Gets the learning_value of this FeedbackCreationDto.  # noqa: E501


        :return: The learning_value of this FeedbackCreationDto.  # noqa: E501
        :rtype: float
        """
        return self._learning_value

    @learning_value.setter
    def learning_value(self, learning_value):
        """Sets the learning_value of this FeedbackCreationDto.


        :param learning_value: The learning_value of this FeedbackCreationDto.  # noqa: E501
        :type: float
        """
        if learning_value is None:
            raise ValueError("Invalid value for `learning_value`, must not be `None`")  # noqa: E501

        self._learning_value = learning_value

    @property
    def presentation(self):
        """Gets the presentation of this FeedbackCreationDto.  # noqa: E501


        :return: The presentation of this FeedbackCreationDto.  # noqa: E501
        :rtype: float
        """
        return self._presentation

    @presentation.setter
    def presentation(self, presentation):
        """Sets the presentation of this FeedbackCreationDto.


        :param presentation: The presentation of this FeedbackCreationDto.  # noqa: E501
        :type: float
        """
        if presentation is None:
            raise ValueError("Invalid value for `presentation`, must not be `None`")  # noqa: E501

        self._presentation = presentation

    @property
    def comprehensiveness(self):
        """Gets the comprehensiveness of this FeedbackCreationDto.  # noqa: E501


        :return: The comprehensiveness of this FeedbackCreationDto.  # noqa: E501
        :rtype: float
        """
        return self._comprehensiveness

    @comprehensiveness.setter
    def comprehensiveness(self, comprehensiveness):
        """Sets the comprehensiveness of this FeedbackCreationDto.


        :param comprehensiveness: The comprehensiveness of this FeedbackCreationDto.  # noqa: E501
        :type: float
        """
        if comprehensiveness is None:
            raise ValueError("Invalid value for `comprehensiveness`, must not be `None`")  # noqa: E501

        self._comprehensiveness = comprehensiveness

    @property
    def structure(self):
        """Gets the structure of this FeedbackCreationDto.  # noqa: E501


        :return: The structure of this FeedbackCreationDto.  # noqa: E501
        :rtype: float
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        """Sets the structure of this FeedbackCreationDto.


        :param structure: The structure of this FeedbackCreationDto.  # noqa: E501
        :type: float
        """
        if structure is None:
            raise ValueError("Invalid value for `structure`, must not be `None`")  # noqa: E501

        self._structure = structure

    @property
    def overall_rating(self):
        """Gets the overall_rating of this FeedbackCreationDto.  # noqa: E501


        :return: The overall_rating of this FeedbackCreationDto.  # noqa: E501
        :rtype: float
        """
        return self._overall_rating

    @overall_rating.setter
    def overall_rating(self, overall_rating):
        """Sets the overall_rating of this FeedbackCreationDto.


        :param overall_rating: The overall_rating of this FeedbackCreationDto.  # noqa: E501
        :type: float
        """
        if overall_rating is None:
            raise ValueError("Invalid value for `overall_rating`, must not be `None`")  # noqa: E501

        self._overall_rating = overall_rating

    @property
    def optional_text_comment(self):
        """Gets the optional_text_comment of this FeedbackCreationDto.  # noqa: E501


        :return: The optional_text_comment of this FeedbackCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._optional_text_comment

    @optional_text_comment.setter
    def optional_text_comment(self, optional_text_comment):
        """Sets the optional_text_comment of this FeedbackCreationDto.


        :param optional_text_comment: The optional_text_comment of this FeedbackCreationDto.  # noqa: E501
        :type: str
        """

        self._optional_text_comment = optional_text_comment

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
        if issubclass(FeedbackCreationDto, dict):
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
        if not isinstance(other, FeedbackCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other