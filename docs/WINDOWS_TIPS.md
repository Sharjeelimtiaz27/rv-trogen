\# Windows-Specific Tips



Tips for using RV-TroGen on Windows, especially on restricted systems like university PCs.



---



\## Use `python -m pip` Instead of `pip`



\*\*Always use:\*\*

```bash

python -m pip install -e .

```



\*\*Instead of:\*\*

```bash

pip install -e .

```



\*\*Why?\*\*

\- Works on group policy restricted systems

\- More reliable on Windows

\- Official Python recommendation

\- Always uses correct Python version



---



\## Use `python -m pytest` Instead of `pytest`



\*\*Always use:\*\*

```bash

python -m pytest tests/ -v

```



\*\*Instead of:\*\*

```bash

pytest tests/ -v

```



\*\*Same reasons as above!\*\*



---



\## Virtual Environment Issues



If `venv\\Scripts\\activate` is blocked:



\*\*Don't worry!\*\* You can work without virtual environments:

```bash

\# Just install globally

python -m pip install -e .



\# Everything works the same

python src/parser/rtl\_parser.py examples/ibex/original/ibex\_cs\_registers.sv

```



\*\*Or use full path without activating:\*\*

```bash

venv\\Scripts\\python.exe -m pip install -e .

venv\\Scripts\\python.exe -m pytest tests/ -v

```



---



\## PowerShell Execution Policy



If you see "blocked by group policy" errors:



\*\*Try this:\*\*

1\. Open PowerShell as Administrator

2\. Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

3\. Try again



\*\*Or just use Command Prompt (cmd) instead of PowerShell!\*\*



---



\## Long Path Names



If you get errors about path length:



Windows has a 260-character path limit. Your OneDrive path is quite long:

`C:\\Users\\shimti\\OneDrive - Tallinna Tehnikaülikool\\Sharjeel\\Taltech\\PhD\\MY Articles\\TroGen\_V`



\*\*Solution:\*\*

1\. Move project to shorter path: `C:\\Projects\\rv-trogen`

2\. Or enable long paths (requires admin)



---



\## File Access Issues



OneDrive can sometimes lock files.



\*\*If you get "file in use" errors:\*\*

1\. Pause OneDrive sync

2\. Make your changes

3\. Resume OneDrive sync



---



\## Running Scripts



\*\*Always use:\*\*

```bash

python script\_name.py

```



\*\*Not:\*\*

```bash

script\_name.py

```



\*\*Or use:\*\*

```bash

python -m module\_name

```



---



\## Git Commands on University PC



If Git is blocked:



\*\*Use GitHub Desktop\*\* (usually allowed) or work on personal machine.



---



\## Summary - Your Command Patterns



\*\*Installation:\*\*

```bash

python -m pip install -e .

```



\*\*Testing:\*\*

```bash

python -m pytest tests/ -v

```



\*\*Running Scripts:\*\*

```bash

python src/parser/rtl\_parser.py <file.sv>

python scripts/batch\_parse.py --dir <directory>

```



\*\*These patterns work reliably on restricted Windows systems!\*\*

