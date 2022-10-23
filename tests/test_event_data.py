from eventstore_grpc import event_data


class TestJSONEventData:
    def test_deserialize(self) -> None:
        assert event_data.JSONEventData.deserialize_data('{"foo": "bar"}') == {
            "foo": "bar"
        }
