class India():
    def capital(self):
        print("India's capital is New Dehli")
    def language(self):
        print("India's most spoken language is Hindi.")
    def type(self):
        print("India is a developing country.")

class US():
    def capital(self):
        print("USA's capital is Washington DC")
    def language(self):
        print("USA's most spoken language is English.")
    def type(self):
        print("The USA is a developed country.")

objIndia = India()
objUS = US()
for country in (objIndia, objUS):
    country.capital()
    country.language()
    country.type()