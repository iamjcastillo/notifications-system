from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event):
        pass

    @abstractmethod
    def subscribe(self, event_type, handler):
        pass


class EventPublisherImpl(EventPublisher):
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event):
        event_type = type(event)
        if event_type in self._subscribers:
            for handler in self._subscribers[event_type]:
                handler(event)
