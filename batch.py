from src.model import batch_run
import sys

if sys.argv[-1] == '--debug':
    batch_run(
        rp=[0.05],
        gf=[0.5],
    )
else:
    batch_run()
