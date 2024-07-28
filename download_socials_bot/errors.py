class UnknownService(Exception):
    def __init__(self):
        self.message = "Данный сервис не поддерживается"
        super().__init__(self.message)