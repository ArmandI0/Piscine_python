def ft_filter(function, tab):
	try:
		assert callable(function), "Function not callable"
		for menb in tab:
			if function(menb):
				yield menb
	except AssertionError as error:
		print(error)