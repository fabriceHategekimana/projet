import math  # log function


class ProbabilityFunction:
    """
    Simple (discrete) probability function

    ...

    Attributes
    ----------
    function : dict {int/float: int/float}
        Value of x associated with probability p(x)

    Constructor
    -----------
    ProbabilityFunction(*args)
        1 argument  :   arg[0]: dict assigned to .function

        2 arguments :   arg[0]: list(int/float), values of x
                        arg[1]: list(int/float), values of p(x). sum(arg[1]) should equal 1

    ProbabilityFunction.uniform(set_x)
        Uniformly distributed probability function, non zero for every value of set_x

    ProbabilityFunction.binary(cls, p)
        Binary probability function, probability of success P(1) = p

    """

    def __init__(self, *args):
        """
        Initialize .function with the given arguments

        :param args: 1 argument, arg[0]: dict   {int/float: int/float}
                                                {x: p(x)}
                     2 arguments, arg[0]: int/float  x
                                  arg[1]: int/float  p(x)

        :raises ValueError if sum(p(x)) != 1 (with 1e-5 precision)
        """

        if len(args) == 0:
            raise TypeError(self.__name__ + '() takes at least 1 argument (0 given)')

        elif len(args) == 1:
            if type(args[0]) != dict:
                raise TypeError('Expected dict, got ' + type(args[0]).__name__)
            if any(type(x) != int and type(x) != float for x in list(args[0].keys())) \
                    or any(type(x) != int and type(x) != float for x in list(args[0].values())):
                raise TypeError('Expected int or float')
            if abs(sum(args[0].values()) - 1) > 1e-5:
                raise ValueError('sum of probabilities should equal 1, received ' + str(sum(args[0].values())))

            self.function = args[0]

        elif len(args) == 2:
            if len(args[0]) != len(args[1]):
                raise ValueError('incompatible size, received ' + str(len(args[0])) + ' and ' + str(len(args[1])))
            if any(type(x) != int and type(x) != float for x in list(args[0]) + list(args[1])):
                raise TypeError('Expected int or float')
            if abs(sum(args[1]) - 1) > 1e-5:
                raise ValueError('sum of probabilities should equal 1, received ' + str(sum(args[1])))

            self.function = dict(zip(args[0], args[1]))
        else:
            raise TypeError(self.__name__ + '() takes at most 2 arguments (' + str(len(args)) + ' given)')

    @classmethod
    def uniform(cls, set_x):
        if any(type(x) != int and type(x) != float for x in set_x):
            raise TypeError('Expected int or float')

        set_ = set(set_x)
        return cls(dict(zip(set_, [1 / len(set_)] * len(set_))))

    @classmethod
    def binary(cls, p: int or float):
        if type(p) != int and type(p) != float:
            raise TypeError('Expected int or float')
        if not (0 <= p <= 1):
            raise ValueError('probability of success p, should be bound between 0 and 1 received ' + str(p))

        set_x = {0, 1}
        return cls(dict(zip(set_x, [1 - p, p])))


def dkl(p: dict, q: dict, log_base: int or float = None) -> float or str:
    """
    Kullback-Leibler Divergence: D(p||q)

    ! No input coherence verification

    :param p: dict, probability function p(x)
    :param q: dict, probability function p(x)
    :param log_base: Base of the logarithm, default is natural log
    :return: float or "inf" if there is a value of x such that q(x) = 0 and p(x) != 0
    """
    set_x = set.union(set(p.keys()), set(q.keys()))
    if any(q.get(x, 0) == 0 != p.get(x, 0) for x in set_x):
        return "inf"

    if log_base is None:
        return sum([0 if p.get(x, 0) == 0 else
                    p.get(x, 0) * math.log(p.get(x, 0) / q.get(x, 0)) for x in set_x])
    else:
        return sum([0 if p.get(x, 0) == 0 else
                    p.get(x, 0) * math.log(p.get(x, 0) / q.get(x, 0), log_base) for x in set_x])


if __name__ == '__main__':
    # _p = dict(zip(range(1, 9), [0.125] * 8))
    # _q = dict(zip(range(1, 9), [0.03, 0.07, 0.1, 0.2, 0.25, 0.2, 0.1, 0.05]))

    _p = ProbabilityFunction.uniform(range(1, 9))

    _q = ProbabilityFunction(range(1, 9), [0.03, 0.07, 0.1, 0.2, 0.25, 0.2, 0.1, 0.05])
    print('a) q(x)= [' + ', '.join(str(e) for e in _q.function.values()) + ']\n' +
          '   Dkl(p||q)= ' + str(dkl(_p.function, _q.function, 2)) + '\n' +
          '   Dkl(q||p)= ' + str(dkl(_q.function, _p.function, 2)) + '\n')

    _q = ProbabilityFunction(range(1, 9), [0.1, 0, 0, 0.4, 0, 0, 0.3, 0.2])
    print('b) q(x)= [' + ', '.join(str(e) for e in _q.function.values()) + ']\n' +
          '   Dkl(p||q)= ' + str(dkl(_p.function, _q.function, 2)) + '\n' +
          '   Dkl(q||p)= ' + str(dkl(_q.function, _p.function, 2)))

    # a) q(x)= [0.03, 0.07, 0.1, 0.2, 0.25, 0.2, 0.1, 0.05]
    # Dkl(p||q) = 0.3131294289009376
    # Dkl(q||p) = 0.2704248389114091
    #
    # b) q(x) = [0.1, 0, 0, 0.4, 0, 0, 0.3, 0.2]
    # Dkl(p||q) = inf
    # Dkl(q||p) = 1.1535606553289848
