# bananaPepper Pitfalls to learn from

## 12/12/18 Importing python modules
After any "import x" statement, consider immediately using "reload(x)".
The reason is that all "behaviors" are actually loaded in 1 Python session.
Which means when you "import" your library the second time, the library already exists in this Python session, and Python just gives you back the old module.
Using reload forces Python to get the latest updated version of it.﻿
