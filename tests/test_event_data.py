from eventstore_grpc import event_data

import pytest

class TestJSONEventData:
    def test_deserialize(self) -> None:
        assert event_data.JSONEventData.deserialize_data('{"foo": "bar"}') == {
            "foo": "bar"
        }

    def test_validate_event_id(self) -> None:
        with pytest.raises(ValueError):
            event_data.JSONEventData(
                event_id="invalid-uuid", type="something-happened", data=None
            )
