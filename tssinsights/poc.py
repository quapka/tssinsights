from properties import *
from policyproperty import Policy


class MPCanalyzer():

    def __init__(self, limit: int = 6):
        self.limit = limit
        self.policies = self.bruteforce_policies(self.limit)
        self.properties = [SameRolesProp, MultipleProp, SameTEProp, LargerNProp, SmallTProp, SameTNProp]
    
    def __str__(self):
        return f"{self.policies}"

    def bruteforce_policies(self, limit: int) -> Policy:
        out = []

        for n in range(1, limit):
            for t in range(1, limit):
                for e in range(1, limit):
                    if t > n or e > n:
                        continue
                    out.append([(t, n, e), []])
        return out

    def analyze(self, policy: Policy) -> None:
        policy = [policy, []]
        common_policies = [policy_candidate for policy_candidate in self.policies if self.has_common_properties(policy_candidate, policy)]
        print(f"Policy {policy[0]} has common properties with {len(common_policies)} ({(len(common_policies)/len(self.policies)* 100):.2f}%) policies in limit {self.limit}:")

        for policy in common_policies:
            print(f"Policy {policy[0]}: ")
            for prop in policy[1]:
                print(prop.description())

    def has_common_properties(self, candidate: Policy, base: Policy) -> bool:

        #placeholder pre higher-level rules
        final_sum = []

        for prop in self.properties:
            if prop.check_property(candidate, base):
                final_sum.append(True)
                candidate[1].append(prop)
            else:
                final_sum.append(False)
        
        return (final_sum[0] and final_sum[1]) or (final_sum[2] and final_sum[3]) or (final_sum[4]) or (final_sum[5] and final_sum[0])



if __name__=="__main__":
    # t out of n with e distinct roles
    policy = (2,3,2)
    mpcanalyzer = MPCanalyzer()
    #print(mpcanalyzer)
    mpcanalyzer.analyze(policy)