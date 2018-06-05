from cx_Freeze import *

executables = [Executable("QuizingProject.py")]

options = {
	"build_exe" : {
		"packages" : ["Assets"]
	}
}


setup(name='QuizingProject',
      version='1.1',
      description='Script to make quizes and play them',
      options=options,
      executables=executables)