from sqlitecallback import SqliteCallback
from bucketing import Bucketing
from policytree import *
import time, sys

if __name__ == "__main__":
    sqlite_callback = SqliteCallback(sys.argv[1])
    
    start = time.time()
    bucketing_worker = Bucketing()
    buckets = bucketing_worker.analyze(sqlite_callback)
    bucketing_worker.export_to_csv(buckets)
    end = time.time()

    sqlite_callback.close()
    
    print(f"Time elapsed analyzing: {end-start}")
