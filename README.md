# Scammerzz - ScamSearchAPI Python Client

This is a Python client for the ScamSearchAPI. It provides functions to search for scam reports and report scammers.

## Installation

To use this client, you need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

You also need to install the `requests` library. You can install it using pip:

```
pip install requests
```

## Usage

To use this client, you need to have an API key for the ScamSearchAPI. You can get an API key by signing up on the ScamSearch website: https://scamsearch.io/

Once you have an API key, you can use the `ScamSearchAPI` class to perform searches and report scammers.

Store the API key in SS_API_KEY enviromental variable or in api.txt file.

### Performing an exact search

To perform an exact search, you can use the `search_exact_match` function. This function takes three parameters:

- `search_term`: The term you want to search for.
- `search_type`: The type of search you want to perform. This can be one of the following values: `all`, `bitcoin_address`, `scammer_username`, `scammer_email`, `scammer_phone`, `scam_description`.

Here's an example:

```python
from api import ScamSearchAPI

# create an instance of the ScamSearchAPI class
api = ScamSearchAPI()

# perform an exact search for a bitcoin address
res = api.search_exact_match('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2', 'bitcoin_address')

# print the results
print(res)
```

### Performing a wildcard search

To perform a wildcard search, you can use the `search_wild_card` function. This function takes the same parameters as the `search_exact_match` function.

Here's an example:

```python
from api import ScamSearchAPI

# create an instance of the ScamSearchAPI class
api = ScamSearchAPI()

# perform a wildcard search for a scammer email
res = api.search_wild_card('example.com', 'scammer_email')

# print the results
print(res)
```

### Reporting a scammer

To report a scammer, you can use the `report_scammer` function. This function takes the following parameters:

- `bitcoin_address`: The bitcoin address used by the scammer.
- `scam_type`: The type of scam. This can be one of the following values: `phishing`, `ponzi`, `scareware`, `ransomware`, `tech_support`, `other`.
- `scammer_username` (optional): The username used by the scammer.
- `scammer_email` (optional): The email address used by the scammer.
- `scammer_phone` (optional): The phone number used by the scammer.
- `scam_description` (optional): A description of the scam.

Here's an example:

```python
from api import ScamSearchAPI

# create an instance of the ScamSearchAPI class
api = ScamSearchAPI()

# report a scammer
res = api.report_scammer('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2', 'phishing', scammer_email='example@example.com', scam_description='This is a phishing scam.')

# print the response
print(res)
```

## License

This client is licensed under the GNU v3. See the LICENSE file for more information.
