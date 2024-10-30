from compilecallback import BinaryFeeder
from sqlitecallback import SqliteCallback
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
    
    #all_unique_trees = generate_policy_trees(depth=5, max_children=5, roles=roles, compile_callback=feeder, store_callback=sqlite)
#    for tree in all_unique_trees:
#        feeder.feed(tree)
#        print(tree.miniscript)


    BINARY_PATH = "./miniscript"
    DEPTH = 3
    WIDTH = 3
    ROLES = 3
    
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
    sqlite_callback.close()
    print(f"Time elapsed: {end-start}")
