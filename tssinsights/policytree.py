from itertools import combinations

class PolicyNode:
    pass


class PolicyTree(PolicyNode):
    def __init__(self, threshold: int, nodes: list[PolicyNode]):
        self.threshold = threshold
        self.nodes = nodes
        self.miniscript = ""
        
    def __repr__(self):
        nodes_repr = ", ".join(repr(node) for node in self.nodes)
        return f"thresh({self.threshold}, {nodes_repr})"

    def to_ascii(self, level=0) -> str:
        indent = "  " * level
        representation = f"{indent}thresh({self.threshold})\n"
        for node in self.nodes:
            if isinstance(node, PolicyTree):
                representation += node.to_ascii(level + 1)
            else:
                representation += "  " * (level + 1) + repr(node) + "\n"
        return representation

    def __eq__(self, other):
        if not isinstance(other, PolicyTree):
            return False
        return self.threshold == other.threshold and self.nodes == other.nodes

    def __hash__(self):
        return hash((self.threshold, tuple(self.nodes)))

class PolicyRole(PolicyNode):
    def __init__(self, key: str):
        self.key = key
    
    def __repr__(self):
        return f"pk({self.key})"

    def __eq__(self, other):
        return isinstance(other, PolicyRole) and self.key == other.key
    
    def __hash__(self):
        return hash(self.key)


def generate_policy_trees(depth: int, max_children: int, roles: list[str], compile_callback, store_callback) -> set[PolicyTree]:
    """
    Generate all unique PolicyTree structures up to a given depth and max branching factor.
    Each PolicyTree node can have varying thresholds, from 1 up to the number of its children.
    """
    if depth == 0:
        return {PolicyRole(role) for role in roles}

    unique_trees = set()

    # Generate all possible child trees at the next depth level
    sub_trees = generate_policy_trees(depth - 1, max_children, roles, compile_callback, store_callback)

    # For each possible number of children (1 to max_children)
    for num_children in range(1, max_children + 1):
        # Generate all unique combinations of child subtrees of size `num_children`
        for child_combo in combinations(sub_trees, num_children):
            # For each possible threshold (from 1 up to num_children)
            for threshold in range(1, num_children + 1):
                tree = PolicyTree(threshold, list(child_combo))
                compile_callback.feed(tree)
                store_callback.store(tree)
                unique_trees.add(tree)
                print(tree)

    return unique_trees