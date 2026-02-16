# Problem Statement

Given multiple vendor IP blocks with port definitions (name, direction, width),
automatically generate a synthesizable SystemVerilog top module that:

- Declares required interconnect wires
- Instantiates all IP blocks
- Connects ports correctly
- Avoids manual wiring errors
- Is scalable to N IP blocks

Goal:
Eliminate manual top-level integration effort using Python automation.
