class Mail:
    __DOMAIN_LIST = ['mail.com','mail.cc','mail-archive.com','mail.org','mail.com']
    def __init__(self):
        self.mail = ''

    @staticmethod
    def __validate(value):
        domain = value.split('@')[1]
        if domain not in Mail.__DOMAIN_LIST:
            raise ValueError('Invalid domain')
        elif len(value.split('@')) > 2:
            raise ValueError('Invalid domain')
        return value

    @property
    def valid_domain(self):
        return f'Domain is valid: {self.mail}'

    @valid_domain.setter
    def valid_domain(self,mail):
        self.mail = Mail.__validate(mail)
