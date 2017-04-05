Untested on Windows and linux.

# Requirement 
	Python 2.x

	dlib 
		pip install dlib

# Requirement for dlib 
	### cmake 
	### boost (from boost.org)
		follow as :
		1. install boost from boost.org
		2. Run 
			./bootstrap.sh --with-libraries=python
			./b2
			sudo ./b2 install
	### Xquartz for macOS (x11 for linux)