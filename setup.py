from setuptools import setup

setup(
	name="QB-solver",
	version="0.1.7",
	packages=["qb_solver",],	# name of modules
	package_data={
		"qb_solver": [
			"Models/*.obj",
			"Models/*.png",
			"Models/*.jpeg",
			"Models/*.jpg"
			"Models/*.gif",
			"Models/*.mp3",
			"Models/*.wav",
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
	install_requires=["ursina==3.5.0",
		"rubik-cube==0.0.1",
		"psd-tools3==1.8.2"],
	scripts=['bin/run_simulation']
)
