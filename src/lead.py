class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.leads = []


    def __repr__(self):
        return f'{self.name} / {self.email} / {self.phone}'
