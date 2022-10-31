"""
Shared constant values.
"""

"""
## Handling Concurrency.
When appending events to a stream, you can supply a
*stream state* or *stream revision*. Your client can
use this to tell EventStoreDB what state or version
you expect the stream to be in when you append. If the
stream isn't in that state the an exception will be thrown.

The are three available stream states:

* Any
* NoStream
* StreamExists

This check can be used to implement optimistic concurrency. When you retrieve a stream
from EventStoreDB, you take note of the current version number, then when you save it
back you can determine if somebody else has modified the record in the meantime.
"""

NO_STREAM = "NO_STREAM"
ANY = "ANY"
STREAM_EXISTS = "STREAM_EXISTS"

"""
## Directions
"""
FORWARDS = "FORWARDS"
BACKWARDS = "BACKWARDS"

"""
## Revision positions.
"""
START = "START"
END = "END"

"""
## OTHERS
"""
WRONG_EXPECTED_VERSION = "wrong_expected_version"
ROUND_ROBIN = "ROUND_ROBIN"
DISPATCH_TO_SINGLE = "DISPATCH_TO_SINGLE"
PINNED = "PINNED"
