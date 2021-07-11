from setuptools import setup

setup(
	name="QB-solver",
	version="0.1.4.8.9",
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
	license = "GPL3",
	author="Andrew Penton, Heinrich Perez, Steven Perez, Noah Sharpe, Daniel Shinkarow",
	author_email = "andrew.penton@gmail.com",
	description="Rubik's cube simulation and tutorial",
	install_requires=["ursina", "rubik-cube", "psd-tools3"],
	scripts=['bin/run_simulation']
)
