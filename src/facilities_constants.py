#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 02/06/2008 
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

# DICTIONARIES REGARDING RESOURCES REQD TO BUILD EACH FACILITY PER BUILDING

RES_REQD_BUILD_HOUSE = {'BUILDING MATERIAL' : 5 , 'TOOLS' : 5 , 'WATER' :3 }
RES_REQD_BUILD_HOSPITAL = {'BUILDING MATERIAL' : 25 , 'TOOLS' : 20 , 'WATER' : 8 }
RES_REQD_BUILD_SCHOOL = {'BUILDING MATERIAL' : 20 , 'TOOLS' : 20 , 'WATER' : 8 }
RES_REQD_BUILD_WORKSHOP = {'BUILDING MATERIAL' : 25 , 'TOOLS' : 10 , 'WATER' : 10 }
RES_REQD_BUILD_FARM = {'BUILDING MATERIAL' : 0 , 'TOOLS' : 5 , 'WATER' : 15 }
RES_REQD_BUILD_FOUNTAIN = {'BUILDING MATERIAL' : 10 , 'TOOLS' : 20 , 'WATER' : 0 }

# MANPOWER REQD TO BUILD EACH FACILITY PER BUILDING

MANP_REQD_BUILD_HOUSE = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 2 }
MANP_REQD_BUILD_HOSPITAL = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 10 } 
MANP_REQD_BUILD_SCHOOL = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 8 }
MANP_REQD_BUILD_WORKSHOP = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4 }
MANP_REQD_BUILD_FARM = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 2 }
MANP_REQD_BUILD_FOUNTAIN = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4 }

# DICTIONARY OF ALL THE MANPOWER DISTRIBUTION CHANGES WHEN SETTING A FACILITY

FACILITY_MANP_DICT_BUILD = { 'HOUSING' : MANP_REQD_BUILD_HOUSE , 'HOSPITAL' : MANP_REQD_BUILD_HOSPITAL , 'SCHOOL' : MANP_REQD_BUILD_SCHOOL , 'WORKSHOP' : MANP_REQD_BUILD_WORKSHOP , 'FARM' : MANP_REQD_BUILD_FARM , 'FOUNTAIN' : MANP_REQD_BUILD_FOUNTAIN }







# DICTIONARIES OF RESOURCES REQD TO UPGRADE A FACILITY PER BUILDING  ( ASSUMPTION : NO MANPOWER IS REQD TO UPGRADE A FACILITY )

RES_REQD_UPGRADE_HOUSE = {'BUILDING MATERIAL' : 2 , 'TOOLS' : 2 }
RES_REQD_UPGRADE_HOSPITAL = {'BUILDING MATERIAL' : 10 , 'TOOLS' : 5 }
RES_REQD_UPGRADE_SCHOOL = {'BUILDING MATERIAL' : 8 , 'TOOLS' : 5 }
RES_REQD_UPGRADE_WORKSHOP = {'BUILDING MATERIAL' : 10 , 'TOOLS' : 5 }
RES_REQD_UPGRADE_FARM = {'BUILDING MATERIAL' : 0 , 'TOOLS' : 3 }
RES_REQD_UPGRADE_FOUNTAIN = {'BUILDING MATERIAL' : 2 , 'TOOLS' : 5 }
 




# DICTIONARIES OF RESOURCES BEING CONSUMED BY EACH FACILITY PER BUILDING

RES_CONS_HOUSE = { None : None }										 # Remember that resources are being 															 # consumed by manpower also so we need to 															 # make that thing too... a TODO for 
														 # controller
RES_CONS_HOSPITAL = { 'MEDICINE' : 2 , 'WATER' : 5 }
RES_CONS_SCHOOL = { 'BOOKS' : 2 , 'WATER' : 2 }
RES_CONS_WORKSHOP = { None : None }
RES_CONS_FARM = { 'WATER' : 10 }
RES_CONS_FOUNTAIN = { None : None }


# DICTIONARIES OF RESOURCES BEING PRODUCED BY THE FACILITY PER BUILDING

RES_PROD_HOUSE = { None : None }
RES_PROD_HOSPITAL = { 'MEDICINE' : 1 }  									 # WE CAN MAKE IT TO ZERO EVEN 
RES_PROD_SCHOOL = { None : None }
RES_PROD_WORKSHOP = { 'TOOLS' : 15 }
RES_PROD_FARM = { 'FOOD' : 100 , 'RICE' : 0 , 'WHEAT' : 0 , 'BEANS' : 0 , 'SUGAR' : 0 , 'SALT' : 0 , 'OILS' : 0 , 'WATER' : 0 } 
														 #THIS HAS TO BE DECIDED BY THE USER, BY 															 #DEFAULT THEIR VALUE HAS BEEN PUT EQUAL TO 															 #ZERO, TODO: FOR CONTROLLER FILL IN THE 															 #VALUES OF RICE ETC IN % 		
RES_PROD_FOUNTAIN = { 'WATER' : 25 }




# MANPOWER DISTRIBUTION CHANGED BY EACH FACILITY, THIS WILL INCREASE OR DECREASE AT BUILDIN OR UPGRADATION OF A FACILITY AND NOT AT EVERY TURN

MANP_DIST_HOUSE = { 'SHELTERED PEOPLE' : 4 }
MANP_DIST_HOSPITAL = { 'EMPLOYED PEOPLE IN HOSPITAL' : 10 ,  'HEALTHY PEOPLE' : 25 } 				 #BY HEALTHY PEOPLE I MEAN THE NUMBER OF 															 #PEOPLE THAT CAN BE MADE HEALTHY BY A 	 															 #HOSPITAL 
MANP_DIST_SCHOOL = { 'EMPLOYED PEOPLE IN SCHOOL' : 8 , 'EDUCATED PEOPLE' : 20 }
MANP_DIST_WORKSHOP = { 'EMPLOYED PEOPLE IN WORKSHOP' : 10 }
MANP_DIST_FARM = { 'EMPLOYED PEOPLE IN FARM' : 10 }             						 # PEOPLE FED = FOOD PRODUCED / 5 ,PEOPLE 															 # FED NEEDS TO BE INCREMENTED BY THE  															 # CONTROLLER AS FOOD CAN BE BOUGHT BY THE 															 # MARKET ALSO , TODO : CONTROLLER
MANP_DIST_FOUNTAIN = { None : None }





# DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGES

FACILITY_MANP_DICT_RUN = { 'HOUSING' : MANP_DIST_HOUSE , 'HOSPITAL' : MANP_DIST_HOSPITAL , 'SCHOOL' : MANP_DIST_SCHOOL , 'WORKSHOP' : MANP_DIST_WORKSHOP , 'FARM' : MANP_DIST_FARM , 'FOUNTAIN' : MANP_DIST_FARM }



# DICTIONARY FOR MANPOWER DISTRIBUTION WHICH IS USED IN MODEL.PY

MANP_DIST_DICT = { 'TOTAL POPULATION' : 0 , 'SHELTERED PEOPLE' : 0 , 'EDUCATED PEOPLE' : 0 , 'HEALTHY PEOPLE' : 0 , 'PEOPLE FED' : 0 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0 , 'EMPLOYED PEOPLE IN SCHOOL' : 0 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0 , 'EMPLOYED PEOPLE IN FARM' : 0 }
