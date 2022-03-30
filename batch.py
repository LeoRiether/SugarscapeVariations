from src.model import SugarscapeCg
from mesa.batchrunner import batch_run
from datetime import datetime
import numpy as np
import pandas as pd
import sys
import os

def run(split=1, debug=False):

    params = {
        "reproduce_prob": np.linspace(0, 0.6, 13),
        "growback_factor": 0.15,
    }

    iterations = 500
    steps = 100

    if debug:
        params["reproduce_prob"] = 0.15
        iterations = 2
        steps = 5

    for i in range(split):
        results = batch_run(
            SugarscapeCg,
            params,
            iterations=iterations // split,
            max_steps=steps,
            number_processes=None,
            data_collection_period=-1,
        )

        dataframe = pd.DataFrame(results)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

        # Create csv filename
        fn = "data"
        fn += "_t{}.csv".format(timestamp)

        os.makedirs("csv", exist_ok=True)
        dataframe.drop(['SsAgent'], axis=1).to_csv(os.path.join("csv", 'model_' + fn))
        dataframe.drop(['Oscillation', 'Average'], axis=1).to_csv(os.path.join("csv", 'agent_' + fn))

def join(files):
    """ Concatena vários dataframes em um só """
    frame = pd.read_csv(files[0]).drop('Unnamed: 0', axis=1)
    max_id = frame['RunId'].max()
    for f in files[1:]:
        frame2 = pd.read_csv(f).drop('Unnamed: 0', axis=1)
        frame2['RunId'] = frame2['RunId'].map(lambda x: x + max_id)
        max_id = max(max_id, frame2['RunId'].max())
        frame = pd.concat([ frame, frame2 ])
    return frame

# files = [ e.path for e in os.scandir('agent') ]
# join(files).to_csv("AGENT.csv")
# files = [ e.path for e in os.scandir('model') ]
# join(files).to_csv("MODEL.csv")

if __name__ == '__main__':
    if sys.argv[-1] == '--debug':
        run(debug=True)
    elif sys.argv[-1] == '--split':
        run(split=20)
    else:
        run()
