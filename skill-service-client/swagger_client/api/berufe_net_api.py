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


class BerufeNetApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def berufe_net_controller_get_all_jobs(self, **kwargs):  # noqa: E501
        """berufe_net_controller_get_all_jobs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_all_jobs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.berufe_net_controller_get_all_jobs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.berufe_net_controller_get_all_jobs_with_http_info(**kwargs)  # noqa: E501
            return data

    def berufe_net_controller_get_all_jobs_with_http_info(self, **kwargs):  # noqa: E501
        """berufe_net_controller_get_all_jobs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_all_jobs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method berufe_net_controller_get_all_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/berufeNet/saveJobsToLocalDB', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def berufe_net_controller_get_all_jobs_start_with(self, page, **kwargs):  # noqa: E501
        """berufe_net_controller_get_all_jobs_start_with  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_all_jobs_start_with(page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.berufe_net_controller_get_all_jobs_start_with_with_http_info(page, **kwargs)  # noqa: E501
        else:
            (data) = self.berufe_net_controller_get_all_jobs_start_with_with_http_info(page, **kwargs)  # noqa: E501
            return data

    def berufe_net_controller_get_all_jobs_start_with_with_http_info(self, page, **kwargs):  # noqa: E501
        """berufe_net_controller_get_all_jobs_start_with  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_all_jobs_start_with_with_http_info(page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method berufe_net_controller_get_all_jobs_start_with" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `berufe_net_controller_get_all_jobs_start_with`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/berufeNet/getJobsByPage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def berufe_net_controller_get_competencies_by_job_id(self, job_id, **kwargs):  # noqa: E501
        """berufe_net_controller_get_competencies_by_job_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_competencies_by_job_id(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.berufe_net_controller_get_competencies_by_job_id_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.berufe_net_controller_get_competencies_by_job_id_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def berufe_net_controller_get_competencies_by_job_id_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """berufe_net_controller_get_competencies_by_job_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_competencies_by_job_id_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method berufe_net_controller_get_competencies_by_job_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `berufe_net_controller_get_competencies_by_job_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('jobId', params['job_id']))  # noqa: E501

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
            '/berufeNet/getCompetenciesByJobId', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def berufe_net_controller_get_digital_competencies_by_job_id(self, job_id, **kwargs):  # noqa: E501
        """berufe_net_controller_get_digital_competencies_by_job_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_digital_competencies_by_job_id(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.berufe_net_controller_get_digital_competencies_by_job_id_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.berufe_net_controller_get_digital_competencies_by_job_id_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def berufe_net_controller_get_digital_competencies_by_job_id_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """berufe_net_controller_get_digital_competencies_by_job_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_digital_competencies_by_job_id_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method berufe_net_controller_get_digital_competencies_by_job_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `berufe_net_controller_get_digital_competencies_by_job_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('jobId', params['job_id']))  # noqa: E501

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
            '/berufeNet/getDigitalCompetenciesByJobId', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def berufe_net_controller_get_jobs_by_id(self, job_beruf_id, **kwargs):  # noqa: E501
        """berufe_net_controller_get_jobs_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_jobs_by_id(job_beruf_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_beruf_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.berufe_net_controller_get_jobs_by_id_with_http_info(job_beruf_id, **kwargs)  # noqa: E501
        else:
            (data) = self.berufe_net_controller_get_jobs_by_id_with_http_info(job_beruf_id, **kwargs)  # noqa: E501
            return data

    def berufe_net_controller_get_jobs_by_id_with_http_info(self, job_beruf_id, **kwargs):  # noqa: E501
        """berufe_net_controller_get_jobs_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_jobs_by_id_with_http_info(job_beruf_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_beruf_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_beruf_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method berufe_net_controller_get_jobs_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_beruf_id' is set
        if ('job_beruf_id' not in params or
                params['job_beruf_id'] is None):
            raise ValueError("Missing the required parameter `job_beruf_id` when calling `berufe_net_controller_get_jobs_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_beruf_id' in params:
            query_params.append(('JobBerufId', params['job_beruf_id']))  # noqa: E501

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
            '/berufeNet/getJobById', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def berufe_net_controller_get_jobs_by_search_string(self, search_string, **kwargs):  # noqa: E501
        """berufe_net_controller_get_jobs_by_search_string  # noqa: E501

        Getting Job Description by search string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_jobs_by_search_string(search_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_string: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.berufe_net_controller_get_jobs_by_search_string_with_http_info(search_string, **kwargs)  # noqa: E501
        else:
            (data) = self.berufe_net_controller_get_jobs_by_search_string_with_http_info(search_string, **kwargs)  # noqa: E501
            return data

    def berufe_net_controller_get_jobs_by_search_string_with_http_info(self, search_string, **kwargs):  # noqa: E501
        """berufe_net_controller_get_jobs_by_search_string  # noqa: E501

        Getting Job Description by search string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.berufe_net_controller_get_jobs_by_search_string_with_http_info(search_string, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_string: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_string']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method berufe_net_controller_get_jobs_by_search_string" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_string' is set
        if ('search_string' not in params or
                params['search_string'] is None):
            raise ValueError("Missing the required parameter `search_string` when calling `berufe_net_controller_get_jobs_by_search_string`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_string' in params:
            query_params.append(('searchString', params['search_string']))  # noqa: E501

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
            '/berufeNet/getJobBySearchString', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
