import random 
from enum import Enum
class TimeoutError(Exception):
    pass
class ConditionsError(Exception):
    pass

class EnumRequest(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'

class NewRequest(Enum):
    OK = 'OK'
    CREATED = 'CREATED'
    BAD_REQUEST = 'BAD_REQUEST'
    NOT_FOUND = 'NOT_FOUND'
    NOT_AUTH = 'NOT_AUTH'

class Response:
    def __init__(self, url: str, params: dict, status: int, timeout: int, method:str):
        self._url = url
        self.params = params 
        self.status = status 
        self.timeout = timeout 
        self.method = method
        self.status_text_addiction()
    
    def status_text_addiction(self): 
        if self.status == 200 and self.method == EnumRequest.GET.value:
            self.status_text = NewRequest.OK 
            return NewRequest.OK
        elif self.status == 201 and self.method == EnumRequest.POST.value:
            self.status_text = NewRequest.CREATED
            return NewRequest.CREATED
        elif self.status == 400:
            self.status_text = NewRequest.BAD_REQUEST
            return NewRequest.BAD_REQUEST 
        elif self.status == 404:
            self.status_text = NewRequest.NOT_FOUND
            return NewRequest.NOT_FOUND
        elif self.status == 401:
            self.status_text = NewRequest.NOT_AUTH
            return NewRequest.NOT_AUTH
        elif self.timeout > 5:
            raise TimeoutError ('timeout can not be more than 5')
    
def retry(max_attemps):
    def wreaper(func):
        def inner(*args, **kwargs):
            counter = 0
            response = func(*args, **kwargs)
            while response.status not in {200, 201}:
                response = func(*args, **kwargs)
                counter +=1
                if counter >max_attemps:
                    print('проверка работы декоратора')
                    break
            return response
        return inner
    return wreaper

@retry(5)
def controller(url: str, params: dict, status: int, timeout: int, method: str):
    response = Response(url=url, params=params, status=status, timeout=timeout, method=method)
    return response


for i in range(10):
    url = 'http://example.com'
    params = {'param1': 'value1', 'param2': 'value2'}
    status = random.choice([200,201,400,401,404])
    timeout = random.randrange(1, 11) 
    method = random.choice(['GET', 'POST'])
    print(url,params,status,timeout,method)
    controller(url=url, params=params, status=status, timeout=timeout, method=method) 
        
