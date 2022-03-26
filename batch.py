from src.model import SugarscapeCg
from mesa.batchrunner import batch_run
from datetime import datetime
import numpy as np
import pandas as pd
import sys
import os

def run(split=1, debug=False):

    params = {
        "reproduce_prob": np.linspace(0, 0.65, 12),
        "growback_factor": 0.15,
    }

    iterations = 300
    steps = 100

    if debug:
        params["reproduce_prob"] = 0.15
        iterations = 2
        steps = 5

    for i in range((iterations + split - 1) // split):
        print("starting results")

        results = batch_run(
            SugarscapeCg,
            params,
            iterations=iterations // split,
            max_steps=steps,
            number_processes=None,
            data_collection_period=-1,
        )

        print("results ok")

        dataframe = pd.DataFrame(results)

        print("dataframe ok")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

        print("timestamp ok")

        # Create csv filename
        fn = "data"
        # if type(rp) != list:
        #     fn += "_rp{}".format(rp)
        # if type(gf) != list:
        #     fn += "_gf{}".format(gf)
        fn += "_t{}.csv".format(timestamp)

        print("fn ok")

        os.makedirs("csv", exist_ok=True)
        print("makedir ok")
        dataframe.drop(['SsAgent'], axis=1).to_csv(os.path.join("csv", 'model_' + fn))
        print("model_ ok")
        dataframe.drop(['Oscillation', 'Average'], axis=1).to_csv(os.path.join("csv", 'agent_' + fn))
        print("agent_ ok")


if __name__ == '__main__':
    if sys.argv[-1] == '--debug':
        run(debug=True)
    if sys.argv[-1] == '--split':
        run(split=10)
    else:
        run()
