# The module pdb defines an interactive source code debugger for Python
# programs. It supports setting (conditional) breakpoints and single stepping
# at the source line level, inspection of stack frames, source code listing,
# and evaluation of arbitrary Python code in the context of any stack frame. It
# also supports post-mortem debugging and can be called under program control.

# it acts a bit line binding.pry in ruby

# https://docs.python.org/release/2.7/library/pdb.html
# insert following snippet in any piece of code
import pdb
pdb.set_trace()

# the execution flow call set_trace(), the debugger will take over the
# terminal and display the familiar (Pdb) prompt, being the environment that of
# the scope where set_trace() was called.
