# CountryBorders
There are two functionalities of the program:

1. List of all countries that border a country, and all the countries which border those countries.
Input a country, and the list of countries that borders it is returned

2. Input two countries into the terminal. The program will tell you if they border, or are seperated by one country. 

This site or product includes Country Borders data available from https://www.geodatasource.com.

# How to use main program
County database(s) are in the border_database folder. Input is in the test_cases folder. 
If you want to test your own countries, for now you have to either edit input.txt, or create a new text file with the countries you want, and then edit INPUT_FILES in Test_cases to be the file you want.
Results will appear in terminal if using terminalOutputMain, and will appear in output.txt if using main. 

# How to structure input file for main or terminalOutputMain
In the input file, enter the level of ordinance, and the list of countries you want to check. 
Level of ordinance is the degrees of seperation you want between your country and the furthest input

Level of Ordinance == 1 -> Countries which border country A

Level of Ordinance == 2 -> Countries which border ordinance 1 countries

Level of Ordinance == 3 -> Countries which border ordinance 2 countries

# How to run with specific input file
In line 31 of main.py, enter the location of the input file
Run the code through the following line:
py -u "{location}\CountryBorders\main.py"

# Example
If input file is:

2

Australia

Bangladesh

Pakistan

Victoria

The result will be: 

Australia borders no countries

Australia doesn't have any secondary borders


Bangladesh borders these countries: India, Myanmar

Bangladesh's secondary border nations are: Bhutan, China, Nepal, Pakistan, Lao People's Democratic Republic, Thailand


Pakistan borders these countries: Afghanistan, China, India, Iran (Islamic Republic of)

Pakistan's secondary border nations are: Tajikistan, Turkmenistan, Uzbekistan, Bhutan, Hong Kong, Kazakhstan, Korea (Democratic People's Republic of), Kyrgyzstan, Lao People's Democratic Republic, Macao, Mongolia, Myanmar, Nepal, Russian Federation, Viet Nam, Bangladesh, Armenia, Azerbaijan, Iraq, Turkey


Victoria not present in database

# How to use 'do they border'
Run doTheyBorder.py, and enter two countries, seperated by a comma. Results will appear in the terminal, and they will tell you if the countries border, are seperated by 1 country, or are not either