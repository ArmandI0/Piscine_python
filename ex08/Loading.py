def ft_tqdm(lst: range) -> None:
	for val in lst:
		percent = round(val / len(lst) * 100)
		print(percent, percent * '█', (100 - percent) * " ", " | " , val + 1 , "/", len(lst), end='\r')
		yield