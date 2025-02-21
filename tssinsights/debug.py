from tssinsights.src.compilecallback import BinaryFeeder
from tssinsights.src.sqlitecallback import SqliteCallback
from tssinsights.src.bucketing import Bucketing
from tssinsights.src.policytree import *
import time, string, sys

if __name__ == "__main__":
    BINARY_PATH = "./miniscript/miniscript"
    ROLES = 2
    DEPTH = 2
    WIDTH = 2
    
    #Get distinct roles ["a", "b", "c"]
    roles_list = tuple(string.ascii_lowercase[:ROLES])

    #Start the miniscript subprocess
    miniscript_feeder = BinaryFeeder(BINARY_PATH)
    miniscript_feeder.start()
    
    #Start db
    sqlite_callback = SqliteCallback(f"exports/policytrees({ROLES},{DEPTH},{WIDTH}).db")
    
    generate_policy_trees(depth=DEPTH, max_children=WIDTH, roles=roles_list, compile_callback=miniscript_feeder, store_callback=sqlite_callback)
