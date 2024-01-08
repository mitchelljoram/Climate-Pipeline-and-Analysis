'''
CLIMATIQ API
'''

import requests

# Change this to be your API key
MY_API_KEY="ZBPQ1K1FXVM2EMGRVY5CPJG0KFRQ"

BASE_URL = "https://beta4.api.climatiq.io/estimate"

# The activity ID for the emission factor.
activity_id = "electricity-supply_grid-source_supplier_mix"

# We have many regions with the same activity id, representing the power grid in different countries.
# We'd like to get the power for Australia specifically, so we will need to specify a region.
# We'd like to get the power for US States specifically, so we will need to specify each region.
# We do this by specifying the US postal code for the region.
states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

# We provide a data version on which we want to base our calculation. The recommended approach
# is to use the latest version.
data_version = "^3"

# We must also specify how much electricity generation we would like to make the estimation for.
# In this case we will do it for 100 kilowatt-hours.
# Different emission factors have different requirement as to what units they support estimates for.
# You can see the units supported by an emission factor in the data explorer
# and find more documentation about units in the API documentation.
parameters = {
    "energy": 100,
    "energy_unit": "kWh"
}

# You must always specify your AUTH token in the "Authorization" header like this.
authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

# Extract
def extract():
    try: 
        print("Extracting data from Climatiq API...")

        raw = []
        for state in states:
            json_body = {
                "emission_factor": {
                    "activity_id": activity_id,
                    "data_version": data_version,
                    "region": f"US-{state}",
                    "year": 2022,
                },
                # Specify how much energy we're estimating for
                "parameters": parameters
            }
            # We send a POST request to the estimate endpoint with a json body
            # and the correct authorization headers.
            # This line will send the request and retrieve the body as JSON.

            response = requests.post(BASE_URL, json=json_body, headers=authorization_headers).json()
            
            raw.append({"state":state, "estimate":response})

        print("Finished extracting data from Climatiq API.")
        return raw
    except Exception as e:
        print("Extraction error: " + str(e))


# Test Climatiq API
def test():
    test_data = []
    for state in states:
        json_body = {
            "emission_factor": {
                "activity_id": activity_id,
                "data_version": data_version,
                "region": f"US-{state}",
                "year": 2022,
            },
            "parameters": parameters
        }

        response = requests.post(BASE_URL, json=json_body, headers=authorization_headers).json()
        
        test_data.append({"state":state, "estimate":response})

    print(test_data)


# try:
#     print("Executing Climatiq API test...")
#     test()
#     print("Finished Climatiq API test...")
# except Exception as e:
#     print("Test error: " + str(e))