# choreo_GUI
This is the sister project to **choreo**, a Python package aiming at finding periodic solutions to the gravitational N-body problem. **choreo-GUI** is a Graphical User Interface (GUI) to **choreo**, facilitating the process of setting up the optimization procedure, and providing means to visualize solutions. Thanks to [Pyodide](https://pyodide.org/en/stable/), the solver can be launched directly in the browser.

## Try out this project, no installation required!

Check out the online in-browser GUI: https://gabrielfougeron.github.io/choreo/

## Power up the GUI solver with the CLI backend
Using clang or gcc as a C compiler, the single-threaded CLI solver is about 3 times faster that the wasm in-browser GUI solver. In addition, several independent single-threaded solvers can be launched simultaneously using a single command.

To use the CLI backend, follow these steps:

- Install the package
- In the GUI, define a workspace folder under `Play => Workspace => Setup Workspace`
- Every time the workspace is reloaded under `Play => Workspace => Reload Workspace` **or** every time a new initial state is generated in the GUI, a new configuration file `choreo_config.json` is written to disk.
- In the command line, run the installed script as `choreo_CLI_search -f /path/to/workspace/folder/` 

## Online documentation

Available at: https://gabrielfougeron.github.io/choreo-docs/
