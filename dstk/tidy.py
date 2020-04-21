
from hashlib import md5
from collections import namedtuple
from dstk.util import md5sum, duplicates, which

def makeId(row,indices):
    idxRow = [str(v) for v in row[list(indices)]]
    return md5sum("".join(idxRow))

def duplicatedUoaIndices(data,indices):
    if not all([i in data.columns for i in indices]):
        missing = [i for i in indices if not i in data.columns]
        raise ValueError(f"The data is missing these indices: {missing}")

    identifiers = [makeId(row,indices) for idx,row in data.iterrows()]

    nids = len(set(identifiers))
    nrows = data.shape[0]

    if nids != nrows: 
        dups = duplicates(identifiers)
        return which([id in dups for id in identifiers])
    else:
        return []

        
