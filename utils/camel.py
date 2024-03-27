'''Parser snake_case to camelCase'''


def to_camel(snake_str: str | None = None):
    """Parser snake_case to camelCase"""
    if snake_str is None:
        return None
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
