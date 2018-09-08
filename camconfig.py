#SET CONFIG AYARLARI

#Parameters
'''  #5MP4:3(W) 8MP16:9(W) 12MP16:9(16M4:3 olarak algiliyor) 16MP 4:3
'100':['Photo_Image_Size', '12M_4032x3024', '10M_3648x2736', '8M_3264x2448', '5M_2592x1944', '3M_2048x1536', '2MHD_1920x1080', 'VGA_640x480', '1.3M_1280x960'],
	       	       #'1006':['Sharpness', 'Strong', 'Normal', 'Soft'],
		       #'1007':['White_Balance', 'Auto', 'Daylight', 'Cloudy', 'Tungsten', 'Flourescent'],
		       #'1008':['Colour', 'Colour', 'B/W', 'Sepia','],
		       #'1009':['ISO', 'Auto', '100', '200', '400'],
		       #'1011':['Anti_Shaking', 'Off', 'On'],
			'2002':['Movie_Resolution', '1080FHD_1920x1080', '720P_1280x720_60fps', '720P_1280x720_30fps', 'WVGA_848x480', 'VGA_640x480'],
			'2003':['Cyclic_Record', 'Off', '3_Minutes', '5_Minutes', '10_Minutes'],
			'2004':['HDR/WDR', 'Off', 'On'],
		       #'2005':['EV', '+2.0', '+5/3', '+4/3', '+1.0', '+2/3', '+1/3', '+0.0', '-1/3', '-2/3', '-1.0', '-4/3', '-5/3', '-2.0'],
			'2006':['Motion_Detection', 'Off', 'On'],
			'2007':['Audio', 'Off', 'On'],
			'2008':['Date_Stamping', 'Off', 'On'],
			'2019':['Videolapse','Off', '1_Second', '2_Seconds', '5_Seconds', '10_Seconds', '30_Seconds', '1_Minute'],
			'3007':['Auto_Power_Off', 'Off', '3_Minutes', '5_Minutes', '10_Minutes'],
			'3008':['Language', 'English', 'French', 'Spanish', 'Polish', 'German', 'Italian', 'Unknown_1', 'Unknown_2', 'Russian', 'Unknown_3', 'Unknown_4', 'Unknown_5', 'Portugese'],
			'3010':['Format', 'Cancel', 'OK'],
			'3011':['Default_Setting', 'Cancel', 'OK'],
			'3025':['Frequency', '50Hz', '60Hz'],
			'3026':['Rotate', 'Off', 'On'],


			NOTES: 3M_2048x1536 4:3 Working
			       5M_2592x1944 4:3 Working
			       8M_3264x2448 16:9 Working
			       10M_3648x2736 12MP 16:9 olarak algiliyor
			       12M_4032x3024 16MP 4:3 olarak algiliyor
			    

'''
#Methods

'get_config_by_name(config)  '                      #returns the value of the given conf. ex: get_config_by_name("Photo_Image_Size) returns 1002
'get_disk_space()                   '               #Remaining space Returns true,int
'get_element(response,element)      '               #extract a single element from response to 'send_command' ***Returns a text file???****
'get_file(path,file)                '               #download file(can be used combined with snap) Returns TRUE & Filename 
'get_file_details(cells,filename)   '               #????
'get_mode()                         '               #????
'get_preview()                      '               #Returning random numbers.
'http_test ()                       '               #returns 'HTTP socket CLOSED' or "HTTP socket OPEN"
'human_readable                     '               #???
'ping ()                            '               #Ping self returns 'Host is UP' or 'Host is DOWN'
'print_config_help(parameter)       '               #Prints the green info panel up there 
'print_config()                       '             #config
'print_directory(quiet= False,'                     #find= None) Returns filesize ????
'send_command (command, param= None, str_param= None)' #
'set_config(set_config(self, param, val)'           #Chose Parameter and its Value to set config 
'set_date(date)  '                                  #Sets Date <YYYY-MM-DD>
'set_mode(mode) '                                   #Enter Video or Photo to switch mote
'set_time(time) '                                   #Sets Time of the cam
'set_wifi_name(ssid)'                               #Wifi SSID  ps:somehow it connects to the manuel given network(NEEDS NIRE TESTING)
'set_wifi_pw(pw)'                                   #Wifi Pass
'snap(path)'                                        #Snap and Download to the given path 
'start_stop_movie(action)'                          #NOT WORKING
'stream'                                            #NOT WORKING


import sj4000 
from bs4 import BeautifulSoup
camera=sj4000.camera()

#camera.set_wifi_name("HisseliHarikalar") #SWITCHES ONLY CONNECT AND DISCONNECT)
#camera.set_wifi_pw("hhf-sormagir")          


ret=camera.http_test()  #HttpTEst return 'HTTP socket CLOSED' or 'HTTP socket OPEN'
print("HTTP")
print(ret)


if ret== 'HTTP socket OPEN': 


    camera.get_config_by_name("Photo_Image_Size")
    ret,info=camera.get_disk_space()   # True or False & Space(int)
    print("DISK SPACE")
    print(ret)
    print(info)

    ret,info=camera.set_mode("PHOTO") #VIDEO or PHOTO 
    print("PHOTOMODE")
    print(ret)                          
    print(info)

    ret, info=camera.set_config("AUDIO", "OFF")#AUDIO ON OFF
    print("AUDIO")
    print(ret)
    print(info)

    ret, info=camera.set_config("Photo_Image_Size", "8M_3264x2448") #Minimum is 3M_2048x1536 
    #This part of the code can be deleted and photosize can manually setted.
    print("IMAGESIZE")
    print(ret)
    print(info)
    ret, info=camera.set_config("EV", "2")
    print("WHITE BALANCE")
    print(ret)
    print(info)


    info1, info2=camera.print_config()
    print("info1 conf")
    print(info1)
    print("info2 conf")
    print(info2)


    ret,info=camera.snap("/home/pi/sjcam/") #INPUT LOCATION DIRECTORY
    print("SNAP")                           #RETURN TRUE OR FALSE & PHOTO NAME
    print(ret)                              #SIZE?
    print(info)
   
    camera.print_config()
    #ret,info=camera.set_config("FORMAT","OK")   #WIPE SD CARD 
    print("FORMAT")
    print(ret)
    print(info)



    

