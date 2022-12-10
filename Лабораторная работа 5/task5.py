import random
import string


def get_random_password(n=8) -> str:
    password_str = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.sample(password_str, n))


print(get_random_password())
#
