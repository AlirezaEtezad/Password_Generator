# Password Generator

Ete_Pass is a strong password generator with customizable character types and length.

## Features

- Generate passwords of desired length. (Min3, Max100)
- Include or exclude lowercase letters, uppercase letters, numbers, and symbols.
- command line accessabitly.

## Installation

```sh
pip install ete_pass
```

## Usage:
```sh
from ete_pass import strongpass
```

### Generate a password of length 12 with all character types
```sh
password = strongpass(12)
print(password)
```
### Generate a password of length 16 with only numbers and symbols
```sh
password = strongpass(16, use_symbols=True, use_uppercase=False, use_lowercase=False, use_numbers=True)
print(password)
```


### CLI orders:
  -  --length: Length of the password (default is 8).
  -  --no-symbols: Exclude symbols from the password.
  -  --no-uppercase: Exclude uppercase letters from the password.
  -  --no-lowercase: Exclude lowercase letters from the password.
  -  --no-numbers: Exclude numbers from the password.

### Example:
```sh
generate-password length=16 --no-symbols --no-uppercase --no-lowercase
```
It will generate a password only made of digits with the length of 16
