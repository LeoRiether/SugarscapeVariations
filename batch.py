from src.model import SugarscapeCg
from mesa.batchrunner import batch_run
from datetime import datetime
import numpy as np
import pandas as pd
import sys
import os

def run(
    rp=np.linspace(0, 0.5, 11),
    gf=[0.15],
):

    params = {
        "reproduce_prob": rp,
        "growback_factor": gf,
    }

    iterations = 300
    steps = 100

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
    dataframe.to_csv(os.path.join("csv", fn))

if __name__ == '__main__':
    if sys.argv[-1] == '--debug':
        run(rp=[0.15])
    else:
        run()
