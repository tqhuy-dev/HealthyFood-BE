class SuccessResponseDto(object):
    def __init__(self, code, data):
        self.code = code
        self.data = data


class ErrorResponseDto(object):
    def __init__(self, code, message):
        self.code = code
        self.message = message
