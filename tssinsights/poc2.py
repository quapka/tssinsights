from binaryfeeder import BinaryFeeder
from policytree import *

if __name__ == "__main__":
    #Exampple struct
    ra = PolicyRole("A")
    rb = PolicyRole("B")
    rc = PolicyRole("C")
    th = PolicyTree(1, [ra, rb])
    thresh = PolicyTree(2, [ra, rc, th])
    print(thresh)

    BINARY_PATH = "./miniscript"

    #Generator
    roles = ["a", "b", "c"]
    all_unique_trees = generate_policy_trees(depth=2, max_children=2, roles=roles)

    feeder = BinaryFeeder(BINARY_PATH)
    feeder.start()

    for tree in all_unique_trees:
        feeder.feed(tree)
        print(tree.miniscript)

    feeder.stop()
