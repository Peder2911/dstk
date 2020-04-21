from hashlib import md5
from contextlib import contextmanager
import sys

import pandas as pd

### Small functions
# Mostly just for readability

md5sum = lambda x: md5(x.encode()).hexdigest()
duplicates = lambda l: {x for x in set(l) if l.count(x) > 1}
which = lambda l: [i for i,e in enumerate(l) if e]

def applyToCsv(fn,infile=None,*args,**kwargs):
    """
    This function makes it possible to open a CSV data file, do stuff to it,
    and write the resulting data to stdout. 
    """
    if infile is None:
        infile = sys.stdin

    dat = pd.read_csv(infile)
    fn(dat,*args,**kwargs).to_csv(sys.stdout,index=False)


def obfuscate(dataset,seed):
    """
    This function makes it possible to use any kind of data 
    as example data, since it is effectively obfuscated while
    preserving the informational content.
    """
    seededSum = lambda x: md5sum(str(x)+seed)[:8]

    for name,values in dataset.iteritems():
        dataset[name] = values.apply(seededSum) 

    dataset.columns = [seededSum(nm) for nm in dataset.columns]

    return dataset
