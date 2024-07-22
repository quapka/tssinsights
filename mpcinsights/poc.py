class MPCanalyzer():

    def __init__(self, limit: int = 10):
        self.limit = limit
        self.policies = self.bruteforce_policies(self.limit)
    
    def __str__(self):
        return f"{self.policies}"

    def bruteforce_policies(self, limit: int) -> list[tuple[int, int, int]]:
        out = []

        for n in range(1, limit):
            for k in range(1, limit):
                for e in range(1, limit):
                    if k > n or e > n:
                        continue
                    out.append((n, k, e))
        return out

    def find_commonalities(self, policy: tuple[int, int, int]) -> None:
        common_policies = [policy_candidate for policy_candidate in self.policies if self.has_same_properties(policy_candidate, policy)]
        print(f"Policy {policy} has common properties with {len(common_policies)} policies in limit {self.limit}: {common_policies}")

    def has_same_properties(self, candidate: tuple[int, int, int], policy: tuple[int, int, int]) -> bool:
        return (candidate[0] % policy[0] == 0 and candidate[1] % policy[1] == 0 and candidate[1] % policy[1] == 0)


if __name__=="__main__":

    policy = (3,2,2)
    mpcanalyzer = MPCanalyzer(10)
    print(mpcanalyzer)
    mpcanalyzer.find_commonalities(policy)