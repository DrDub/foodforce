#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 9/06/2008 
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

import model             
import initial           
import Exceptions        
import facilities        
import indicators         
import threading      
from time import sleep,time,ctime


'''initialization of money '''
money=model.Money()




'''  initialization of facilities   '''
#house
House = model.Facility('HOUSE',facilities.COST_HOUSE,facilities.COST_LEVEL_HOUSE,facilities.PROD_HOUSE,facilities.CONS_HOUSE,0,initial.INIT_HOUSE)
#school
School = model.Facility('SCHOOL',facilities.COST_SCHOOL,facilities.COST_LEVEL_SCHOOL,facilities.PROD_SCHOOL,facilities.CONS_SCHOOL,0,initial.INIT_SCHOOL)
#hospital
Hospital = model.Facility('HOSPITAL',facilities.COST_HOSPITAL,facilities.COST_LEVEL_HOSPITAL,facilities.PROD_HOSPITAL,facilities.CONS_HOSPITAL,0,initial.INIT_HOSPITAL)
#farm
Farm = model.Facility('FARM',facilities.COST_FARM,facilities.COST_LEVEL_FARM,facilities.PROD_FARM,facilities.CONS_FARM,0,initial.INIT_FARM)
#workshop
Workshop = model.Facility('WORKSHOP',facilities.COST_WORKSHOP,facilities.COST_LEVEL_WORKSHOP,facilities.PROD_WORKSHOP,facilities.CONS_WORKSHOP,0,initial.INIT_WORKSHOP)
#fountain
Fountain = model.Facility('FOUNTAIN',facilities.COST_FOUNTAIN,facilities.COST_LEVEL_FOUNTAIN,facilities.PROD_FOUNTAIN,facilities.CONS_FOUNTAIN,0,initial.INIT_FOUNTAIN)








''' initialization of resources   '''
#water
Water=model.Resource('WATER',initial.INIT_WATER,initial.INIT_M_WATER,initial.COST_WATER)
#building material
Buildmat=model.Resource('BUILDING MATERIAL',initial.INIT_BUILDMAT,initial.INIT_M_BUILDMAT,initial.COST_BUILDMAT)
#tools
Tools=model.Resource('TOOLS',initial.INIT_TOOLS,initial.INIT_M_TOOLS,initial.COST_TOOLS)
#medicines
Medicine=model.Resource('MEDICINE',initial.INIT_MEDICINE,initial.INIT_M_MEDICINE,initial.COST_MEDICINE)
#books
Book=model.Resource('BOOKS',initial.INIT_BOOKS,initial.INIT_M_BOOKS,initial.COST_BOOKS)
#rice
Rice=model.Resource('RICE',initial.INIT_RICE,initial.INIT_M_RICE,initial.COST_RICE)
#wheat
Wheat=model.Resource('WHEAT',initial.INIT_WHEAT,initial.INIT_M_WHEAT,initial.COST_WHEAT)
#beans
Beans=model.Resource('BEANS',initial.INIT_BEANS,initial.INIT_M_BEANS,initial.COST_BEANS)
#sugar
Sugar=model.Resource('SUGAR',initial.INIT_SUGAR,initial.INIT_M_SUGAR,initial.COST_SUGAR)
#salt
Salt=model.Resource('SALT',initial.INIT_SALT,initial.INIT_M_SALT,initial.COST_SALT)
#oil
Oil=model.Resource('OILS',initial.INIT_OILS,initial.INIT_M_OILS,initial.COST_OILS)







''' initialization of indicators  '''
#housing
Housing=model.Indicator('HOUSING',initial.INIT_HOUSING,indicators.PDICT_HOUSING)
#health
Health=model.Indicator('HEALTH',initial.INIT_HEALTH,indicators.PDICT_HEALTH)
#education
Education=model.Indicator('EDUCATION',initial.INIT_EDUCATION,indicators.PDICT_EDUCATION)
#nutrition
Nutrition=model.Indicator('NUTRITION',initial.INIT_NUTRITION,indicators.PDICT_NUTRITION)
#training
Training=model.Indicator('TRAINING',initial.INIT_TRAINING,indicators.PDICT_TRAINING)





'''initialisation of manpower resources'''
ppl = model.People(initial.INIT_PEOPLE, 16.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



'''initialisation of lists'''
resources=(Water,Buildmat,Tools,Medicine,Book,Rice,Wheat,Beans,Sugar,Salt,Oil)  # resources list
food_resources=(Rice,Wheat,Beans,Sugar,Salt,Oil)  #food resources list
facilities_list=(House,School,Hospital,Workshop,Farm,Fountain) #facilities list
indicators_list=(Housing,Health,Education,Nutrition,Training) #indicators list


''' Definition of threads'''

def stop_facility(facility_obj):
    ''' Thread to stop a facility it resumes the facility when the village
    has enough resources to run the facility
    '''
    global resources
    facility_obj.stop_facility()
    a=1
    while True:
        a=0
        res_cost = facilities.FACILITY_RES_DICT_CONS[facility_obj.get_name()]
        for i in range(len(resources)):
            name = resources[i].get_name()
            if res_cost.has_key(name):
                if resources[i].get_vquantity() < res_cost[name]:
                    a=1
        if a==0:
            break

    facility_obj.resume_facility()
    print 'Facility : ' , facility_obj.get_name() , ' resumed'







def build_facility(facility_obj):
    ''' Thread to build a new building of any facility
    '''
    global resources
    global ppl
    
    try:
        resources=facility_obj.build_start(resources,ppl)
        
        ppl = facility_obj.update_manp_res(ppl)
        
        if facility_obj.get_level() == 0:
            rs = facility_obj.update_level(resources)
    except Exceptions.Resources_Underflow_Exception:
        print 'you dont have enough resources to build the facility', facility_obj.get_name()
        return 1
    except Exceptions.Low_Manpower_Resources_Exception:
        print 'you dont have enough manpower'
        return 1
    sleep(2)
    print 'drawing first phase of facility-',facility_obj.get_name()
    sleep(2)
    print 'drawing second phase of facility-',facility_obj.get_name()
    sleep(2)
    print 'drawing third phase of facility-',facility_obj.get_name()
    sleep(2)
    print 'drawing fourth phase of facility-',facility_obj.get_name()
    sleep(2)
    
    ppl = facility_obj.build_end(ppl)
    print 'FACILITY MADE', facility_obj.get_name()    












def upgrade_facility(facility_obj):
    ''' Upgrades a facility
    COMMENT : change the view of facility if you want to do so
    '''
    global resources
    try:
        resources = facility_obj.update_level(resources)
    except Exceptions.Resources_Underflow_Exception:
        print 'low resources'
    except Exceptions.Maximum_Level_Reached:
        print 'facility has reached its maximum level you cant upgrade it now'
    sleep(2)
    print 'Updation of facility started',facility_obj.get_name()
    sleep(2)
    print 'FACILITY UPDATED',facility_obj.get_name()








def update_turn():
    ''' Updates the resources, facilities, manpower resources and indicators
    at each turn
    '''
    global resources
    global facilities_list
    global ppl
    global food_resources
    global Housing
    global Nutrition
    global Health
    global Water
    global School

    while(1):
        
        # updation of all facilities
        for i in range(len(facilities_list)):
            try:
                resources = facilities_list[i].turn(resources)
            except Exceptions.Resources_Underflow_Exception:
                print ' you dont have enough resources to run the facility' , facilities_list[i].get_name(), ' it is being stopped temporarily'
                t = threading.Thread(target = stop_facility , args = [facilities_list[i]])
                t.start()
            except Exceptions.Resources_Overflow_Exception:
                pass 




        # updation of manpower resources
                   
        resources = ppl.update_turn(resources,facilities_list)

        # updation of prices of resources
        for i in range(len(resources)):
            resources[i].update_price()





        # updation of indicators

        # housing
        ratio_people_sheltered = ppl.get_no_of_ppl_sheltered()/ppl.get_total_population()
        Housing.turn({'SHELTERED PEOPLE' : ratio_people_sheltered})

        # nutrition
        ppl_fed_ratio = ppl.get_no_of_ppl_fed()/ppl.get_total_population()
        temp = initial.FOOD_DIST_DICT
        protiens = 0
        vitamins = 0
        fats = 0
        for resource in food_resources:
            name = resource.get_name()
            if temp.has_key(name):
                protiens += temp[name]['PROTIENS'] * resource.get_vquantity()
                vitamins += temp[name]['VITAMINS'] * resource.get_vquantity()
                fats += temp[name]['FATS'] * resource.get_vquantity()
            
        
        food = protiens + vitamins + fats
        protiens /= food
        vitamins /= food
        fats /= food

        Nutrition.turn({'PEOPLE FED' : ppl_fed_ratio , 'PROTIENS' : protiens , 'FATS' : fats , 'VITAMINS' : vitamins})

        # health
        healthy_ppl_ratio = ppl.get_no_of_ppl_healthy()/ppl.get_total_population()
        nutrition = Nutrition.get_value()
        nutrition /= initial.MAX_INDICATOR
        water = Water.get_vquantity()/initial.MAX_RES_VAL_VILLAGE

        Health.turn({'HEALTHY PEOPLE' : healthy_ppl_ratio , 'NUTRITION' : nutrition , 'WATER' : water})

        # education
        educated_ppl = ppl.get_no_of_ppl_educated()/ppl.get_total_population()
        level = School.get_level()/initial.MAX_LEVELS_FACILITY
        Education.turn({'EDUCATED PEOPLE' : educated_ppl , 'LEVEL OF EDUCATION' : level })

        # training
        level = Workshop.get_level()/initial.MAX_LEVELS_FACILITY
        ppl_workshop = ppl.get_no_of_ppl_emp_in_workshop()/ppl.get_total_population()
        ppl_farm = ppl.get_no_of_ppl_emp_in_farm()/ppl.get_total_population()    
        ppl_hospital = ppl.get_no_of_ppl_emp_in_hospital()/ppl.get_total_population()
        ppl_construction = ppl.get_no_of_ppl_emp_in_cons()/ppl.get_total_population()
        Training.turn({ 'LEVEL OF WORKSHOPS' : level , 'EMPLOYED PEOPLE IN WORKSHOP' : ppl_workshop , 'EMPLOYED PEOPLE IN FARM' : ppl_farm , 'EMPLOYED PEOPLE IN HOSPITAL' : ppl_hospital , 'EMPLOYED PEOPLE IN CONSTRUCTION' : ppl_construction })

        sleep(15)











    





def buy_res():
    ''' This method allows a user to buy resources
    '''
    global resources
    global money
    
    re_user=raw_input('WHICH RESOURCE DO YOU WANT TO BUY:(enter in uppercase)')
    
    for i in range(len(resources)):
        if resources[i].get_name()==re_user:    
            try:
                print "The initial value of resources with the village is" , resources[i].get_vquantity()
                print "The initial value of resources with the market is" , resources[i].get_mquantity()
                quantity=int(raw_input('ENTER QUANTITY YOU WANT TO PURCHASE'))
                print 'initial money is'
                print money.get_money()
                money = resources[i].buy(quantity , money)
                print 'final money is'
                print money.get_money()
                print "The final value of resources with the village is" , resources[i].get_vquantity()
                print "The final value of resources with the market is" , resources[i].get_mquantity()
            except Exceptions.Money_Underflow_Exception:
                print 'You dont have enough money to buy this resource'
            except Exceptions.Resources_Underflow_Exception:
                print 'The market doesnot have enough quantity to sell this resource to village'
            except Exceptions.Resources_Overflow_Exception:
                print 'resource overflow'
                

    

    


def sell_res():
    ''' This method allows a user to sell resources
    '''
    global resources
    global money
    
    re_user=raw_input('WHICH RESOURCE DO YOU WANT TO SELL:(enter in uppercase)')
    

    for i in range(len(resources)):
        if resources[i].get_name()==re_user:    
            try:
                print "The initial value of resources with the village is" , resources[i].get_vquantity()
                print "The initial value of resources with the market is" , resources[i].get_mquantity()
                quantity=int(raw_input('ENTER QUANTITY YOU WANT TO SELL'))
                money = resources[i].sell(quantity , money)        
                print "The final value of resources with the village is" , resources[i].get_vquantity()
                print "The final value of resources with the market is" , resources[i].get_mquantity()
            except Exceptions.Resources_Underflow_Exception:
                print 'The village doesnot have enough quantity to sell this resource to market'
            except Exceptions.Resources_Overflow_Exception:
                pass




'''
for i in range(len(resources)):
    print 'name : ' , resources[i].get_name()
    print 'value : ' , resources[i].get_vquantity()

resources = Hospital.turn(resources)

for i in range(len(resources)):
    print 'name : ' , resources[i].get_name()
    print 'value : ' , resources[i].get_vquantity()

'''
