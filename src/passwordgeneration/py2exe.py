# -*- coding: utf-8 -*-
'''
Created on 26 february. 2018 year.

@author: Aleksandr.Muga
'''
import os, shutil, sys
from pip._vendor.distlib.compat import raw_input

class Py2Exe:
    def py2exe(self, argv = None):
        if argv == None:
            FileName = raw_input('Enter the name of the py file that you want to convert (should be in the current directory):').strip()
        else:
            FileName = argv[1].strip()
            
        if FileName[0] == '\'' or FileName[0] == "\"":
            FileName = FileName[1:-1]
        FileName = FileName.split('\\')[-1]
        
        CurrentPath = os.getcwd()
        PyInstaller = sys.path[0] + "\\PyInstaller-3.1.1\\pyinstaller.py"
        PyFile_1 = sys.path[0] + '\\' + FileName
        SpecFile = CurrentPath + '\\' + FileName[:-3] + '.spec'
        ExeFile_1 = "%s.exe" % (FileName[:-3])
        print(str(ExeFile_1))
        ExePath_1 = "%s\\dist\\%s"%((CurrentPath, ExeFile_1))
        CopyPath_1 = "%s\\%s" % ((CurrentPath, ExeFile_1))
        
        if os.path.exists(sys.path[0] + '\\' + ExeFile_1):
            print ("%sAll ready exist, don`t need convert" % (ExeFile_1))
            return False
        else:
            os.system('python "%s" --onefile "%s"' % (PyInstaller, PyFile_1))
        
        if os.path.exists(ExePath_1):
            print('exe generated')
            print('Copy file%s in%s...' % (ExePath_1, CopyPath_1))
            shutil.copy(ExePath_1, CopyPath_1)
            if argv != None:
                print('Copy file%s in%s...' % (CopyPath_1, sys.path[0] + '\\' + ExeFile_1))
                shutil.move(CopyPath_1, sys.path[0] + '\\' + ExeFile_1)
            else:
                print('Build Error')
                print('File%s not exists' % (ExePath_1))
                return False
            
            if os.path.exists(CurrentPath + '\\dist'):
                print('Delete dir%s ...' % (CurrentPath + '\\dist'))
                shutil.rmtree(CurrentPath + '\\dist')
            else:
                print('Dir%s not exists' % (CurrentPath + '\\dist'))
                return False
            
            if os.path.exists(CurrentPath + '\\build'):
                print('Del dir%s ...' % (CurrentPath + '\\build'))
                shutil.rmtree(CurrentPath + '\\build')
            else:
                print('Dir%s not exists' % (CurrentPath + '\\build'))
                return False
                
            if os.path.exists(SpecFile):
                print('Del files%s……' % (SpecFile))
                os.remove(SpecFile)
            else:
                print('File%s not exists'%(SpecFile))
                return False
            return True
            
        
if __name__=='__main__':
    if len(sys.argv) == 1:
        Py2Exe().py2exe()
    elif len(sys.argv) == 2:
        Py2Exe().py2exe(sys.argv)
    else:
        print('ERROR:parameters!\n')
    raw_input('\nPress(Enter) to exit……')
            
            
            
            
                