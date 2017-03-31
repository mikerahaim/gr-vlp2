# gr-vlp2
Restarting the GNURadio repository for visible light positioning to clean up files and organize the file functionality.
This OOT module requires Eigen as a dependency. Before installing gr-vlp2, install Eigen by using 'apt-get install libeigen3' or by downloading and building the source code from Eigen's website.

To install, follow the steps below:

1-) cd to the gr-vlp2 directory

2-) Create a build directory with 'mkdir build' and move into the directory with 'cd build/'

3-) Run cmake with the path to your local gnuradio installation (assuming installed via PyBOMBS): 'cmake -DCMAKE_INSTALL_PREFIX=<target> ../'

4-) Run 'make'

5-) Test the build with 'make test' (shouldn't be any failures)

6-) Install with 'make install'

7-) Configure your linker/debugger with 'sudo ldconfig'

8-) Open gnuradio-companion and you should find a module for VLP. You can test the grc flowgraph(s) in ./examples to check functionality.
