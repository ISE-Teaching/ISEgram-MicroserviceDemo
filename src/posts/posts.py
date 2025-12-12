import random
from faker import Faker

fake = Faker()


def fake_post():
    return {
        "id": random.randint(1,100_000),
        "user_id": random.randint(1,3),
        "text": fake.text(),
    }