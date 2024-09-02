"""Config for proxy/redirecter"""

# Base path to force a redirect to other API
BASE_PATH = '/redirect'

# Define if is necessary to use BASE_PATH to redirect.
# Warning: conflict risk with own endpoint if it is False.
REQUIRED_BASE_PATH_TO_REDIRECT = True

external_apis = []
