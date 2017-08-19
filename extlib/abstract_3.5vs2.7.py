from abc import ABCMeta, abstractmethod


#
# abc 2.7 and 3.5 are NOT complatible
#
# For 2.7 the definition should look like
# class AbstractSuperClassNew(metaclass=ABCMeta):
#    __metaclass__ = ABCMeta
#
# for 3.5
#
class AbstractSuperClassNew(metaclass=ABCMeta):

    def do_stuff(self):
        print('I am doing stuff')

    def delgate(self):
        self.do_real_work()

    @abstractmethod
    def do_real_work(self):
        pass


try:
    absn = AbstractSuperClassNew()
except Exception as ex:
    print('{} Fails as soon as the super class is instantiated: {}'.format(type(ex).__name__, ex))


class SubAbstractSuperClassNew(AbstractSuperClassNew):
    pass

try:
    sabsn = SubAbstractSuperClassNew()
except TypeError as ex:
    print('Fails as soon as the sub class is instantiated: {}'.format(ex))
