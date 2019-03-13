#1
#SELECT countries.name, language, percentage FROM languages JOIN countries ON countries.id = languages.country_id WHERE language = 'Slovene' ORDER BY languages.percentage DESC;
#3
#SELECT cities.name, cities.population FROM cities JOIN countries ON countries.id = cities.country_id WHERE countries.name = 'Mexico' AND cities.population > 500000 ORDER BY cities.population DESC;
#4
#SELECT countries.name, languages.language, languages.percentage FROM languages JOIN countries ON countries.id = languages.country_id WHERE languages.percentage > 89 ORDER BY languages.percentage DESC;
#6
#SELECT name, government_form, capital, life_expectancy FROM countries WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;
#5
#SELECT name, surface_area, population FROM countries WHERE surface_area < 501 AND population > 100000;
#7
#SELECT countries.name, cities.name, cities.district, cities.population FROM cities JOIN countries on countries.id = cities.country_id WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;
#8
#SELECT region, COUNT(countries.id) FROM countries GROUP BY countries.region ORDER BY COUNT(countries.id) DESC;
#2
#SELECT countries.name, COUNT(cities.id) FROM countries JOIN cities ON cities.country_id = countries.id GROUP BY countries.name ORDER BY COUNT(cities.id) DESC;