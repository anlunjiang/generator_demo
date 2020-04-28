import resource


def memory_usage_resource():
    denom = 1024.
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / denom
    return mem