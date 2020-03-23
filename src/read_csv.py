import ast
from collections import namedtuple
import csv


def iter_csv(path, delimiter=',', **reader_kwds):
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, **reader_kwds)
        for row in spamreader:
            yield row


def read_pop_exp_csv(path,
                     col_types=[int,int,int,int,str,int,float,int,float],
                     as_dict=True):
    """Read in a csv with population experiment."""
    it_csv = iter_csv(path)
    cols = next(it_csv)
    data = list(it_csv)
    data = [[f(d[i]) for d in data] for i,f in enumerate(col_types)]
    if as_dict:
        res = dict(zip(cols, data))
    else:
        PopExp = namedtuple('PopExp', ' '.join(cols))
        res = PopExp(*data)
    return res


def read_households_csv(path):
    """Reads households_experiments files.
    
    Assumption: second column is that with the lists.
    """
    it_csv = iter_csv(path)
    cols = next(it_csv)
    d = list(it_csv)
    inhabitants = [ast.literal_eval(i) for hi, i in d]
    household   = [int(hi) for hi,_ in d]
    capacities  = [len(i) for i in inhabitants]
    return household, inhabitants, capacities
