import webbrowser

def quickadress(adress):
	open_adress = "https://www.google.com/maps/place/" + adress
	return webbrowser.open(open_adress)

quickadress("13 avenue vaucanson")
