from src.model import SugarscapeCg
from mesa.batchrunner import batch_run
from datetime import datetime
import numpy as np
import pandas as pd
import sys
import os

def run(debug=False):

    params = {
        "reproduce_prob": np.linspace(0, 0.5, 11),
        "growback_factor": [0.15],
    }

    iterations = 300
    steps = 100

    if debug:
        params["reproduce_prob"] = [0.15]
        iterations = 2
        steps = 5

    results = batch_run(
        SugarscapeCg,
        params,
        iterations=iterations,
        max_steps=steps,
        number_processes=None,
        data_collection_period=-1,
    )

    dataframe = pd.DataFrame(results)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    # Create csv filename
    fn = "data"
    # if type(rp) != list:
    #     fn += "_rp{}".format(rp)
    # if type(gf) != list:
    #     fn += "_gf{}".format(gf)
    fn += "_t{}.csv".format(timestamp)

    os.makedirs("csv", exist_ok=True)
    dataframe.drop(['SsAgent'], axis=1).to_csv(os.path.join("csv", 'model_' + fn))
    dataframe.drop(['Oscillation', 'Average'], axis=1).to_csv(os.path.join("csv", 'agent_' + fn))

if __name__ == '__main__':
    if sys.argv[-1] == '--debug':
        run(debug=True)
    else:
        run()
