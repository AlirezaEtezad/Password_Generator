import unittest
from password_generator.password_generator import PassGen, strongpass

class TestPassGen(unittest.TestCase):
    def test_generate_password_default_length(self):
        pg = PassGen(length=8)
        password = pg.generate_password()
        self.assertEqual(len(password), 8)

    def test_generate_password_custom_length(self):
        pg = PassGen(length=12)
        password = pg.generate_password()
        self.assertEqual(len(password), 12)

    def test_generate_password_with_no_lowercase(self):
        pg = PassGen(length=10, use_lowercase=False)
        password = pg.generate_password()
        self.assertTrue(all(char.islower() == False for char in password))

    def test_generate_password_with_no_uppercase(self):
        pg = PassGen(length=10, use_uppercase=False)
        password = pg.generate_password()
        self.assertTrue(all(char.isupper() == False for char in password))

    def test_generate_password_with_no_numbers(self):
        pg = PassGen(length=10, use_numbers=False)
        password = pg.generate_password()
        self.assertTrue(all(char.isdigit() == False for char in password))

    def test_generate_password_with_no_symbols(self):
        pg = PassGen(length=10, use_symbols=False)
        password = pg.generate_password()
        self.assertTrue(all(char not in '!@#$%^&*()' for char in password))

    def test_strongpass_default_length(self):
        password = strongpass()
        self.assertEqual(len(password), 8)

    def test_strongpass_custom_length(self):
        password = strongpass(length=12)
        self.assertEqual(len(password), 12)

if __name__ == '__main__':
    unittest.main()
