
def bruteforce_policies(limit: int):

    out = []

    for n in range(1, limit):
        for k in range(1, limit):
            for e in range(1, limit):
                    
                if k > n or e > n:
                    continue

                out.append((n, k, e))
    return out


if __name__=="__main__":

    limit = 10

    policies = bruteforce_policies(limit)
    print(policies)