import tempfile
import sys
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

def render(sources, showImage = False, output = None, yieldsPixels = False, canvas = (10,10)):
    if canvas == None: canvas = ""
    else: canvas = '''
\draw[fill = white, white] (0,0) rectangle (%d,%d);
'''%(canvas[0],canvas[1])

    sources = ["\\begin{tikzpicture}\n" + canvas + "\n" + s + "\n\\end{tikzpicture}"
               for s in sources ]
    source = "\n".join(sources)
    source = '''
\\documentclass[convert={density=300,size=300x300,outext=.png},tikz]{standalone}

\\begin{document}
%s
\\end{document}
''' % (source)

    fd, temporaryName = tempfile.mkstemp(suffix = ".tex")
    with os.fdopen(fd, 'w') as new_file:
        new_file.write(source)
    os.system("cd /tmp; echo X|pdflatex -shell-escape %s > /dev/null 2> /dev/null" % temporaryName)

    temporaryPrefix = temporaryName[:-4]
    temporaryImages = [temporaryPrefix + ".png"]
    if len(sources) > 1:
        pattern = "%s-%0"+str(len(str(len(sources) - 1)))+"d.png"
        temporaryImages = [pattern%(temporaryPrefix,j) for j in range(len(sources)) ]

    if showImage:
        for temporaryImage in temporaryImages:
            os.system("feh %s" % temporaryImage)

    returnValue = []
    if output != None:
        os.system("mv %s %s 2> /dev/null" % (temporaryImages[0], output))
        temporaryImages = [output]
        
    if yieldsPixels:
        for temporaryImage in temporaryImages:
            im = Image.open(temporaryImage).convert('L')
            (width, height) = im.size
            greyscale_map = list(im.getdata())
            greyscale_map = np.array(greyscale_map)
            greyscale_map = greyscale_map.reshape((height, width))
            returnValue.append(greyscale_map/255.0)


    os.system("rm %s*" % temporaryPrefix)
    if returnValue != []: return returnValue

def animateMatrices(matrices):
    fig = plot.figure() # make figure
    im = plot.imshow(matrices[0], cmap=plot.get_cmap('bone'), vmin=0.0, vmax=1.0)

    # function to update figure
    def updatefig(j):
        # set the data in the axesimage object
        im.set_array(matrices[j])
        # return the artists set
        return im,
    # kick off the animation
    ani = animation.FuncAnimation(fig, updatefig, frames=range(len(matrices)), 
                              interval=50, blit=True)
    plot.show()

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    i = sys.stdin if inputFile == '-' else open(inputFile, "r")
    source = i.read()
    render(source, outputFile)
