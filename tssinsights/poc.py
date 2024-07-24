class MPCanalyzer():

    def __init__(self, limit: int = 6):
        self.limit = limit
        self.policies = self.bruteforce_policies(self.limit)
    
    def __str__(self):
        return f"{self.policies}"

    def bruteforce_policies(self, limit: int) -> list[tuple[int, int, int]]:
        out = []

        for n in range(1, limit):
            for t in range(1, limit):
                for e in range(1, limit):
                    if t > n or e > n:
                        continue
                    out.append((t, n, e))
        return out

    def analyze(self, policy: tuple[int, int, int]) -> None:
        common_policies = [policy_candidate for policy_candidate in self.policies if self.has_common_properties(policy_candidate, policy)]
        print(f"Policy {policy} has common properties with {len(common_policies)} ({(len(common_policies)/len(self.policies)* 100):.2f}%) policies in limit {self.limit}: {common_policies}")

    def has_common_properties(self, candidate: tuple[int, int, int], base: tuple[int, int, int]) -> bool:

        same_roles = (candidate[2] == base[2])
        multiples = (candidate[0] % base[0] == 0 and candidate[1] % base[1] == 0)
        same_t_e = ((candidate[0] == candidate[2]) if base[0] == base[2] else False)
        larger_n = ((candidate[0] < candidate[1]) if base[0] < base[1] else False)
        small_t = (candidate[0] == 1 if base[0] == 1 else candidate[0] != 1)
        return (same_roles and multiples) or (same_t_e and larger_n and small_t) 

if __name__=="__main__":
    # t out of n with e distinct roles
    policy = (2,3,2)
    mpcanalyzer = MPCanalyzer()
    print(mpcanalyzer)
    mpcanalyzer.analyze(policy)