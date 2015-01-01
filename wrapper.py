"""Maya Wrapper

Attributes:
    MAYAPATH: Absolute path to Maya executable
    PYBLISHINSTALLDIR: Absolute path to Pyblish installation directory
    PYBLISHINTEGRATIONDIR: Absolute path to Pyblish for Maya
        integration directory
    PLUGINSDIR: Path to Pyblish plug-ins

"""

import os
import imp
import subprocess


MAYAPATH = r"c:\Program Files\Autodesk\Maya2015\bin\maya.exe"
PYBLISHINSTALLDIR = r"c:\Python27\lib\site-packages"
PLUGINSDIR = "%s\pyblish" % os.getcwd()


def main():
    try:
        path = imp.find_module("pyblish_maya")[1]
        PYBLISHINTEGRATIONDIR = os.path.join(path, "pythonpath")
    except:
        return 1

    if not os.path.isfile(MAYAPATH):
        return 2

    # Set environment variables
    os.environ["PYBLISHPLUGINPATH"] = PLUGINSDIR
    os.environ["PYTHONPATH"] = "{root};{integration}".format(
        root=PYBLISHINSTALLDIR,
        integration=PYBLISHINTEGRATIONDIR)

    print "Setting PYTHONPATH = %s" % os.environ["PYTHONPATH"]
    print "Setting PYBLISHPLUGINPATH = %s" % os.environ["PYBLISHPLUGINPATH"]

    subprocess.Popen([MAYAPATH])

    return 0


if __name__ == '__main__':
    retval = main()

    if retval == 1:
        print "Error: Pyblish for Maya not found"

    if retval == 2:
        print "Error: Maya not found @ %s" % MAYAPATH
