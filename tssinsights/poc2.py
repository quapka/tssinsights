from compilecallback import BinaryFeeder
from sqlitecallback import SqliteCallback
from bucketing import Bucketing
from policytree import *
import time, string

if __name__ == "__main__":
    #Exampple struct
    #ra = PolicyRole("A")
    #rb = PolicyRole("B")
    #rc = PolicyRole("C")
    #th = PolicyTree(1, [ra, rb])
    #thresh = PolicyTree(2, [ra, rc, th])
    #print(thresh)

    BINARY_PATH = "./miniscript"
    ROLES = 3
    DEPTH = 3
    WIDTH = 2

    #Get distinct roles ["a", "b", "c"]
    roles_list = list(string.ascii_lowercase[:ROLES])

    #Start the miniscript subprocess
    miniscript_feeder = BinaryFeeder(BINARY_PATH)
    miniscript_feeder.start()
    
    #Start db
    sqlite_callback = SqliteCallback(f"policytrees({ROLES},{DEPTH},{WIDTH}).db")
    
    start = time.time()
    generate_policy_trees(depth=DEPTH, max_children=WIDTH, roles=roles_list, compile_callback=miniscript_feeder, store_callback=sqlite_callback)
    end = time.time()

    miniscript_feeder.stop()
    print("Database populated")
    gen_timer = end-start
    
    start = time.time()
    bucketing_worker = Bucketing()
    bucketing_worker.analyze(sqlite_callback)
    end = time.time()

    sqlite_callback.close()
    
    print(f"Time elapsed generating: {gen_timer}")
    print(f"Time elapsed analyzing: {end-start}")
