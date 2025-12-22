import requests

# The following API uses hashed psswrd but only the first 5 characters
# Never use un-hashed passwords


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res = requests.get(url)
    print(res)


def pwned_api_check(password):
    # Check password if it exists in API response
    pass
