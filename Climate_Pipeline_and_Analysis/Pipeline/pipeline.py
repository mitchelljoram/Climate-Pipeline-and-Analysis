'''
CLIMATIQ API -> POSTGRES PIPELINE
'''

from api import extract
from postgres import load

#TODO: Transform
def transform(raw):
    try:
        print("Transforming data...")

        data = []
        for raw_state in raw:
            s = f"{raw_state['state']}"

            estimate = raw_state['estimate']
            y = 2022
            a = estimate['emission_factor']['source_lca_activity']
            av = estimate['activity_data']['activity_value']
            au = f"{estimate['activity_data']['activity_unit']}"
            c = estimate['co2e']
            cu = f"{estimate['co2e_unit']}"

            state = {
                "state": s,
                "year": y,
                "activity": a,
                "activity_value": av,
                "activity_unit": au,
                "co2e": c,
                "co2e_unit": cu
            }

            data.append(state)

        print("Finished transforming data.")
        return data
    except Exception as e:
        print("Transformation error: " + str(e))


def pipeline():
    print("Executing pipeline...")

    raw = extract()
    data = transform(raw)
    load(data)

    print("Pipeline executed!")

try:
    pipeline()
except Exception as e:
    print("Pipeline error: " + str(e))