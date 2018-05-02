"""Small useful function to generate random string."""
import random
import string

DEFAULT_CHARS = string.ascii_lowercase + string.digits


def generate_random_string(size=20, chars=DEFAULT_CHARS):
    """Generate random string."""
    return ''.join(random.choice(chars) for _ in range(size))
