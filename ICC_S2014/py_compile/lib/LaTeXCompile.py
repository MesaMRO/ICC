import os
import sys

# Pseudo-LaTeX document class
class LaTeXDocument:
    # document_class
    # package_list
    # title_line_styles
    # title_lines
    # title_position

    # Make document class
    document_class = "article"
    def makeDocumentClass(self):
        return r"\documentclass{%s}"%self.document_class

    # Make package list
    package_list = []
    def makePackageList(self):
        lines = []
        for i in self.package_list:
            if type(i) is tuple:
                lines.append(r"\usepackage%s{%s}"%(''.join(["[%s]"%i[j] for j in range(1,len(i))]),i[0]))
            else:
                lines.append(r"\usepackage{%s}"%i)
        return lines

    # Make document begin
    def makeDocumentBegin(self):
        return r"\begin{document}"

    # Make preamble
    def makePreamble(self):
        lines = []
        lines.append(self.makeDocumentClass())
        for i in self.makePackageList():
            lines.append(i)
        lines.append(self.makeDocumentBegin())
        return lines

    # Make title
    title_line_styles = []
    title_lines = []
    title_position = 1
    def makeTitle(self):
        lines = []
        if self.title_position == 0:
            pos = "flushleft"
        elif self.title_position == 1:
            pos = "center"
        else:
            pos = "flushright"
        lines.append(r"\begin{%s}"%pos)
        for i in self.title_lines:
            lines.append(self.title_line_styles[i[0]]%i[1])
        lines.append(r"\end{%s}"%pos)
        return lines

    # Make end
    def makeEnd(self):
        return r"\end{document}"

    # Make vertical space
    def makeVerticalSpace(self, amt):
        return r"\vspace{%s}"%amt

    # Compile whole document
    def makeDocument(self):
        lines = []
        # Make preamble
        for i in self.makePreamble():
            lines.append(i)
        # Make title
        for i in self.makeTitle():
            lines.append(i)
        # Make end
        lines.append(self.makeEnd())
        return lines

# Test document compile
if __name__ == "__main__":
    doc = LaTeXDocument()
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
        print(i, file=test_file)
    test_file.close()
