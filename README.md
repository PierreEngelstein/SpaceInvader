# SpaceInvader
Space Invader Project for ISTIA

Python libraries used (we will provide an setup script later):
	->Tkinter for graphics
	->PIL(pillow) for image file management
	->pyaudio and wave for sounds
		debian : apt-get install python-pyaudio
		fedora : 
		There are currently some errors (using linux) caused by pyaudio wanting to use jack server
		To avoid getting these errors, please modify the file /usr/share/alsa/alsa.conf :
			comment the following lines:
			   pcm.rear cards.pcm.rear
			   pcm.center_lfe cards.pcm.center_lfe
			   pcm.side cards.pcm.side
			   All the lines that starts with pcm.surround