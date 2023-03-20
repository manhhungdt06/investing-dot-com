IGNORES = (
    'google',
)


def should_abort_request(req):
    for item in IGNORES:
        if item in req.url:
            # print(req.url)
            return True

    if req.resource_type == "image":
        return True

    if req.resource_type == "media":
        return True

    # if req.resource_type == "script":
    #     return True

    # if req.resource_type == "xhr":    # need
    #     return True

    # if req.resource_type == "stylesheet": # slow
    #     return True

    if req.resource_type == "other":
        return True

    # if req.method.lower() == 'post':
    #     # logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
    #     return True

    return False
