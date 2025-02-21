from tssinsights.src.compilecallback import BinaryFeeder
from tssinsights.src.sqlitecallback import SqliteCallback
from tssinsights.src.bucketing import Bucketing
from tssinsights.src.policytree import *
import time, string, sys

if __name__ == "__main__":
    #Exampple struct
    #ra = PolicyRole("A")
    #rb = PolicyRole("B")
    #rc = PolicyRole("C")
    #th = PolicyTree(1, [ra, rb])
    #thresh = PolicyTree(2, [ra, rc, th])
    #print(thresh)

    BINARY_PATH = "./miniscript/miniscript"
    #ROLES = 2
    #DEPTH = 2
    #WIDTH = 2
    
    ROLES = int(sys.argv[1])
    DEPTH = int(sys.argv[2])
    WIDTH = int(sys.argv[3])


    #Get distinct roles ["a", "b", "c"]
    roles_list = tuple(string.ascii_lowercase[:ROLES])

    #Start the miniscript subprocess
    miniscript_feeder = BinaryFeeder(BINARY_PATH)
    miniscript_feeder.start()
    
    #Start db
    sqlite_callback = SqliteCallback(f"exports/policytrees({ROLES},{DEPTH},{WIDTH}).db")
    
    start = time.time()
    generate_policy_trees(depth=DEPTH, max_children=WIDTH, roles=roles_list, compile_callback=miniscript_feeder, store_callback=sqlite_callback)
    end = time.time()

    miniscript_feeder.stop()
    print("Database populated")
    gen_timer = end-start
    
    start = time.time()
    bucketing_worker = Bucketing()
    buckets = bucketing_worker.analyze(sqlite_callback)
    bucketing_worker.export_to_csv(buckets, f"exports/report({ROLES},{DEPTH},{WIDTH}).csv")
    end = time.time()

    sqlite_callback.close()
    
    print(f"Time elapsed generating: {gen_timer}")
    print(f"Time elapsed analyzing: {end-start}")
