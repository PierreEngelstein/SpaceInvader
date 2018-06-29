# SpaceInvader
Space Invader Project for ISTIA

## Python version ##
For the moment, this project works fine on python 2 but not on python 3. You can try on python 3, but you should not expect it to work correctly.

## Python libraries needed ##
 - Tkinter for graphics
 	- Installation on Debian : `sudo apt-get install python-tk`
	- Installation on Fedora : `sudo dnf install python2-tkinter`
 - PIL (pillow) for image file management
 	- Installation : `pip install Pillow`
 - pyaudio and wave for sounds (still bugs)
 	- to install on debian (and derivatives) : `sudo apt-get install python-pyaudio`
	- to install on fedora (and derivatives) : `sudo dnf install portaudio-devel redhat-rpm-config` and `pip install --user pyaudio`
	- We still have errors that cause the game to lag when using pyaudio, mainly because of the jack server. If you want to avoid the main errors, please modify the file `/usr/share/alsa/alsa.conf`, by commenting the following lines :
		- `pcm.rear cards.pcm.rear`
		- `pcm.center_lfe cards.pcm.center_lfe`
		- `pcm.side cards.pcm.side`
		- All the lines that starts with `pcm.surround`
