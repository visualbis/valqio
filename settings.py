import os
import schema.scenario as scenarioSchema

DOMAIN = {'scenarios': scenarioSchema.scenarios}

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))

# Skip this block if your db has no auth. But it really should.
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
# Name of the database on which the user can be authenticated,
# needed if --auth mode is enabled.
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE")

MONGO_DBNAME = os.getenv("MONGO_DBNAME")

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
IF_MATCH = False

X_DOMAINS = "*"
X_HEADERS = ["Content-Type"]
HATEOAS = False
PAGINATION = False
