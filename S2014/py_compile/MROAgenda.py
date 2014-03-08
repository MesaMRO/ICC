from ./libs/LaTeXCompile import LaTeXDocument as texdoc


doc = texdoc()
# Packages
doc.package_list = [
        ("tabularx"),
        ("babel","english")
]
# Title styles
doc.title_line_styles = [
        r"{\LARGE\scshape %s}\\[0.2cm]",
        r"{\Large\scshape %s}\\[0.2cm]",
        r"{\large %s}\\[0.2cm]"
]
# Title lines
doc.title_lines = [
        (0,"Mesa Robotics Organization"),
        (1,"Meeting Agenda"),
        (1,"Month Day, 2014"),
        (2,"(Test document)")
]

# Compile TeX document lines
lines = []
# Preamble
for i in doc.makePreamble():
    lines.append(i)
# Title
for i in doc.makeTitle():
    lines.append(i)
# Vertical space
lines.append(doc.makeVerticalSpace("0.4cm"))
# Make end
lines.append(doc.makeEnd())

# Write lines to file
test_file = open("test_file.tex",'w')
for i in lines:
    #print(i, file=test_file)
    print(i)
test_file.close()
