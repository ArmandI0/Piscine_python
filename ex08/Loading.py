def ft_tqdm(lst: range) -> None:
    """
    Args:
        lst (range): The iterable to loop over, typically a range object.

    Yields:
        None: Updates the progress display in-place after each iteration.
    """
    for val in lst:
        prct = round(val / len(lst) * 100)
        loading = prct * '█'
        rest = (100 - prct) * " "
        print(f"{prct}%| {loading} {rest} | {val + 1} / {len(lst)}", end='\r')
        yield
