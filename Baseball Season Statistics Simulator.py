#Sammy Gray
#February 9, 2021
#This program simulates the season of a major league player
#across 650 plate appearences and uses random numbers (Monte
#Carlo mathod) to determine the outcome of said season based
#on prespecified chances of occurences, such as a pitcher
#throwing a strike and if the batter swings and hits it. It
#then summarizes the player's season by saying his batting
#average, strikeout rate, and walk rate.

import random
import math

if __name__ == "__main__":
    PA = 650
    BB = 0
    H = 0
    K = 0
    ball = 0
    strike = 0
    StopAtBat = False
    
    for i in range(PA):
        
        while StopAtBat == False:
            pitch = random.random()
        
            #pitcher throws a strike 55% of the time
            if pitch <= .55:
                swing = random.random()
                
                #batter does not swing at 20% of strikes
                if swing <= .20:
                    #print('looking strike')
                    strike = strike + 1
                    if strike == 3:
                        K = K + 1
                        ball = 0
                        strike = 0
                        #print('strikeout')
                        break
            
                #batter swings at 70% of strikes       
                else:
                    contact = random.random()
                    #batter makes contact with 80% of swung at pitches
                    if contact <= 80:
                        in_play = random.random()
                        #batter hits it foul 60% of the time
                        if in_play  <=.60:
                            #print('foul')
                            if strike == 2:
                                strike = strike
                            else:
                                strike = strike + 1
                            
                        
                        #batter hits it in play 40% of the time    
                        else:
                            hit = random.random()
                            #batter gets a hit 40% of the time
                            if hit <= .40:
                                H = H + 1
                                ball = 0
                                strike = 0
                                #print('hit')
                                break
                            #batter gets out the other 60% of the time
                            else:
                                ball = 0
                                strike = 0
                                #print('out')
                                break

                
                    #batter misses 25% of swung at pitches    
                    else:
                        strike = strike + 1
                        #print('swinging strike')
                        if strike == 3:
                            K = K + 1
                            ball = 0
                            strike = 0
                            #print('strikeout')
                            break
                    
            #pitcher throws a ball 45% of the time    
            else:
                swing2 = random.random()
            
                #batter swings at 20% of balls
                if swing2 <= .20:
                    strike = strike + 1
                    #print('strike')
                    if strike == 3:
                        K = K + 1
                        ball = 0
                        strike = 0
                        #print('strikeout')
                        break
                
                #batter does not swing at the other 80% of balls    
                else:
                    ball = ball + 1
                    #print('ball')
                    if ball == 4:
                        BB = BB + 1
                        ball = 0
                        strike = 0
                        #print('walk')
                        break

BA = H/(PA - BB)
SOP = (K/PA) * 100
BBP = (BB/PA) * 100 

print('Batting Average:',round(BA, 3))
print('Strikeout Rate:',round(SOP,(2)),'%')
print('Walk Rate',round(BBP,(2)),'%')