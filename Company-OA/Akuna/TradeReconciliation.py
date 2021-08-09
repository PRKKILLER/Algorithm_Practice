"""  
To verify records, Akuna compares its own data with third party expchanges - 
this is called reconciliation.
For example: Akuna records show we bought 10 units of product A at 12:01:00, and that we sold 15 units
of product B at 12:05:00

AKUNA, A, 10, 12:01:00
AKUNA, B, -15, 12:05:00

if the expchange has the same records, that's a perfect reconciliation:
EXCHANGE, A, 10, 12:01:00
EXCHANGE, B, -15, 12:05:00

We trade across multiple exchanges and in much larger volume than this, so sometimes there are missing
records on one side called breaks. Breaks can occur on either side - e.g. Akuna has a trade not seen
in exchanges, or vice versa

You will be provided input as comma-separated lines of two types:


trade record: "SOURCE, PRODUCT, QUANTITY, TIMESTAMP"

reconciliation request: "RECONCILIATION, SOURCE, CONTERPARTY, reconciliation request"

The item's SOURCE is either Akuna or one of many exchanges, notated EXCHANGE#. THe PRODUCT, QUANTITY,
and TIMESTAMP represent trade information.

On lines representing a trade record {SOURCE, PRODUCT, QUANTITY, TIMESTAMP}, return the quantity
specified in the trade record.

On lines representing a reconciliation request, return the number of trades belonging to the
given SOURCE that aren't matched by the given CONTERPARTY

Example:
AKUNA,A,10,12:01:00
AKUNA,B,-15,12:05:00
RECONCILIATION,AKUNA,EXCHANGE1
RECONCILIATION,EXCHANGE1,AKUNA
EXCHANGE1,B,-15,12:05:00
EXCHANGE1,B,-20,12:07:00
RECONCILIATION,AKUNA,EXCHANGE1
RECONCILIATION,EXCHANGE1,AKUNA
RECONCILIATION,EXCHANGE2,AKUNA

Output:
10
-15
2
0
-15
-20
1
1
0
"""

from collections import defaultdict


class TradeReconciliation:
    def __init__(self):
        self.dic = defaultdict(set)
        self.recon = defaultdict(int)

    def process(self, line: str) -> str:
        ll = line.split(',')
        if ll[0] != 'RECONCILIATION':
            record = tuple(ll[1:])
            self.dic[ll[0]].add(record)
            return ll[2]
        else:
            source, dest = ll[1], ll[2]
            if source not in self.dic:
                return '0'
            if dest not in self.dic:
                return len(self.dic[source])

            mismatch = 0
            for record in list(self.dic[source]):
                if record not in self.dic[dest]:
                    mismatch += 1

            return str(mismatch)


if __name__ == '__main__':
    lines = [
        "AKUNA,A,10,12:01:00",
        "AKUNA,B,-15,12:05:00",
        "RECONCILIATION,AKUNA,EXCHANGE1",
        "RECONCILIATION,EXCHANGE1,AKUNA",
        "EXCHANGE1,B,-15,12:05:00",
        "EXCHANGE1,B,-20,12:07:00",
        "RECONCILIATION,AKUNA,EXCHANGE1",
        "RECONCILIATION,EXCHANGE1,AKUNA",
        "RECONCILIATION,EXCHANGE2,AKUNA"
    ]
    sol = TradeReconciliation()
    for line in lines:
        print(sol.process(line))
