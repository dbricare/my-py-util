# Contains a function to open a file dialog box


# if __name__ == '__main__':

def openfdiag(DialogCaption=None, ReadFolder=None, FileFilter=None):

	"""
	This function uses Qt to open a file dialog box. Still needs some tweaking.
	"""
	from PySide import QtCore, QtGui
	import sys

	app = QtGui.QApplication.instance()
	if app is None:
		app = QtGui.QApplication(sys.argv)	
    
	FileList, _ = QtGui.QFileDialog.getOpenFileNames(None, \
	caption=DialogCaption, dir=ReadFolder, filter=FileFilter)
		
	if not FileList:
		raise ValueError('File list is empty.') 
		
	return (FileList)

if __name__ == '__main__':
	openfdiag()