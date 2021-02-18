import abc


class AbstractConsumerModel(abc.ABC):
    @abc.abstractmethod
    def callback(self, ch, method, properties, body):
        pass
