The folder `policies` contains various examples of policies,
where I tried to see how the _likeliness_, i.e. using `<NUM>@` in the
`or` policies, e.g., `or(9@pk(A), pk(B))` affects the final Script,
when compiled through Miniscript.

The filenames are trying to be descriptive, but aren't always. `cat` the
files inside `policies` directory and pipe them to `miniscript` to see the
differences.

To make human-reading of the policies easier, you can use `#` on a separate line
for example:
```
or(
    1@or(
        1@or(pk(A1), 16@pk(A2)),
        or(1@pk(B1), 1@pk(B2))
    ),
    1@or(
        or(pk(C1), 1@pk(C2)),
        1@or(1@pk(D1), pk(D2))
    )
)
#
or(
    4@or(
        4@or(pk(A4), 4@pk(A2)),
        or(4@pk(B4), 16@pk(B2))
    ),
    4@or(
        or(pk(C4), 4@pk(C2)),
        4@or(8@pk(D4), pk(D2))
    )
)
```
and use the `prep.sh` script before piping to Miniscript:
```bash
$ ./prep.sh <path/to/policy> | <path/to/miniscript>
```
