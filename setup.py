from setuptools import setup

setup(
	name="QB-solver",
	version="0.1.4.8.5",
	packages=["qb_solver",],	# name of modules
	package_data={
		"qb_solver": [
			"Models/*.obj",
			"Models/*.png",
			"Models/Notation/*.png",
			"hints/*.png"
		],
	},
	include_package_data=True,	# make sure resources are included
	url="https://github.com/a-penton/QB",
	# license
	author="Andrew Penton, Heinrich Perez, Steven Perez, Noah Sharpe, Daniel Shinkarow",
	# author_email
	description="Rubik's cube simulation and tutorial",
	install_requires=["ursina", "rubik-cube", "psd-tools3"],

	entry_points = 
	{ "console_scripts":
		[
			"run_simulation=qb_solver.__main__:main",
			#"command_name_2 = qb_solver.file_name:func_name"
		]
	}
)
