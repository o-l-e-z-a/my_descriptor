import models


class User:
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    telephone = models.PhoneField()
    date_birthday = models.DateField()

    def __init__(self, first_name, last_name, email, telephone, date_birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone
        self.date_birthday = date_birthday

    def __str__(self):
        return self.first_name + ' ' + self.last_name
