import abc
import re


class AutoStorage:
    __id = 0

    def __init__(self):
        cls = self.__class__
        self.storage_name = f'_{cls.__name__}№{cls.__id}'
        cls.__id += 1

    def __get__(self, instance, owner):
        if isinstance:
            return getattr(instance, self.storage_name)
        else:
            return instance

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validate(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """ Возвращает проверенное значение или ValueError"""


class CharField(Validate):
    """ Возвращает проверенное значение или ValueError"""

    def validate(self, instance, value):
        char = re.compile(r"^([А-ЯЁ][а-яё,.'-]+|[A-Z][a-z,.'-]+)$")
        if char.fullmatch(value):
            return value
        else:
            raise ValueError('Не корректный ввод')


class EmailField(Validate):
    """ Возвращает проверенное значение или ValueError"""

    def validate(self, instance, value):
        email = re.compile(r"^[\w!#$%&'*+\-/=?\^_`{|}~]+(\.[\w!#$%&'*+\-/=?\^_`{|}~]+)*"
                           r"@"
                           r"((([\-\w]+\.)+[a-zA-Z]{2,4})|(([0-9]{1,3}\.){3}[0-9]{1,3}))$", re.I)
        if email.fullmatch(value):
            return value
        else:
            raise ValueError('E-mail не корректный')


class PhoneField(Validate):
    """ Возвращает проверенное значение или ValueError"""

    def validate(self, instance, value):
        phone = re.compile(r"^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$")
        if phone.fullmatch(value):
            return value
        else:
            raise ValueError('Номер телефона не корректный')


class DateField(Validate):
    """ Возвращает проверенное значение или ValueError"""

    def validate(self, instance, value):
        date = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)"
                          r"(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))"
                          r"(?:(?:1[6-9]|[2-9]\d)?\d{"r"2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?"
                          r"(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|"
                          r"2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|"
                          r"(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
        if date.fullmatch(value):
            return value
        else:
            raise ValueError('Только буквы')
