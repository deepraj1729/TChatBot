from setuptools import setup, find_packages 

with open('requirements.txt') as f: 
	requirements = f.readlines() 

def readme():
	with open('README.md') as f:
		README = f.read()
	return README

setup( 
		name ='TChatBot', 
		version ='0.1.0', 
		author ='Deepraj Baidya', 
		author_email ='bdeeprajrkm1@gmail.com', 
		url ='https://github.com/deepraj1729/TChatBot', 
		description ='A ChatBot framework to create customizable all purpose Chatbots using NLP, Tensorflow, Speech Recognition', 
		long_description = readme(), 
		long_description_content_type ="text/markdown", 
		license ='MIT', 
		packages = find_packages(), 
		entry_points ={ 
			'console_scripts': [ 
				'tchatbot = TChatBot.main:main'
			] 
		}, 
		classifiers =( 
			"Programming Language :: Python :: 3", 
			"License :: OSI Approved :: MIT License", 
			"Operating System :: OS Independent", 
		), 
		keywords ='A Customizable ChatBot framework with Tensorflow,NLP,Speech Recognition',
		include_package_data = True, 
		install_requires = requirements, 
		zip_safe = False
) 
