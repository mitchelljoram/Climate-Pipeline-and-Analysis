'''
CLIMATIQ -> POSTGRES PIPELINE
'''

import requests

'''
API
'''
# Change this to be your API key
MY_API_KEY="ZBPQ1K1FXVM2EMGRVY5CPJG0KFRQ"

BASE_URL = "https://beta4.api.climatiq.io/estimate"

# The activity ID for the emission factor. You can find this via the search endpoint listed above
# or via the Data Explorer.
activity_id = "electricity-supply_grid-source_supplier_mix"

# We have many regions with the same activity id, representing the power grid in different countries.
# We'd like to get the power for Australia specifically, so we will need to specify a region.
# We do this by specifying the UN location code for the region
# You can also see the region for different emission factors in the data explorer.
region = "US"

# We provide a data version on which we want to base our calculation. The recommended approach
# is to use the latest version.
data_version = "^1"

# We must also specify how much electricity generation we would like to make the estimation for.
# In this case we will do it for 100 kilowatt-hours.
# Different emission factors have different requirement as to what units they support estimates for.
# You can see the units supported by an emission factor in the data explorer
# and find more documentation about units
# in the API documentation.
parameters = {
    "energy": 100,
    "energy_unit": "kWh"
}

json_body = {
    "emission_factor": {
        "activity_id": activity_id,
        "data_version": data_version,
        "region": region,
        "year": 2020,
    },
    # Specify how much energy we're estimating for
    "parameters": parameters
}

# You must always specify your AUTH token in the "Authorization" header like this.
authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

# We send a POST request to the estimate endpoint with a json body
# and the correct authorization headers.
# This line will send the request and retrieve the body as JSON.
response = requests.post(BASE_URL, json=json_body, headers=authorization_headers).json()

# You can now do anything you want with the response
print(response)