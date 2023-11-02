from task1.BaseRequest import BaseRequest
import random 
from enum import Enum

class LenError(Exception):
    pass

class NewRequest(Enum):
    OK = 'OK'
    CREATED = 'CREATED'
    BAD_REQUEST = 'BAD_REQUEST'
    NOT_FOUND = 'NOT_FOUND'
    NOT_AUTH = 'NOT_AUTH'

class Response:
    def __init__(self, url: str, params: dict, status: int, timeout: int, status_text: str, content: str):
        self._url = url
        self.params = params 
        self.status = status 
        self.timeout = timeout 
        self.status_text = status_text
        self.content = content
    
    def status_text_addiction(self): #какие аргументы? 
        if self.status == 200 and self.method == BaseRequest.GET:
            self.status_text = NewRequest.OK 
            return NewRequest.OK
        if self.status == 201 and self.method == BaseRequest.POST:
            self.status_text = NewRequest.CREATED
            return NewRequest.CREATED
        if self.status == 400:
            self.status_text = NewRequest.BAD_REQUEST
            return NewRequest.BAD_REQUEST 
        if self.status == 404:
            self.status_text = NewRequest.NOT_FOUND
            return NewRequest.NOT_FOUND
        if self.status == 401:
            self.status_text = NewRequest.NOT_AUTH
            return NewRequest.NOT_AUTH
        if self.timeout > 5:
            raise TimeoutError ('timeout can not be more than 5')
        else: 
            raise Exception ('condition is not met')
    
def retry(func):
    def wreaper(max_attemps):
        def inner(*args, **kwargs):
            counter = 0
            response = func(*args, **kwargs)
            while response.status not in {200, 201}:
                response = func(*args, **kwargs)
                counter +=1
                if counter >max_attemps:
                    break
            return response
        return inner
    return wreaper

@retry 
def controller(url: str, params: dict, status: int, timeout: int, status_text: str):
    response = Response()
    return response


for i in range(10):
    url = 'http://example.com'
    params = {'param1': 'value1', 'param2': 'value2'}
    timeout = random.randrange(1, 11) 
    method = random.choice(['GET', 'POST'])
    status = random.choice([200,201,400,401,404])
    controller(url, params, timeout, method, status) 
    
