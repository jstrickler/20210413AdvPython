import lxml.etree as et

tree = et.parse('DATA/solar.xml')
print(tree)

root = tree.getroot()
print(root, root.tag)
for section in root:
    print(section.tag)
    if section.tag.endswith('planets'):
        for planet in section.findall('planet'):
            print("    {}".format(planet.get('planetname')))
            for moon in planet:
                print("        {}".format(moon.text))



