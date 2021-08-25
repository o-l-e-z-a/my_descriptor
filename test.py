import unittest
from user import User


class MyTestCase(unittest.TestCase):
    def test_fail_last_name(self):
        with self.assertRaises(ValueError):
            user = User(
                last_name='oleg',  # с маленькой буквы
                first_name='Oleg',
                email='mail@yandex.ru',
                date_birthday='22.02.2220',
                telephone='+79812395017')

    def test_fail_email(self):
        with self.assertRaises(ValueError):
            user = User(
                last_name='Oleg',
                first_name='Oleg',
                email='mail@.ru',
                date_birthday='22.02.2220',
                telephone='+79812695017')

    def test_fail_date(self):
        with self.assertRaises(ValueError):
            user = User(
                last_name='Oleg',
                first_name='Oleg',
                email='mail@yandex.ru',
                date_birthday='22.13.2220',
                telephone='+79812695017')

    def test_fail_phone(self):
        with self.assertRaises(ValueError):
            user = User(
                last_name='Oleg',
                first_name='Oleg',
                email='mail@mail.ru',
                date_birthday='22.12.2220',
                telephone='+7981269501712121')

    def test_valid_user(self):
        try:
            user = User(
                last_name='Oleg',
                first_name='Oleg',
                email='mail@mail.ru',
                date_birthday='22.12.2220',
                telephone='+79812695017')
        except ValueError:
            self.fail('Ошибка в данных')


if __name__ == '__main__':
    unittest.main()
