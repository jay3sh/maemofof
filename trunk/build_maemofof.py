#!/usr/bin/env python

import py2deb
import os
import sys


if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass
    print
    p=py2deb.Py2deb("maemofof")   #This is the package name and MUST be in lowercase! (using e.g. "mClock" fails miserably...)
    p.description="Maemo port of Frets on Fire"
    p.author="Jayesh Salvie"
    p.mail="jayeshsalvi@gmail.com"
    p.depends = "python2.5 (>= 2.5.1-1osso5), python2.5-osso, python2.5-pygame"
    p.section="user/games"
    p.icon = "/home/user/MyDocs/maemofof/icon-48x48.png"
    p.arch="all"                #should be all for python, any for all arch
    p.urgency="low"             #not used in maemo onl for deb os
    p.distribution="fremantle"
    p.repository="extras-devel"

    p.postinstall="""#!/bin/sh
    chmod +x /usr/bin/maemofof.py""" #Set here your post install script


    version = '0.1'
    build = '1'
    changeloginformation = 'First Release'
    dir_name = 'src'

    for root, dirs, files in os.walk(dir_name):
        real_dir = root[len(dir_name):]
        fake_file = []
        for f in files:
            fake_file.append(root + os.sep + f + "|" + f)
        if len(fake_file) > 0:
            p[real_dir] = fake_file

    print p
    r = p.generate(version,build,changelog=changeloginformation,tar=True,dsc=True,changes=True,build=False,src=True)

