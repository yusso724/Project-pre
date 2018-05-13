# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from urllib2 import Request, urlopen, URLError,HTTPError
from selenium.common.exceptions import TimeoutException


class WEIBO:

    def __init__(self):
        pass

    def AWAKE_BROWSER(self):
        self.driver1 = webdriver.Chrome()
        self.driver1.set_page_load_timeout(15)
        self.driver1.implicitly_wait(10)
        time.sleep(3)
        print("======================================================================")
        print("NEW Web Browser is Opened")
        print("======================================================================")

    def LOGIN(self,ID,PASSWD):
        login_flag = 0
        finished = 0
        self.Id = ID
        while finished == 0:
            print("    ======================================================================")
            print("    Try to ACCESS to WEIBO LOGIN Page...")
            try:
                self.driver1.get("https://www.weibo.com/login.php")
                time.sleep(2.5)
                finished = 1
            except HTTPError:
                print("        **ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**")
                print("        HTTP ERROR, RETRYING...")
                print("        **ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**ERROR**")
            except:
                print("        ....RELOADING.... ....RELOADING.... ....RELOADING.... ....RELOADING....")
                print("        ID login, Need to be reloaded, RELOADING...")
                print("        ....RELOADING.... ....RELOADING.... ....RELOADING.... ....RELOADING....")
                time.sleep(5)
            print("    Accessed LOGIN Page!")
            print("    ======================================================================")

            self.driver1.find_element_by_id("loginname").clear()
            self.driver1.find_element_by_id("loginname").send_keys(ID)
            self.driver1.find_element_by_name("password").send_keys(PASSWD)
            self.driver1.find_element_by_css_selector(".W_btn_a.btn_32px").click()

            print "        Waiting for LOGIN Page Loading..."
#            time.sleep(2)
            time.sleep(5)
            if "login" in (self.driver1.current_url):
#                print "        ",self.driver1.current_url
                print("        LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  ")
                print("        Possible LOGIN ERROR.")
                print("        LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  LOGIN Problem ...  ")
                if(login_flag>5):
                    self.driver1.quit()
                    break
                if(login_flag>2):
                    ID = raw_input("PLEASE, input ID : \n")
                    PASSWD = raw_input("PLEASE, input Password : \n")
                login_flag = login_flag + 1 
                finished = 0
        print("    ======================================================================")
        print("    Succeed with LOGIN!")
        print("    **** !! Please Make sure you are successfully logged in !! ****")
        print("    ======================================================================")

    def DATE_MAKER(self,START_YEAR,START_MONTH,START_DAY,INTERVAL=1):
        s_day = START_DAY
        s_month = START_MONTH
        s_year = START_YEAR
        e_day = START_DAY + INTERVAL
        e_month = START_MONTH
        e_year = START_YEAR
        if( (s_day >31 ) & ((START_MONTH ==1) | (START_MONTH ==3) | (START_MONTH ==5) | (START_MONTH ==7) | (START_MONTH ==8) | (START_MONTH ==10) | (START_MONTH ==12))):
            s_day = s_day-31
            s_month = s_month + 1
            if(s_month > 12):
                s_month = s_month - 12
                s_year = s_year + 1
        elif( (s_day >30 ) & ((START_MONTH ==4)|(START_MONTH ==6)|(START_MONTH ==9)|(START_MONTH ==11))):
            s_day = s_day-30
            s_month = s_month + 1
            if(s_month > 12):
                s_month = s_month - 12
                s_year = s_year + 1
        elif( (s_day >29) & ((START_MONTH ==2) & START_YEAR==2016)   ):
            s_day = s_day-29
            s_month = s_month + 1
        elif((s_day >28) & (START_MONTH ==2) ):    
            s_day = s_day-28
            s_month = s_month + 1
        else:
            pass
        if( (e_day >31 ) & ((START_MONTH ==1) | (START_MONTH ==3) | (START_MONTH ==5) | (START_MONTH ==7) | (START_MONTH ==8) | (START_MONTH ==10) | (START_MONTH ==12))):
            e_day = e_day -31
            e_month = e_month + 1
            if(e_month > 12):
                e_month = e_month -12
                e_year = e_year + 1
        elif((e_day >30 ) & ((START_MONTH ==4)|(START_MONTH ==6)|(START_MONTH ==9)|(START_MONTH ==11))):
            e_day = e_day -30
            e_month = e_month + 1
        elif((e_day >29 ) & ((START_MONTH ==2) & START_YEAR==2016)   ):
            e_day = e_day -29
            e_month = e_month + 1
        elif((e_day >28) & (START_MONTH ==2) ):
            e_day = e_day -28
            e_month = e_month + 1
        else:
            pass

        return [s_year, s_month, s_day, e_year, e_month, e_day]

    def MAKE_DATE_STR(self,DATE_LIST_INPUT):
        DATE_LIST = DATE_LIST_INPUT
        str_s_year = str(DATE_LIST[0]); str_e_year = str(DATE_LIST[3]);
        if(DATE_LIST[1] <=9):
            str_s_month = str(0) + str(DATE_LIST[1])
        else:
            str_s_month = str(DATE_LIST[1])
        if(DATE_LIST[2] <=9):
            str_s_day = str(0) + str(DATE_LIST[2])
        else:
            str_s_day = str(DATE_LIST[2])
        if(DATE_LIST[4] <=9):
            str_e_month = str(0) + str(DATE_LIST[4])
        else:
            str_e_month = str(DATE_LIST[4])
        if(DATE_LIST[5] <=9):
            str_e_day = str(0) + str(DATE_LIST[5])
        else:
            str_e_day = str(DATE_LIST[5])
        startDATE = str_s_year + "-" + str_s_month + "-" + str_s_day
        endDATE   = str_e_year + "-" + str_e_month + "-" + str_e_day
        RE_DATE = startDATE + ":" + endDATE
        return RE_DATE


    def MAKE_WEIBO_URL(self, DATE_LIST_INPUT, KEYWORD = "%25E9%259B%25BE%25E9%259C%25BE", LOCAL_NUM=1, PAGE =1):
        DATE = self.MAKE_DATE_STR(DATE_LIST_INPUT)
        Add_str_weibo = "https://s.weibo.com/weibo/"
        Add_some_info = "&region=custom:11:"+ str(LOCAL_NUM) + "&typeall=1&suball=1&timescope=custom:"
        Add_page_info = "&page="
        WEB_PAGE = Add_str_weibo + KEYWORD + Add_some_info + DATE + Add_page_info + str(PAGE)
        self.keyword = KEYWORD
        self.webpage = WEB_PAGE
        return WEB_PAGE



    def ACCESS_URL(self, WEB_PAGE):
        TEMP1 = 0
        finished =0
        print("        ======================================================================")
        print "        ACCESSING Web page: ", self.webpage
        while finished == 0:
            #self.ROBOT()
            try:
                time.sleep(5)
                self.driver1.get(WEB_PAGE)
#                time.sleep(10)
#                print("        Succeed on accessing web page")
                finished = 1
            except:
                print("        Seleninum WebDriver 'get' not returing... I will refresh...")
                time.sleep(5); TEMP1 = TEMP1+1
                if(TEMP1%3==0):
                    try:
                        self.driver1.refresh()
                    except:
                        print("            Refresh Error... let's try 'get' without refresh...")
                if(TEMP1>10):
                    self.ROBOT()
                if(TEMP1 > 15):                    
                    print("            Please REFRESH the web site by your self!!!")
                    CONTINUE = "test"
                    while ((CONTINUE != "c") & (CONTINUE != "C")):
                        CONTINUE = raw_input("[NEED YOUR HELP] - After refresh website by yourself, input 'C' to continue : \n")
        time.sleep(5)

        self.GREP_WORD()
        print("        ======================================================================")
        print("")


    def GREP_WORD(self):
        TEXT_FLAG = 0
        GET_TEXT=0
        print("            ======================================================================")
        print("            Let's EXTRACT number of keyword mention! I will help you get keyword number on this page")
        while GET_TEXT==0:
            #self.ROBOT()
            try:
                time.sleep(5)
                tt1 = self.driver1.find_elements_by_css_selector('.red')
#                self.ROBOT()
                print("            Successfully catched!")
                time.sleep(3)
            except:
                print("                Something went wrong... I will try again to catch.")
                TEXT_FLAG = TEXT_FLAG+1            
                if(TEXT_FLAG>5):
                    self.ROBOT()
                if(TEXT_FLAG>10):
                    self.ACCESS_URL(self.webpage)
        print("WRITE INTO YOUR FILE!")


        print("            ======================================================================") 



    def ROBOT(self):
        ROBOT_FLAG = 0
        ROBOT = 0
        print("                ======================================================================")
        print("                This is ROBOT TEST...")
        while ROBOT == 0:
            try:
#                time.sleep(1)
                tt2 = self.driver1.find_elements_by_css_selector('.code_tit')
#                print(" [NEED YOUR HELP] -  Unfortunately, you need to prove that your are not a ROBOT on Web")
                ROBOT=1
            except:
                print("                RE-test due to driver doesn't responding")
#                time.sleep(3)
                ROBOT_FLAG = ROBOT_FLAG + 1
                if(ROBOT_FLAG>20):
                    print(" [NEED YOUR HELP] -  Please check internet connection...")
 
        if(len(tt2)!=0):
            print(" [NEED YOUR HELP] - 'Prove you are not ROBOT' on Web site *****")
            CONTINUE = 'test'
            while ((CONTINUE != "c") & (CONTINUE != "C")):
                CONTINUE = raw_input("input 'C' to be continue : \n")
#            time.sleep(2)
        print("                END of ROBOT TEST...")
        print("                ======================================================================")

    def QUIT(self):
        print("======================================================================")
        try:
            print "ID : ", self.Id, "Access is closed"
        except:
            print "No login process is closed"
        print("Closing Current Web Browser")
        print("======================================================================")
        print("\n")
        self.driver1.quit()


