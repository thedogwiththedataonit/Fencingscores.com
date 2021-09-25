from typing import List



list = ["Junior Men's Epee January 4, 2019", "Cadet Men's Foil November 13, 2015", "Div I Men's Epee December 05, 2015", "Junior Men's Epee January 11, 2016", "Junior Men's Foil February 13, 2016", "Cadet Men's Foil February 15, 2016", "Div I Men's Foil April 09, 2016", "Div I Men's Foil June 29, 2016", "Junior Men's Foil July 01, 2016", "Div I Men's Foil October 08, 2016", "Div I Men's Epee October 09, 2016", "Junior Men's Foil November 11, 2016", "Junior Men's Epee November 13, 2016", "Junior Men's Foil January 6, 2017", "Div I Men's Foil January 8, 2017", "Junior Men's Epee January 9, 2017", "Junior Men's Epee February 17, 2017", "Junior Men's Foil February 18, 2017", "Div I Men's Epee April 23, 2017", "Div I Men's Foil April 24, 2017", "Junior Men's Epee July 01, 2017", "Div I Men's Foil July 02, 2017", "Div I Men's Epee July 03, 2017", "Junior Men's Foil July 04, 2017", "Div I Men's Foil October 16, 2017", "Junior Men's Foil November 13, 2017", "Div I Men's Foil December 11, 2017", "Div I Men's Foil January 7, 2018", "Junior Men's Foil February 16, 2018", "Junior Men's Foil June 29, 2018", "Div I Men's Foil July 1, 2018", "Div I Men's Epee January 6, 2019", "Div I Men's Epee January 6, 2019"]

sorted = sorted(list, key=lambda x: int(x.split(", 20")[-1]))


print(sorted)

        

