# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FeedbackApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def feedback_controller_add_feedback(self, body, **kwargs):  # noqa: E501
        """feedback_controller_add_feedback  # noqa: E501

        Creates a new feedback and returns it for the respective learning unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_add_feedback(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FeedbackCreationDto body: (required)
        :return: FeedbackDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.feedback_controller_add_feedback_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.feedback_controller_add_feedback_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def feedback_controller_add_feedback_with_http_info(self, body, **kwargs):  # noqa: E501
        """feedback_controller_add_feedback  # noqa: E501

        Creates a new feedback and returns it for the respective learning unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_add_feedback_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FeedbackCreationDto body: (required)
        :return: FeedbackDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method feedback_controller_add_feedback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `feedback_controller_add_feedback`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feedbacks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FeedbackDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def feedback_controller_delete_feedback(self, feedback_id, **kwargs):  # noqa: E501
        """feedback_controller_delete_feedback  # noqa: E501

        Deletes the specified feedback from the database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_delete_feedback(feedback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str feedback_id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.feedback_controller_delete_feedback_with_http_info(feedback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.feedback_controller_delete_feedback_with_http_info(feedback_id, **kwargs)  # noqa: E501
            return data

    def feedback_controller_delete_feedback_with_http_info(self, feedback_id, **kwargs):  # noqa: E501
        """feedback_controller_delete_feedback  # noqa: E501

        Deletes the specified feedback from the database  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_delete_feedback_with_http_info(feedback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str feedback_id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feedback_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method feedback_controller_delete_feedback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'feedback_id' is set
        if ('feedback_id' not in params or
                params['feedback_id'] is None):
            raise ValueError("Missing the required parameter `feedback_id` when calling `feedback_controller_delete_feedback`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'feedback_id' in params:
            path_params['feedbackId'] = params['feedback_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feedbacks/{feedbackId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def feedback_controller_get_feedback(self, feedback_id, **kwargs):  # noqa: E501
        """feedback_controller_get_feedback  # noqa: E501

        Returns the specified feedback.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_get_feedback(feedback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str feedback_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.feedback_controller_get_feedback_with_http_info(feedback_id, **kwargs)  # noqa: E501
        else:
            (data) = self.feedback_controller_get_feedback_with_http_info(feedback_id, **kwargs)  # noqa: E501
            return data

    def feedback_controller_get_feedback_with_http_info(self, feedback_id, **kwargs):  # noqa: E501
        """feedback_controller_get_feedback  # noqa: E501

        Returns the specified feedback.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_get_feedback_with_http_info(feedback_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str feedback_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feedback_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method feedback_controller_get_feedback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'feedback_id' is set
        if ('feedback_id' not in params or
                params['feedback_id'] is None):
            raise ValueError("Missing the required parameter `feedback_id` when calling `feedback_controller_get_feedback`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'feedback_id' in params:
            path_params['feedbackId'] = params['feedback_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/feedbacks/{feedbackId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def feedback_controller_list_feedback(self, learning_unit_id, **kwargs):  # noqa: E501
        """feedback_controller_list_feedback  # noqa: E501

        Lists all available feedback for the respective learning unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_list_feedback(learning_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learning_unit_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.feedback_controller_list_feedback_with_http_info(learning_unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.feedback_controller_list_feedback_with_http_info(learning_unit_id, **kwargs)  # noqa: E501
            return data

    def feedback_controller_list_feedback_with_http_info(self, learning_unit_id, **kwargs):  # noqa: E501
        """feedback_controller_list_feedback  # noqa: E501

        Lists all available feedback for the respective learning unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.feedback_controller_list_feedback_with_http_info(learning_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learning_unit_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learning_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method feedback_controller_list_feedback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learning_unit_id' is set
        if ('learning_unit_id' not in params or
                params['learning_unit_id'] is None):
            raise ValueError("Missing the required parameter `learning_unit_id` when calling `feedback_controller_list_feedback`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learning_unit_id' in params:
            path_params['learningUnitId'] = params['learning_unit_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/learning-units/{learningUnitId}/feedbacks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
