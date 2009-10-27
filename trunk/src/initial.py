#! /usr/bin/env python## ***** BEGIN LICENSE BLOCK *****# Version: CPAL 1.0## The contents of this file are subject to the Common Public Attribution# License Version 1.0 (CPAL); you may not use this file except in# compliance with the License. You may obtain a copy of the License at# http://opensource.org/licenses/cpal_1.0## Software distributed under the License is distributed on an "AS IS" basis,# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License# for the specific language governing rights and limitations under the# License.## ***** END LICENSE BLOCK ****## initial values of variables# INITIAL VALUES OF INDICATORSINIT_HOUSING = 0.0INIT_NUTRITION = 0.0INIT_HEALTH = 0.0INIT_TRAINING = 0.0INIT_EDUCATION = 0.0# FACILITIESINIT_HOUSE = 4INIT_HOSPITAL = 2INIT_WORKSHOP = 0INIT_SCHOOL= 0INIT_FARM = 0INIT_FOUNTAIN = 0# MONEYINIT_MONEY = 10000MAX_MONEY=9999999999L## VILLAGE QUANTITY# RESOURCESINIT_WATER = 1000INIT_BUILDMAT = 1000INIT_TOOLS = 1000INIT_MEDICINE = 100INIT_BOOKS = 0# FOOD RESOURCESINIT_RICE = 500INIT_WHEAT = 500INIT_BEANS = 500INIT_SUGAR = 500INIT_SALT = 500INIT_OILS = 500##MARKET QUANTITY# RESOURCESINIT_M_WATER = 10000INIT_M_BUILDMAT = 10000INIT_M_TOOLS = 10000INIT_M_MEDICINE = 2000INIT_M_BOOKS = 2000# FOOD RESOURCESINIT_M_RICE = 2000INIT_M_WHEAT = 2000INIT_M_BEANS = 2000INIT_M_SUGAR = 2000INIT_M_SALT = 2000INIT_M_OILS = 2000# INITIAL COST OF RESOURCES PER UNIT (ASSUMPTION : THE INITIAL COST OF RESOURCES IN MARKET AS WELL AS FOR THE VILLAGE IS SAME)COST_WATER = 15COST_BUILDMAT = 15COST_TOOLS = 15COST_MEDICINE = 10COST_BOOKS = 10COST_RICE = 10COST_WHEAT = 10COST_BEANS = 12COST_SUGAR = 8COST_SALT = 8COST_OILS = 12# BOUNDS ON INDICATORS AND RESOURCES AND FACILITIESMAX_INDICATOR = 100MAX_NO_INS_FACILITY = {'HOUSE':21 , 'HOSPITAL':3 , 'WORKSHOP':4, 'SCHOOL':3, 'FOUNTAIN':7, 'FARM':4} # MAXIMUM NO. OF INSTALLATIONS OF A FACILITYMAX_LEVELS_FACILITY = 3  # MAXIMUM NO OF LEVELS OF A FACILITYLEVEL_INCR_PROD = 0.4LEVEL_INCR_CONS = 0.2MAX_RES_VAL_VILLAGE = 10000MAX_RES_VAL_MARKET = 1000000000LPRICE_VARIATION = 10# INFORMATION REGARDING CLUSTERSVILLAGE_LEVEL = [{ 'HOUSE':8 , 'HOSPITAL':1 , 'WORKSHOP':2, 'SCHOOL':1, 'FOUNTAIN':3, 'FARM':2}, { 'HOUSE':15 , 'HOSPITAL':2 , 'WORKSHOP':3, 'SCHOOL':2, 'FOUNTAIN':5, 'FARM':3}, { 'HOUSE':21 , 'HOSPITAL':3 , 'WORKSHOP':4, 'SCHOOL':3, 'FOUNTAIN':7, 'FARM':4}]# DICTIONARIES REGARDING NUTRITIVE VALUES OF FOOD ( THEY ARE IN % )RICE_NUTRITION = { 'PROTIENS' : 0.30 , 'FATS' : 0.50 , 'VITAMINS' : 0.20 }WHEAT_NUTRITION = { 'PROTIENS' : 0.15 , 'FATS' : 0.70 , 'VITAMINS' : 0.15 }BEANS_NUTRITION = { 'PROTIENS' : 0.40 , 'FATS' : 0.20 , 'VITAMINS' : 0.40 }SUGAR_NUTRITION = { 'PROTIENS' : 0.30 , 'FATS' : 0.55 , 'VITAMINS' : 0.15 }SALT_NUTRITION = { 'PROTIENS' : 0.40 , 'FATS' : 0.10 , 'VITAMINS' : 0.50 }OILS_NUTRITION = { 'PROTIENS' : 0.35 , 'FATS' : 0.20 , 'VITAMINS' : 0.45 }FOOD_DIST_DICT_INIT = {'RICE' : RICE_NUTRITION , 'WHEAT' : WHEAT_NUTRITION , 'BEANS' : BEANS_NUTRITION , 'SUGAR' : SUGAR_NUTRITION , 'SALT' : SALT_NUTRITION , 'OILS' : OILS_NUTRITION }#MANPOWER REGARDING CONSTANTSINIT_PEOPLE = 200.0FOOD_PP= 1MAX_PER_FOOD_CONS = 30