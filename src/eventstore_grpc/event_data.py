"""
An Event.
"""
import abc
import uuid
from typing import Any, Dict
import json


class EventData(abc.ABC):
    """Events abstract class.

    When appending events to EventStoreDB they must first all be wrapped in an Event
    object. This allow you to specify the content of the event, the type of event
    and whether its in JSON format. In it's simplest form you need to three following
    arguments.

    * `event_id`: this takes the format of `Uuid` and is used to uniquely identify the
        event your are trying to append. If two events with the same `Uuid` are appended
        to the same stream in quick succession, EventStoreDB will only append one copy
        of the event to the stream.
    * `type`: an event type should be supplied for each event. This is a unique string
        used to identify the type of event you are saving.

        It is common to see the explicit event code type name used as the type as
        it makes serializing and de-serializing of the event easy. However we recommend
        against this as it couples the storage to the type and will make it more
        difficult if you need to version the event at a later date.
    * `data`: representation of your event data. It is recommended that you store your
        events as JSON objects as this will allow you to make use of all of
        EventStoreDB's functionality such as projections. Ultimately though, you can
        save it using whatever format you like as eventually, it will be stored as
        encoded bytes.
    * `metadata`: it is common to need to store additional information along side your
        event that is part of the event itself. This can be correlation Id's,
        timestamps, access information, etc. EventStoreDB allows you to store a
        separate byte array containing this information to keep it separate.
    * `is_json`: a simple boolean field to tell EventStoreDB if the event is stored as
        a json, `True` by default.
    """

    def __init__(
        self,
        event_id: uuid.UUID,
        type: str,
        data: Any,
        metadata: Any,
        is_json: bool = True,
    ):
        self.event_id = event_id
        self.type = type
        self.data = data
        self.metadata = metadata
        self.is_json = is_json

    def __repr__(self):
        return f"{self.__class__.__name__}(**{self.__dict__!r})"  # pragma: nocover

    def __str__(self):
        return f"{self.type} => {self.data}"  # pragma: nocover

    @property
    def data_content_type(self):
        return "application/json" if self.is_json else "application/octet-stream"

    @property
    def serialized_metadata(self):
        return json.dumps(self.metadata).encode()

    @property
    @abc.abstractmethod
    def serialized_data(self):
        raise NotImplementedError  # pragma: nocover

    @classmethod
    @abc.abstractmethod
    def deserialize_data(cls, data: str):
        raise NotImplementedError  # pragma: nocover


class JSONEventData(EventData):
    """An Event carrying data as a JSON payload."""

    def __init__(
        self,
        type: str,
        data: Dict,  # TODO: should be JSON-able.
        metadata: Any = None,
        event_id: uuid.UUID = None,
    ):
        if event_id is None:
            event_id = uuid.uuid4()

        if metadata is None:
            metadata = {}
        super().__init__(event_id, type, data, metadata, True)

    @property
    def serialized_data(self):
        return json.dumps(self.data).encode()

    @classmethod
    def deserialize_data(cls, data: str):
        return json.loads(data)
