#Usiel Figueroa
#Module 7.2Assignment: Test Cases
# CSD325 - A311 Advanced Python
# November 26, 2024

# References
# (n.d.). Unittest — Unit testing framework. Python. Retrieved November 18, 2024, from https://docs.python.org/3/library/unittest.html
# Matthes, E. (2019). Python crash course : a hands-on, project-based introduction to programming (2nd edition.). No Starch Press.


# city_functions.py

def city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result




# Call the function with different arguments and print results
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan", 13929286))
print(city_country("Paris", "France", 2161000, "French"))
print(city_country("New York", "USA"))
print(city_country("Beijing", "China", 21540000))
print(city_country("Moscow", "Russia", 12615000, "Russian"))

