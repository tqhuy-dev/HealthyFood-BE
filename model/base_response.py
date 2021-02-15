class SuccessResponseDto:
    def __init__(self, code, data):
        self.code = code
        self.data = data


class ErrorResponseDto:
    def __init__(self, code, message):
        self.code = code
        self.message = message
