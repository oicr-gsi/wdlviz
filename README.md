# wdlviz
Python tool to create DOT diagrams for WDL workflows

---

## Overview
The [`wdlviz.py` script](https://github.com/chanzuckerberg/miniwdl/blob/main/examples/wdlviz.py) originates from the the documentation for the [`miniwdl`](https://github.com/chanzuckerberg/miniwdl) Python package. It has been adopted by OICR to streamline WDL workflow documentation practices.

By default, wdlviz outputs: 
* A PNG workflow diagram
* A DOT file digraph to stdout

The DOT file may be reformatted and rendered to create an improved workflow diagram.

---

## Usage
The primary usage of wdlviz is to create a diagram for a local WDL file:

```
./wdlviz.py /path/to/workflow.wdl
```

To inlclude inputs and/or outputs to the diagram, enable these flags:

```
./wdlviz.py --inputs --ouputs /path/to/workflow.wdl
```

Diagrams can also generated from WDL URIs:

```
# IN PROGRESS
```

`wdlviz` can also generate diagram from stdin:
```
# IN PROGRESS
```
---

## Manual Editing
DOT files wil oftern require some modification and styling before the rendered graphs are ready for use. For a full breakdown on DOT language, see the [documentation](https://graphviz.org/documentation/).

To render out a manually modified DOT file, you can use the `dot.py` script. The script requires two arguments:
* DOT filepath
* Output format

See below:

```
./dot.py /path/to/workflow.dot png
```
You can render diagrams in:
* png (recommeded)
* svg (recommended)
* jpg
* pdf

> The full list of output formats is available [here](https://graphviz.org/docs/outputs/).

Using the dot.py scripts evades the need for the Ubuntu/Debian `dot` package and standardizes use across systems.