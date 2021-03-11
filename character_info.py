import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

################################################################################################
################################################################################################


def get_character_dictionary():
    """어벤져스 시리즈에 등장하는 인물 사전"""

    name_dict = {}
    characters = ['SHURI', 'EITRI', 'KORG', 'WEASELY THUG', 'SHIELD AGENT',
       'EDWIN JARVIS', 'BRUCE BANNER', 'HAPPY', 'HOWARD STARK',
       "GAMORA'S MOTHER", 'DOCTOR STRANGE', 'HANK PYM',
        'RUMLOW (2012)', 'NICK FURY',
       'GENERAL LUCHKOV', 'SAM WILSON', 'VALKYRIE', 'THANOS',
       'SPECIALIST CAMERON KLEIN', 'JAMES RHODES',
       'HYDRA AGENT', 'ULTRON', "T'CHALLA", 'JASPER SITWELL',
       'ULYSSES KLAUE',
       'TONY STARK', 'LILA BARTON', 'COLLECTOR',
       'HELMSMAN', 'GAMORA', 'JARVIS', 'JABARI WARRIORS', "M'BAKU",
       'LOKI', 'MADAME B', 'OKOYE', 'GROOT', 'CHILD OF THANOS', 'ZRINKA',
       'CAROL DANVERS', 'NATASHA ROMANOFF', 'VISION', 'STEVE ROGERS',
       'CLINT BARTON', 'EBONY MAW', 'PEGGY CARTER', 'ALEXANDER PIERCE',
       'FRIGGA', 'YOUNG COP', 'GEORGI LUCHKOV',
       'PEPPER POTTS', 'SECURITY GUARD',
       'SENATOR BOYNTON', 'HOPE VAN DYNE',
       'PETER QUILL', 'THE WASP', 'WANDA MAXIMOFF',
       'DR. HELEN CHO', 'PIETRO MAXIMOFF', 'CORVUS GLAIVE', 'JOE RUSSO',
       'OLD MAN', 'SCOTT LANG', 'ROCKET', 'NATHANIEL BARTON',
       'CULL OBSIDIAN', 'THE ANCIENT ONE',
       'RED SKULL', 'NEBULA', 'CASSIE LANG', 'PROXIMA MIDNIGHT', 'MANTIS',
       'LAURA BARTON', 'THOR', 'COULSON', 'NED LEEDS',
       'DR. LIST', 'FRIDAY', 'BUCKY BARNES',
       'POLICE SERGEANT', 'DRAX',
       "KLAUE'S MERCENARY", 'STAN LEE', 'SECRETARY ROSS',
       'ATTENDING WOMAN', 'JIM STARLIN', 'MORGAN STARK',
       'IRON LEGION', 'PETER PARKER', 'BRUCE ROGERS',
       'HEIMDALL', 'MARIA HILL', 'RONIN', 'WONG', 'COOPER BARTON',
       'ERIK SELVIG', 'STRUCKER', 'STONEKEEPER']

    for ele in characters:
        name_dict[ele] = ele

    return name_dict

name_dict = get_character_dictionary()


################################################################################################
################################################################################################
# 위키피디아 설명 크롤링

# 사이트 접속
PATH = "/Users/dongwook/chromedriver"
driver = webdriver.Chrome(PATH)
URL = "https://www.google.com"
driver.get(URL)
time.sleep(1.5)

info_dict = {}

search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys("dsa")
search.send_keys(Keys.ENTER)
time.sleep(3)

for character in name_dict.keys():
    try:
        # 검색창에 검색어 입력
        search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').clear()
        time.sleep(4)
        search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
        search.send_keys("marvel " + character)
        search.send_keys(Keys.ENTER)
        time.sleep(4)

        # 인물정보 저장
        info = driver.find_element_by_class_name("kno-rdesc")
        description = info.text.replace("위키백과", "")
        info_dict[character] = description

        print(character)
        print(description)
        print()
        time.sleep(4)

    except:
        info_dict[character] = "-"
        print(character)
        print("-")
        print()


################################################################################################
################################################################################################
# 사전 저장
with open('info_dict.json', 'w') as fp:
    json.dump(info_dict, fp)