Rubik's cube simulation with a built-in tutorial on how to solve the cube.
Includes:
 - Virtual cube, interactive via clickable arrows or keyboard shortcuts
 - General strategy for each step
 - Specific hints for each step
 - Ability to change cube sticker colors (in-progress)
 - Light/Dark Mode

Pip package name: QB-Solver (https://pypi.org/project/QB-solver/)

Install requires: pip packages ursina, rubik-cube, and psd-tools3
 - These are automatically installed when running `pip install qb-solver`
 - These can also be installed manually via `pip install ursina rubik-cube psd-tools3`

Deploying the package requires: setuptools, wheel, twine
 - Steps for deploying the package:
   1. Run `pip install setuptools wheel twine`
   2. Make appropriate changes to setup.py (change version number)
   3. If it exists, delete the dist folder from the QB/ directory via `rm -r dist`
   4. Run `python3 setup.py sdist bdist_wheel`
   5. Run `twine upload dist/*` and enter PyPi credentials
 - NOTE: all of these commands are run in the QB/ directory

Run command: "python3 -m qb_solver", or "run_simulation"
 - NOTE: "run_simulation" is not currently functional

GitHub Repo: https://github.com/a-penton/QB
