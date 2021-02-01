"""
Run users examples to check authentication.
"""

from pprint import pprint
from eventstore_grpc.options import base_options
from eventstore_grpc import EventStoreDBClient, JSONEventData


conn_str = "esdb://localhost:2111,localhost:2112,localhost:2113?tls&rootCertificate=./certs/ca/ca.crt"
default_user = {"username": "admin", "password": "changeit"}
credentials = base_options.as_credentials(**default_user)

client = EventStoreDBClient(conn_str)


# Create new admin user.
new_user = {
    "login_name": "john-doe",
    "password": "s3cr3t",
    "full_name": "John Doe",
    "groups": ["$admins", "event-store-guys"],
}
print("Creating new user:")
pprint(new_user)
client.create_user(**new_user, credentials=credentials)

# Check user details.
user_details = client.get_user_details(new_user["login_name"], credentials=credentials)
print("\nUSER DETAILS:")
for elm in user_details:
    print(f"FULL  NAME: {elm.user_details.full_name}")
    print(f"LOGIN NAME: {elm.user_details.login_name}")
    print(f"GROUPS    : {elm.user_details.groups}")

# Delete user.
print("\nDeleting user...")
result = client.delete_user(new_user["login_name"], credentials=credentials)
print(f"Poor {new_user['full_name'].split()[0]}'s gone 😢")
