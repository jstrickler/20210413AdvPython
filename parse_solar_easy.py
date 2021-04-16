import lxml.etree as et

tree = et.parse('DATA/solar.xml')

for planet in tree.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print("    {}".format(moon.text))

# tree.findall() is really tree.getroot().findall()

# element.find() finds the first child that matches
