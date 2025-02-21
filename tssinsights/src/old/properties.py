from policyproperty import PolicyProperty, Policy

class MultipleProp(PolicyProperty):
 
    def check_property(candidate: Policy, base: Policy) -> bool:
        candidate_tuple = candidate[0]
        base_tuple = base[0]
        return (candidate_tuple[0] % base_tuple[0] == 0 and candidate_tuple[1] % base_tuple[1] == 0)

    def description():
        return "is a multiple of the base"


class SameRolesProp(PolicyProperty):
 
    def check_property(candidate: Policy, base: Policy) -> bool:
        candidate_tuple = candidate[0]
        base_tuple = base[0]
        return (candidate_tuple[2] == base_tuple[2])

    def description():
        return "has the same amount of roles"


class SameTNProp(PolicyProperty):
    def check_property(candidate: Policy, base: Policy) -> bool:
        candidate_tuple = candidate[0]
        base_tuple = base[0]
        return (candidate_tuple[0] == candidate_tuple[1] if base_tuple[0] == base_tuple[1] else False)

    def description():
        return "has the same amount of signers and group size"


class SameTEProp(PolicyProperty):

    def check_property(candidate: Policy, base: Policy) -> bool:
        candidate_tuple = candidate[0]
        base_tuple = base[0]
        return ((candidate_tuple[0] == candidate_tuple[2]) if base_tuple[0] == base_tuple[2] else False)

    def description():
        return "has the same number of roles and signers"


class LargerNProp(PolicyProperty):
 
    def check_property(candidate: Policy, base: Policy) -> bool:
        candidate_tuple = candidate[0]
        base_tuple = base[0]
        return ((candidate_tuple[0] < candidate_tuple[1]) if base_tuple[0] < base_tuple[1] else False)

    def description():
        return "has n that is larger than t"


class SmallTProp(PolicyProperty):
 
    def check_property(candidate: Policy, base: Policy) -> bool:
        candidate_tuple = candidate[0]
        base_tuple = base[0]
        return (candidate_tuple[0] == 1 if base_tuple[0] == 1 else False) 

    def description():
        return "has small t"

