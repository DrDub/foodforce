#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#


# This file is meant for creating a setup for windows in exe format.
# You needs to have py2exe installed for that.
# Run it as python setup.py py2exe


from distutils.core import setup
import py2exe
import os

setup(windows = [{"script":"Foodforce2.py"}],data_files=[('data', [os.path.join("data","tileset2.png")
                                                                   ,os.path.join("data","logo.png")
                                                                   ,os.path.join("data","earthquake1.png")
                                                                   ,os.path.join("data","earthquake2.png")
                                                                   ,os.path.join("data","earthquake3.png")
                                                                   ,os.path.join("data","fountain.png")
                                                                   ,os.path.join("data","farm.png")
                                                                   ,os.path.join("data","top.png")
                                                                   ,os.path.join("data","WFPLOGO.png")
                                                                   ,os.path.join("data","Wfpwork.png")
                                                                   ,os.path.join("data","house_upgrade0.png")
                                                                   ,os.path.join("data","house_upgrade1.png")
                                                                   ,os.path.join("data","house_upgrade2.png")
                                                                   ,os.path.join("data","house_upgrade3.png")
                                                                   ,os.path.join("data","market.png")
                                                                   ,os.path.join("data","people.png")
                                                                   ,os.path.join("data","tileset.png")
                                                                   ,os.path.join("data","school_upgrade0.png")
                                                                   ,os.path.join("data","school_upgrade1.png")
                                                                   ,os.path.join("data","school_upgrade2.png")
                                                                   ,os.path.join("data","school_upgrade3.png")
                                                                   ,os.path.join("data","hospital_upgrade0.png")
                                                                   ,os.path.join("data","hospital_upgrade1.png")
                                                                   ,os.path.join("data","hospital_upgrade2.png")
                                                                   ,os.path.join("data","hospital_upgrade3.png")
                                                                   ,os.path.join("data","workshop_upgrade0.png")
                                                                   ,os.path.join("data","workshop_upgrade1.png")
                                                                   ,os.path.join("data","workshop_upgrade2.png")
                                                                   ,os.path.join("data","workshop_upgrade3.png")
                                                                   ,os.path.join("data","soundtrack.ogg")
                                                                   ,os.path.join("data","dot_fountain.png")
                                                                   ,os.path.join("data","dot_farm.png")
                                                                   ,os.path.join("data","dot_workshop.png")
                                                                   ,os.path.join("data","dot_school.png")
                                                                   ,os.path.join("data","dot_hospital.png")
                                                                   ,os.path.join("data","dot_house.png")
                                                                   ,os.path.join("data","dot_market.png")
                                                                   ,os.path.join("data","map.png")])
                                                         ,('art', [os.path.join('art','button.png')
                                                                   ,os.path.join('art','closebutton.png')
                                                                   ,os.path.join('art','optionbox.png')
                                                                   ,os.path.join('art','ajmal.png')
                                                                   ,os.path.join('art','kamat.png')
                                                                   ,os.path.join('art','chatbox.png')
                                                                   ,os.path.join('art','imagebox.png')
                                                                   ,os.path.join('art','son.png')
                                                                   ,os.path.join('art','sukhdev.png')
                                                                   ,os.path.join('art','villager.png')
                                                                   ,os.path.join('art','shadebutton.png')
                                                                   ,os.path.join('art','checkbox.png')
                                                                   ,os.path.join('art','combobox.png')
                                                                   ,os.path.join('art','button_green.png')])
                                                         ,('.',['font.ttf'
                                                                ,'data.pkl'
                                                                ,'data2.pkl'
                                                                ,'data3.pkl'
                                                                ,'data4.pkl'
                                                                ,'data5.pkl'
                                                                ,'data6.pkl'
                                                                ,'data7.pkl'
                                                                ,'data8.pkl'
                                                                ,'storyboard.pkl'
                                                                ,'graphics_layout.pkl']) ])