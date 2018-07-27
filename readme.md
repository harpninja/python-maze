# Python Maze
Two scripts to generate a maze and render it in Maya. The shaders are configured for Arnold render.

### Run the maze generator script
* Uses Prim's algorithm.
* Run from the command line.
* The environment used was the latest Anaconda python distribution, plus NumPy.
* NumPy cannot be accessed from Maya Python, which is why there are two scripts.
* Generates a file called results.txt which should be selected when the Maya script runs.

### Run the script in Maya
* Open the Script Editor.
* Switch tabs from MEL to Python.
* Paste the code into the window.
* Press the Execute button on the tool bar at the top of the window.

### Final image
![Final image of Arnold rendered spheres](/mazeHD.jpg)
Format: ![Final image of Arnold rendered spheres](url)
