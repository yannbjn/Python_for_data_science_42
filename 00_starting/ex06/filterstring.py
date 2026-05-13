def ft_filter(function_to_apply, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    
    if function_to_apply is None:
        # Uses list comprehension, but returns an iterator to mimic original filter
        return iter([x for x in iterable if x])
    
    return iter([x for x in iterable if function_to_apply(x)])