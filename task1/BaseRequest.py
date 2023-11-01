from enum import Enum
import re

class EnumRequest(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'

class BaseRequest:
    def __init__(self, url: str, method: EnumRequest, params: dict=None, body: dict=None):
        self.url = self.validate_url(url)
        self.method = method
        self.params = params
        self.body = self.validate_body(body)

    def validate_body(self, body: dict = None): #проверяем валидность условия body 
        if self.method != EnumRequest.POST and body is not None:
            raise Exception('method must be POST or body must be not None')
        return body

    def validate_url(self, url): #проверяем валидность url 
        pattern = r'^https?://[a-zA-Z0-9.-]+(/[\S]*)?$'
        if not re.match(pattern, url):
            raise Exception('pattern is not true')
        return url

    def validate_get_post(self, method, url): #вторая часть задачи
        without_body = r'^https?://[a-zA-Z0-9.-]'
        with_body = r'^https?://[a-zA-Z0-9.-]+(/[\S]*)?$'
        if method == EnumRequest.GET and re.match(without_body, url):
            return url
        elif method == EnumRequest.POST and re.match(with_body, url):
            return url 
        else:
            raise Exception('conditions are not right')

class Request(BaseRequest): #проверка кол-ва параметров
    MAX_PARAMS = 5

    def validate_params(self, params: dict=None): 
        value=super().validate_params(params)
        if len(value) >= Request.MAX_PARAMS:
            raise ValueError('len of params mast be <=5')
        return value
    
