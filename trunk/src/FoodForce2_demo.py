import pygame
from pygame.locals import *
from sys import exit
import threading
from time import sleep,time,ctime
from threades import *

pygame.init()
SCREEN_SIZE = (1240, 840)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 40);
font_height = font.get_linesize()


while True:
       
    event_text = []
    event = pygame.event.wait()        
    event_text.append(' MENU :')
    event_text.append('1.) Build Facility')
    event_text.append('2.) Upgrade Facility')
    event_text.append('3.) Buy Resources')
    event_text.append('4.) Sell Resources')
    event_text.append('5.) Display Values')
    event_text.append('Enter the appropriate value for your choice')
    
    event_text = event_text[-SCREEN_SIZE[1]/font_height:]
    y = (SCREEN_SIZE[1]-font_height)/2
    for text in reversed(event_text):        
        screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
        y-=font_height
        
    pygame.display.update()

    event = pygame.event.wait()    
    update_thread = threading.Thread(target = update_turn, args=[]).start()

    if event.type == QUIT:
        exit()
    
    if event.type == KEYDOWN:

        if event.unicode == u'1':
            
                        
            while True:
                
                screen.fill((0, 0, 0))
                event_text = []
                event_text.append('BUILD FACILITY :')
                event_text.append('1.) House')
                event_text.append('2.) School')
                event_text.append('3.) Hospital')
                event_text.append('4.) Farm')
                event_text.append('5.) Workshop')
                event_text.append('6.) Fountain')
                event_text.append('7.) Back to previous menu')
                event_text.append('Enter the appropriate value for your choice')
                event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                y = (SCREEN_SIZE[1]-font_height)/2
                for text in reversed(event_text):        
                    screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                    y-=font_height
        
                pygame.display.update()

                event = pygame.event.wait()

                if event.type == QUIT:
                    exit()
    
                if event.type == KEYDOWN:

                    if event.unicode == u'7':
                        break

                    if event.unicode == u'1':
                        t = threading.Thread(target = build_facility, args=[House])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY BUILDING STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()

                    if event.unicode == u'2':
                        t = threading.Thread(target = build_facility, args=[School])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY BUILDING STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'3':
                        t = threading.Thread(target = build_facility, args=[Hospital])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY BUILDING STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'4':
                        t = threading.Thread(target = build_facility, args=[Farm])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY BUILDING STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'5':
                        t = threading.Thread(target = build_facility, args=[Workshop])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY BUILDING STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'6':
                        t = threading.Thread(target = build_facility, args=[Fountain])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY BUILDING STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()

                    sleep(3)




        if event.unicode == u'2':
            
            while True:
                screen.fill((0, 0, 0))
                event_text = []
                event_text.append('UPGRADE FACILITY :')
                event_text.append('1.) House')
                event_text.append('2.) School')
                event_text.append('3.) Hospital')
                event_text.append('4.) Farm')
                event_text.append('5.) Workshop')
                event_text.append('6.) Fountain')
                event_text.append('7.) Back to previous menu')
                event_text.append('Enter the appropriate value for your choice')
                event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                y = (SCREEN_SIZE[1]-font_height)/2
                for text in reversed(event_text):        
                    screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                    y-=font_height
        
                pygame.display.update()

                event = pygame.event.wait()

                if event.type == QUIT:
                    exit()
    
                if event.type == KEYDOWN:

                    if event.unicode == u'7':
                        break

                    if event.unicode == u'1':
                        t = threading.Thread(target = upgrade_facility, args=[House])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY UPGRADATION STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()

                    if event.unicode == u'2':
                        t = threading.Thread(target = upgrade_facility, args=[School])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY UPGRADATION STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'3':
                        t = threading.Thread(target = upgrade_facility, args=[Hospital])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY UPGRADATION STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'4':
                        t = threading.Thread(target = upgrade_facility, args=[Farm])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY UPGRADATION STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'5':
                        t = threading.Thread(target = upgrade_facility, args=[Workshop])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY UPGRADATION STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()


                    if event.unicode == u'6':
                        t = threading.Thread(target = upgrade_facility, args=[Fountain])
                        t.start()
                        screen.fill((0, 0, 0))
                        event_text.append('FACILITY UPGRADATION STARTED CHECK TERMINAL')
                        event_text.append('OR INTERPRETER FOR CURRENT STATUS :')
                        event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                        y = (SCREEN_SIZE[1]-font_height)/2
                        for text in reversed(event_text):        
                            screen.blit( font.render(text, True, (0, 255, 0)), (420, y) )
                            y-=font_height
        
                        pygame.display.update()

                    sleep(3)



        if event.unicode == u'3':
            random = 0
            while True:
                screen.fill((0, 0, 0))
                event_text = []
                event_text.append('BUY FUNCTION:')
                event_text.append('Please go to the terminal or interpreter to')
                event_text.append('enter the name of the resource you want to buy')
                event_text.append('You can buy any of the following resources')
                event_text.append('1.) BUILDING MATERIAL')
                event_text.append('2.) WATER')
                event_text.append('3.) TOOLS')
                event_text.append('4.) MEDICINE')
                event_text.append('5.) BOOKS')
                event_text.append('6.) RICE')
                event_text.append('7.) WHEAT')
                event_text.append('8.) BEANS')
                event_text.append('9.) SUGAR')
                event_text.append('10.) SALT')
                event_text.append('11.) OILS')
                event_text.append('Please enter the name of the Resource in Capitals')
                event_text.append('PRESS 0 TO GO BACK TO PREVIOUS MENU')

                event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                y = (SCREEN_SIZE[1]-font_height)/2
                for text in reversed(event_text):        
                    screen.blit( font.render(text, True, (0, 255, 0)), (420, y+300 ) )
                    y-=font_height
        
                pygame.display.update()
                if random == 0:
                    t = threading.Thread(target = buy_res, args=[]).start()
                    random = 1

                event = pygame.event.wait()

                if event.type == QUIT:
                    exit()
    
                if event.type == KEYDOWN:

                    if event.unicode == u'0':
                        break





        if event.unicode == u'4':
            
            random = 0
            while True:
                screen.fill((0, 0, 0))
                event_text = []
                event_text.append('SELL FUNCTION:')
                event_text.append('Please go to the terminal or interpreter to')
                event_text.append('enter the name of the resource you want to buy')
                event_text.append('You can sell any of the following resources')
                event_text.append('1.) BUILDING MATERIAL')
                event_text.append('2.) WATER')
                event_text.append('3.) TOOLS')
                event_text.append('4.) MEDICINE')
                event_text.append('5.) BOOKS')
                event_text.append('6.) RICE')
                event_text.append('7.) WHEAT')
                event_text.append('8.) BEANS')
                event_text.append('9.) SUGAR')
                event_text.append('10.) SALT')
                event_text.append('11.) OILS')
                event_text.append('Please enter the name of the Resource in Capitals')
                event_text.append('PRESS 0 TO GO BACK TO PREVIOUS MENU')

                event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                y = (SCREEN_SIZE[1]-font_height)/2
                for text in reversed(event_text):        
                    screen.blit( font.render(text, True, (0, 255, 0)), (420, y+300 ) )
                    y-=font_height
        
                pygame.display.update()
                
                if random == 0:
                    t = threading.Thread(target = sell_res, args=[]).start()
                    random = 1

                event = pygame.event.wait()

                if event.type == QUIT:
                    exit()
    
                if event.type == KEYDOWN:

                    if event.unicode == u'0':
                        break


                        
        if event.unicode == u'5':

            while True:
                screen.fill((0,0,0))
                event_text = []
                event_text.append('DISPLAY VALUES:')
                event_text.append('')
                event_text.append('1.) Resources')
                event_text.append('2.) Facilities')
                event_text.append('3.) Indicators')
                event_text.append('4.) Money')
                event_text.append('5.) Manpower Distribution')
                event_text.append('6.) Back to previous menu')

                event_text = event_text[-SCREEN_SIZE[1]/font_height:]
                y = (SCREEN_SIZE[1]-font_height)/2
                for text in reversed(event_text):        
                    screen.blit( font.render(text, True, (0, 255, 0)), (420, y+100 ) )
                    y-=font_height

                pygame.display.update()

                event = pygame.event.wait()

                if event.type == QUIT:
                    exit()

                if event.type == KEYDOWN:

                    if event.unicode == u'6':
                        break

                    if event.unicode == u'1':

                        while True:
                            font2 = pygame.font.SysFont("arial", 30);
                            font2_height = font2.get_linesize()
                            screen.fill((0,0,0))
                            event_text = []
                            event_text.append('RESOURCES')
                            event_text.append('')
                            event_text.append('')
                            event_text.append('')
                            event_text.append('')
                            event_text.append('')
                            for i in range(5):
                                event_text.append('NAME : ' + resources[i].get_name())
                                event_text.append('MARKET QUANTITY : ' + str(int(resources[i].get_mquantity())) )
                                event_text.append('VILLAGE QUANTITY : ' + str(int(resources[i].get_vquantity())) )
                                event_text.append('PRICE : ' + str(int(resources[i].get_price())) )
                                event_text.append('')
                                

                            event_text.append('')
                            event_text.append('')
                            event_text.append('')
                            event_text.append('')
                            event_text.append(' Press 0 to go to the previous menu')

                            event_text = event_text[-(SCREEN_SIZE[1])/font2_height:]
                            y = (SCREEN_SIZE[1]-font2_height)
                            for text in reversed(event_text):        
                                screen.blit( font2.render(text, True, (0, 255, 0)), (0, y ) )
                                y-=font2_height

                            pygame.display.update()

                            event_text = []
                            for i in range(6):
                                
                                event_text.append('NAME : ' + resources[5+i].get_name())
                                event_text.append('MARKET QUANTITY : ' + str(int(resources[5+i].get_mquantity())) )
                                event_text.append('VILLAGE QUANTITY : ' + str(int(resources[5+i].get_vquantity())) )
                                event_text.append('PRICE : ' + str(int(resources[5+i].get_price())) )
                                event_text.append('')
                                

                        
                            
                            event_text = event_text[-SCREEN_SIZE[1]/font2_height:]
                            y = (SCREEN_SIZE[1]-font2_height)
                            for text in reversed(event_text):        
                                screen.blit( font2.render(text, True, (0, 255, 0)), (600, y ) )
                                y-=font2_height

                            pygame.display.update()

                            event = pygame.event.wait()

                            if event.type == QUIT:
                                exit()

                            if event.type == KEYDOWN:
                                if event.unicode == u'0':
                                    break


                    if event.unicode == u'2':
                        
                        while True:
                            font2 = pygame.font.SysFont("arial", 30);
                            font2_height = font2.get_linesize()
                            screen.fill((0,0,0))
                            event_text = []
                            event_text.append('FACILITIES')
                            event_text.append('')
                            event_text.append('')
                            for i in range(len(facilities_list)):
                                event_text.append('NAME : ' + facilities_list[i].get_name())
                                event_text.append('NUMBER OF INSTALLATIONS : ' + str(int(facilities_list[i].get_number())) )
                                event_text.append('LEVEL : ' + str(int(facilities_list[i].get_level())) )
                                event_text.append('')
                                event_text.append('')

                        
                            event_text.append(' Press 0 to go to the previous menu')

                            event_text = event_text[-SCREEN_SIZE[1]/font2_height:]
                            y = (SCREEN_SIZE[1]-font2_height)
                            for text in reversed(event_text):        
                                screen.blit( font2.render(text, True, (0, 255, 0)), (400, y ) )
                                y-=font2_height

                            pygame.display.update()
 
                        
                            event = pygame.event.wait()

                            if event.type == QUIT:
                                exit()

                            if event.type == KEYDOWN:
                                if event.unicode == u'0':
                                    break




                    if event.unicode == u'3':

                        while True:
                            
                            font2 = pygame.font.SysFont("arial", 30);
                            font2_height = font2.get_linesize()
                            screen.fill((0,0,0))
                            event_text = []
                            event_text.append('INDICATORS')
                            event_text.append('')
                            event_text.append('')
                            for i in range(len(indicators_list)):
                                event_text.append('NAME : ' + indicators_list[i].get_name())
                                event_text.append('VALUE OF INDICATOR : ' + str(int(indicators_list[i].get_value())) )
                                event_text.append('')
                                event_text.append('')

                        
                            event_text.append(' Press 0 to go to the previous menu')
   
                            event_text = event_text[-SCREEN_SIZE[1]/font2_height:]
                            y = (SCREEN_SIZE[1]-font2_height)
                            for text in reversed(event_text):        
                                screen.blit( font2.render(text, True, (0, 255, 0)), (400, y ) )
                                y-=font2_height

                            pygame.display.update()
 
                        
                            event = pygame.event.wait()

                            if event.type == QUIT:
                                exit()

                            if event.type == KEYDOWN:
                                if event.unicode == u'0':
                                    break

                        
                        
                    if event.unicode == u'4':

                        while True:
                            
                            font2 = pygame.font.SysFont("arial", 50);
                            font2_height = font2.get_linesize()
                            screen.fill((0,0,0))
                            event_text = []
                            event_text.append('MONEY')
                            event_text.append('')
                            event_text.append('')
                            event_text.append(' MONEY WITH THE VILLAGE IS :  ' + str(int(money.get_money())))
                            event_text.append('')
                            event_text.append('')
                            event_text.append(' Press 0 to go to the previous menu')
   
                            event_text = event_text[-SCREEN_SIZE[1]/font2_height:]
                            y = (SCREEN_SIZE[1]-font2_height)/2
                            for text in reversed(event_text):        
                                screen.blit( font2.render(text, True, (0, 255, 0)), (400, y + 100 ) )
                                y-=font2_height

                            pygame.display.update()
 
                        
                            event = pygame.event.wait()

                            if event.type == QUIT:
                                exit()

                            if event.type == KEYDOWN:
                                if event.unicode == u'0':
                                    break

                    if event.unicode == u'5':

                        while True:
                            
                            font2 = pygame.font.SysFont("arial", 30);
                            font2_height = font2.get_linesize()
                            screen.fill((0,0,0))
                            event_text = []
                            event_text.append(' MANPOWER RESOURCES')
                            event_text.append('')
                            event_text.append(' TOTAL POPULATION : ' + str(int(ppl.get_total_population())))
                            event_text.append('')
                            event_text.append(' Total number of people fed : ' + str(int(ppl.get_no_of_ppl_fed())))
                            event_text.append('')
                            event_text.append(' Total number of people sheltered : ' + str(int(ppl.get_no_of_ppl_sheltered())))
                            event_text.append('')
                            event_text.append(' Total number of people educated : ' + str(int(ppl.get_no_of_ppl_educated())))
                            event_text.append('')
                            event_text.append(' Total number of people healthy : ' + str(int(ppl.get_no_of_ppl_healthy())))
                            event_text.append('')
                            event_text.append(' People employed in construction : ' + str(int(ppl.get_no_of_ppl_emp_in_cons())))
                            event_text.append('')
                            event_text.append(' People employed in hospitals : ' + str(int(ppl.get_no_of_ppl_emp_in_hospital())))
                            event_text.append('')
                            event_text.append(' People employed in schools : ' + str(int(ppl.get_no_of_ppl_emp_in_school())))
                            event_text.append('')
                            event_text.append(' People employed in workshops : ' + str(int(ppl.get_no_of_ppl_emp_in_workshop())))
                            event_text.append('')
                            event_text.append(' People employed in farm : ' + str(int(ppl.get_no_of_ppl_emp_in_farm())))
                            event_text.append('')
                            event_text.append(' Total number of people employed : ' + str(int(ppl.get_total_no_of_ppl_emp())))
                            event_text.append('')
                            event_text.append(' Total number of people unemployed : ' + str(int(ppl.get_total_no_of_ppl_un_emp())))
                            event_text.append('')
                            event_text.append(' Press 0 to go to the previous menu')
   
                            event_text = event_text[-SCREEN_SIZE[1]/font2_height:]
                            y = (SCREEN_SIZE[1]-font2_height)
                            for text in reversed(event_text):        
                                screen.blit( font2.render(text, True, (0, 255, 0)), (100, y ) )
                                y-=font2_height

                            pygame.display.update()
 
                        
                            event = pygame.event.wait()

                            if event.type == QUIT:
                                exit()

                            if event.type == KEYDOWN:
                                if event.unicode == u'0':
                                    break

                                           

                

    screen.fill((0, 0, 0))
    
    