import string
import secrets
import click

class PassGen:
    def __init__(self, length, use_symbols=True, use_uppercase=True, use_lowercase=True, use_numbers=True,):
        self.length = length
        self.use_symbols = use_symbols
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_numbers = use_numbers
        self.alphabets_small = string.ascii_lowercase if use_lowercase else ""
        self.alphabets_capital = string.ascii_uppercase if use_uppercase else ""
        self.numbers = string.digits if use_numbers else ""
        self.symbols = "!@#$%^&*()" if use_symbols else ""
        self.characters = self.alphabets_small + self.alphabets_capital + self.numbers + self.symbols

    def choose_char(self):
        return secrets.choice(self.characters)

    def generate_password(self):
        if self.length < 3:
            self.length = 3
        elif self.length > 100:
            self.length = 100

        if not self.characters:
            raise ValueError("No character types selected for password generation")

        password = []

        if self.use_lowercase:
            password.append(secrets.choice(self.alphabets_small))
        if self.use_uppercase:
            password.append(secrets.choice(self.alphabets_capital))
        if self.use_numbers:
            password.append(secrets.choice(self.numbers))
        if self.use_symbols:
            password.append(secrets.choice(self.symbols))

        while len(password) < self.length:
            password.append(self.choose_char())

        secrets.SystemRandom().shuffle(password)
        return ''.join(password[:self.length])

def strongpass(length=8 ,use_symbols=True, use_uppercase=True, use_lowercase=True, use_numbers=True) -> str:
    generator = PassGen(length, use_symbols,use_uppercase, use_lowercase, use_numbers)
    return generator.generate_password()

@click.command()
@click.option('--length', default=8, help='Length of the password.')
@click.option('--no-lowercase', is_flag=True, help='Exclude lowercase letters from the password.')
@click.option('--no-uppercase', is_flag=True, help='Exclude uppercase letters from the password.')
@click.option('--no-numbers', is_flag=True, help='Exclude numbers from the password.')
@click.option('--no-symbols', is_flag=True, help='Exclude symbols from the password.')
def generate_password(length, no_symbols, no_uppercase, no_lowercase, no_numbers):
    """Generate a strong password."""
    password = strongpass(length,not no_symbols, not no_uppercase, not no_lowercase, not no_numbers)
    click.echo(f"Generated password: {password}")

if __name__ == "__main__":
   generate_password()