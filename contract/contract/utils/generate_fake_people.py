import random, hashlib
def people_generator(num_people):
    for i in range(num_people):
        # print(hashlib.sha224(bytes(str(i).encode('utf-8'))).hexdigest())
        person = {
                    'id': hashlib.sha224(bytes(str(i).encode('utf-8'))).hexdigest(),
                    'amount': random.randint(1000, 5000),
                    'cibil': random.randint(700, 990),
                    'KYCCheck': random.randint(0, 1),
                    'birthYear': random.randint(1980, 2003)
                }
        yield person