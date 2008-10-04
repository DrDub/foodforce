#! /usr/bin/env python##   Author : Mohit Taneja (mohitgenii@gmail.com)#   Date : 02/06/2008 ##   This program is free software; you can redistribute it and/or modify#   it under the terms of the GNU General Public License as published by#   the Free Software Foundation; either version 2 of the License, or#   (at your option) any later version.##   This program is distributed in the hope that it will be useful,#   but WITHOUT ANY WARRANTY; without even the implied warranty of#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the#   GNU General Public License for more details.##   You should have received a copy of the GNU General Public License#   along with this program; if not, write to the Free Software#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.## DICTIONARIES REGARDING RESOURCES REQD TO BUILD EACH FACILITY PER BUILDINGCOST_HOUSE = {'BUILDING MATERIAL' : 5.0 , 'TOOLS' : 5.0 , 'WATER' :3.0 }COST_HOSPITAL = {'BUILDING MATERIAL' : 25.0 , 'TOOLS' : 20.0 , 'WATER' : 8.0 }COST_SCHOOL = {'BUILDING MATERIAL' : 20.0 , 'TOOLS' : 20.0 , 'WATER' : 8.0 }COST_WORKSHOP = {'BUILDING MATERIAL' : 25.0 , 'TOOLS' : 10.0 , 'WATER' : 10.0 }COST_FARM = {'BUILDING MATERIAL' : 0.0 , 'TOOLS' : 5.0 , 'WATER' : 15.0 }COST_FOUNTAIN = {'BUILDING MATERIAL' : 10.0 , 'TOOLS' : 20.0 , 'WATER' : 0.0 }# MANPOWER REQD TO BUILD EACH FACILITY PER BUILDINGMANP_REQD_BUILD_HOUSE = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 2.0 }MANP_REQD_BUILD_HOSPITAL = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 10.0 } MANP_REQD_BUILD_SCHOOL = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 8.0 }MANP_REQD_BUILD_WORKSHOP = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4.0 }MANP_REQD_BUILD_FARM = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 2.0 }MANP_REQD_BUILD_FOUNTAIN = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4.0 }# DICTIONARY OF ALL THE MANPOWER DISTRIBUTION CHANGES WHEN SETTING A FACILITYFACILITY_MANP_DICT_BUILD = { 'HOUSE' : MANP_REQD_BUILD_HOUSE , 'HOSPITAL' : MANP_REQD_BUILD_HOSPITAL , 'SCHOOL' : MANP_REQD_BUILD_SCHOOL , 'WORKSHOP' : MANP_REQD_BUILD_WORKSHOP , 'FARM' : MANP_REQD_BUILD_FARM , 'FOUNTAIN' : MANP_REQD_BUILD_FOUNTAIN }FACILITY_NAMES = {'HOUSE' : 'House' , 'HOSPITAL' : 'Hospital' , 'SCHOOL' : 'School' , 'WORKSHOP' : 'Workshop' , 'FARM' : 'Farm' , 'FOUNTAIN' : 'Well'}# DICTIONARIES OF RESOURCES REQD TO UPGRADE A FACILITY PER BUILDING  ( ASSUMPTION : NO MANPOWER IS REQD TO UPGRADE A FACILITY )COST_LEVEL_HOUSE = {'BUILDING MATERIAL' : 2.0 , 'TOOLS' : 2.0 }COST_LEVEL_HOSPITAL = {'BUILDING MATERIAL' : 10.0 , 'TOOLS' : 5.0 }COST_LEVEL_SCHOOL = {'BUILDING MATERIAL' : 8.0 , 'TOOLS' : 5.0 }COST_LEVEL_WORKSHOP = {'BUILDING MATERIAL' : 10.0 , 'TOOLS' : 5.0 }COST_LEVEL_FARM = {'BUILDING MATERIAL' : 0.0 , 'TOOLS' : 3.0 }COST_LEVEL_FOUNTAIN = {'BUILDING MATERIAL' : 2.0 , 'TOOLS' : 5.0 } # DICTIONARIES OF RESOURCES BEING CONSUMED BY EACH FACILITY PER BUILDINGCONS_HOUSE = { }										 # Remember that resources are being 															 # consumed by manpower also so we need to 															 # make that thing too... a TODO for 														 # controllerCONS_HOSPITAL = { 'MEDICINE' : 2.0 , 'WATER' : 5.0 }CONS_SCHOOL = { 'BOOKS' : 2.0 , 'WATER' : 2.0 }CONS_WORKSHOP = { }CONS_FARM = { 'WATER' : 10.0 }CONS_FOUNTAIN = { }# DICTIONARIES OF RESOURCES BEING PRODUCED BY THE FACILITY PER BUILDINGPROD_HOUSE = { }PROD_HOSPITAL = { }  									 # WE CAN MAKE IT TO ZERO EVEN PROD_SCHOOL = { }PROD_WORKSHOP = { 'TOOLS' : 15.0 }MAX_FOOD_PROD_PER_FARM = 100PROD_FARM = { 'RICE' : 20.0 , 'WHEAT' : 20.0 , 'BEANS' : 20.0 , 'SUGAR' : 20.0 , 'SALT' : 10.0 , 'OILS' : 10.0 }														 #THIS HAS TO BE DECIDED BY THE USER, BY 															 #DEFAULT THEIR VALUE HAS BEEN PUT EQUAL TO 															 #ZERO, TODO: FOR CONTROLLER FILL IN THE 															 #VALUES OF RICE ETC IN % 		PROD_FOUNTAIN = { 'WATER' : 25 }# MANPOWER DISTRIBUTION CHANGED BY EACH FACILITY TO RUN THE FACILITY, THIS WILL INCREASE OR DECREASE AT BUILDIN OR UPGRADATION OF A FACILITY AND NOT AT EVERY TURNMANP_DIST_HOUSE = { }MANP_DIST_HOSPITAL = { 'EMPLOYED PEOPLE IN HOSPITAL' : 10.0 }  				 #BY HEALTHY PEOPLE I MEAN THE NUMBER OF 															 #PEOPLE THAT CAN BE MADE HEALTHY BY A 	 															 #HOSPITAL MANP_DIST_SCHOOL = { 'EMPLOYED PEOPLE IN SCHOOL' : 8.0 }MANP_DIST_WORKSHOP = { 'EMPLOYED PEOPLE IN WORKSHOP' : 10.0 }MANP_DIST_FARM = { 'EMPLOYED PEOPLE IN FARM' : 10.0 }             						 # PEOPLE FED = FOOD PRODUCED / 5 ,PEOPLE 															 # FED NEEDS TO BE INCREMENTED BY THE  															 # CONTROLLER AS FOOD CAN BE BOUGHT BY THE 															 # MARKET ALSO , TODO : CONTROLLERMANP_DIST_FOUNTAIN = { }# CHANGE IN MANPOWER DISTRIBUTION DUE TO THE FACILITIESMANP_CH_HOUSE = { 'SHELTERED PEOPLE' : 4.0 }MANP_CH_HOSPITAL = { 'HEALTHY PEOPLE' : 25.0 } MANP_CH_SCHOOL = { 'EDUCATED PEOPLE' : 20.0 }MANP_CH_WORKSHOP = { }MANP_CH_FARM = { }MANP_CH_FOUNTAIN = { }# DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGESFACILITY_MANP_DICT_CH = { 'HOUSE' : MANP_CH_HOUSE , 'HOSPITAL' : MANP_CH_HOSPITAL , 'SCHOOL' : MANP_CH_SCHOOL , 'WORKSHOP' : MANP_CH_WORKSHOP , 'FARM' : MANP_CH_FARM , 'FOUNTAIN' : MANP_CH_FOUNTAIN }# DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGES TO RUN FACILITYFACILITY_MANP_DICT_RUN = { 'HOUSE' : MANP_DIST_HOUSE , 'HOSPITAL' : MANP_DIST_HOSPITAL , 'SCHOOL' : MANP_DIST_SCHOOL , 'WORKSHOP' : MANP_DIST_WORKSHOP , 'FARM' : MANP_DIST_FARM , 'FOUNTAIN' : MANP_DIST_FOUNTAIN }# DICTIONARY OF ALL THE FACILITIES WITH THE RESOURCES THAT THEY CONSUMEFACILITY_RES_DICT_CONS = { 'HOUSE' : CONS_HOUSE , 'HOSPITAL' : CONS_HOSPITAL , 'SCHOOL' : CONS_SCHOOL , 'WORKSHOP' : CONS_WORKSHOP , 'FARM' : CONS_FARM , 'FOUNTAIN' : CONS_FOUNTAIN }# DICTIONARY FOR MANPOWER DISTRIBUTION WHICH IS USED IN MODEL.PYMANP_DIST_DICT = { 'TOTAL POPULATION' : 0.0 , 'SHELTERED PEOPLE' : 0.0 , 'EDUCATED PEOPLE' : 0.0 , 'HEALTHY PEOPLE' : 0.0 , 'PEOPLE FED' : 0.0 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.0 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.0 , 'EMPLOYED PEOPLE IN SCHOOL' : 0.0 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.0 , 'EMPLOYED PEOPLE IN FARM' : 0.0 }FOOD_DIST_DICT ={ 'RICE':0.0 , 'WHEAT':0.0 , 'BEANS':0.0 ,'SUGAR': 0.0 ,'SALT' : 0.0 , 'OILS' : 0.0}#with levels increase LEVEL_INCR_PROD = 0.4LEVEL_INCR_CONS = 0.2