def ft_filter(function, tab):
    """
    Filters elements in an iterable using a specified function.

    Args:
        function (callable): A function that returns True for elements to keep.
        tab (iterable): The iterable to filter.

    Yields:
        Elements from `tab` for which `function` returns True.

    Raises:
        AssertionError: If `function` is not callable.
    """
    try:
        assert callable(function), "Function not callable"
        for menb in tab:
            if function(menb):
                yield menb
    except AssertionError as error:
        print(error)
