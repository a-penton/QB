from setuptools import setup

setup(
	name="QB-solver",
	version="0.1.4.7.1",
	packages=["qb_solver",],	# name of modules
	url="https://github.com/a-penton/QB",
	# license
	author="Andrew Penton, Heinrich Perez, Steven Perez, Noah Sharpe, Daniel Shinkarow",
	# author_email
	description="Rubik's cube simulation and tutorial",
	install_requires=["ursina", "rubik-cube", "psd-tools3"],

	entry_points = 
	{ "console_scripts":
		[
			"run_simulation=qb_solver.main:main",
			#"command_name_2 = src.file_name:func_name"
		]
	}
)
