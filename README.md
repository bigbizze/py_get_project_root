# py_get_project_root

A simple package for resolving project root in most situations.
I found myself rewriting something to resolve this in various 
different project structures & situations, annoyingly, so I wroto
this to save myself time.

Let me know if you run into any situations where it doesn't resolve
the project root path correctly.

____

```py
import get_proj_root from get_project_root

project_root = get_proj_root(ignore_cwd=False)
# >> "C:/Users/person/source/some_project/"

```

____

### ignore_cwd: 
  Ignores the current working directory for deriving the root path.
  In the case where the directory of the file this is called from is 
   the same as the current working directory CWD, it will return
   the current working directory if this is set to True.
