import pandas as pd
import numpy as np
import difflib
import time
import json
import networkx as nx
import matplotlib.pyplot as plt
plt.interactive(False)

##########################################################################################
##########################################################################################

class Utils:
    """static class for utils used in the analysis"""

    @staticmethod
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

        name_dict["ROCKET RACCOON"] = "ROCKET"
        name_dict["RACCOON"] = "ROCKET"
        name_dict["WAR MACHINE"] = "JAMES RHODES"
        name_dict["CAPTAIN MARVEL"] = 'CAROL DANVERS'
        name_dict["SITWELL"] = 'JASPER SITWELL'
        name_dict["PHIL COULSON"] = "COULSON"
        name_dict["BARTON"] = "HAWKEYE"
        name_dict["CLINT"] = "CLINT BARTON"
        name_dict["HAWKEYE"] = "CLINT BARTON"
        name_dict["BANNER"] = "BRUCE BANNER"
        name_dict["HULK"] = "BRUCE BANNER"
        name_dict["NATASHA"] = "NATASHA ROMANOFF"
        name_dict["BLACK WIDOW"] = "NATASHA ROMANOFF"
        name_dict["STEVE"] = "STEVE ROGERS"
        name_dict["CAPTAIN AMERICA"] = "STEVE ROGERS"
        name_dict["SELVIG"] = "ERIK SELVIG"
        name_dict["FURY"] = "NICK FURY"
        name_dict["TONY"] = "TONY STARK"
        name_dict["IRON MAN"] = "TONY STARK"
        name_dict["FALCON"] = "SAM WILSON"
        name_dict["BLACK PANTHER"] = "T'CHALLA"
        name_dict["SPIDERMAN"] = "PETER PARKER"
        name_dict["STAR LORD"] = "PETER QUILL"
        name_dict["STAR-LORD"] = "PETER QUILL"
        name_dict["STEPHEN STRANGE"] = "DOCTOR STRANGE"
        name_dict["STRANGE"] = "DOCTOR STRANGE"
        name_dict["DR.STRANGE"] = "DOCTOR STRANGE"
        name_dict["WINTER SOLDIER"] = "BUCKY BARNES"
        name_dict["ANTMAN"] = "SCOTT LANG"
        name_dict["HILL"] = "MARIA HILL"

        return name_dict


    @staticmethod
    def name_check(name):
        """캐릭터명이 정확한지 체크 및 반환"""

        name_dict = Utils.get_character_dictionary()

        if name.upper() in name_dict.keys():
            return name_dict[name.upper()]
        else:
            # 단순 오타일 경우 캐릭터명 추천
            suggestion = []
            for ele2 in name_dict.keys():
                similarity = difflib.SequenceMatcher(None, name.upper(), ele2).ratio()
                if similarity > 0.5:
                    suggestion.append(ele2)

            print("존재하지 않는 캐릭터입니다.")
            print("혹시 이 캐릭터가 아닌가요?: {}".format(suggestion))
            print()
            return "unmatch"


    @staticmethod
    def get_edge_df():
        path = ["avengers1.csv", "avengers2.csv", "avengers3.csv", "avengers4.csv"]
        edges = pd.DataFrame()
        for ele in path:
            df = pd.read_csv(ele)
            edges = pd.concat([edges, df])

        return edges


    @staticmethod
    def Loading():
        """로딩"""
        print("조회중입니다", end='')

        for i in range(3):
            time.sleep(0.5)
            print(".", end='')
        print()
        print()


    @staticmethod
    def Borderline():
        """줄바꿈"""
        print()
        print(
            "##########################################################################################\n##########################################################################################")


    @staticmethod
    def degree_centrality(graph):
        """ 그래프에서 노드별 degree centrality를 계산하는 함수

        Returns
        ----------
        list
            내림차순 정렬된 노드별 degree centrality
        """
        return sorted(nx.degree_centrality(graph).items(), key=lambda x: x[1], reverse=True)


    @staticmethod
    def pagerank(graph):
        """ 그래프에서 노드별 pagerank를 계산하는 함수

        Returns
        ----------
        list
            내림차순 정렬된 노드별 pagerank
        """
        return sorted(nx.pagerank_numpy(graph, weight='weight').items(), key=lambda x: x[1], reverse=True)


    @staticmethod
    def get_importance_df(graphs):
        # 중요도 데이터프레임 정의
        importance = [dict(Utils.pagerank(graph)) for graph in graphs]
        importance_df = pd.DataFrame.from_records(importance).fillna(0)
        return importance_df

##########################################################################################
##########################################################################################

class Analysis_byCharacter(Utils):
    """인물별 네트워크 분석 자료"""

    def __init__(self, character):
        self.character = character
        with open("info_dict.json", "r") as fb:
            self.info_dict = json.load(fb)
        self.edges = self.get_edge_df()
        self.graphs = [nx.from_pandas_edgelist(self.edges[self.edges.series == i],
                                               source='Source', target='Target',  edge_attr=['weight']) for i in range(1, 5)]

    def character_interactions(self, series_no: int):
        """분석1: 특정 시리즈에서 한 캐릭터가 다른 캐릭터들과 상호작용한 횟수

        Returns
        ----------
        DataFrame
            상호작용한 횟수 (weight)
        """
        filter1 = (self.edges.series == series_no)
        filter2 = (self.edges.Source == self.character) | (self.edges.Target == self.character)

        df = self.edges[filter1 & filter2]

        if len(df) == 0:
            print("해당 인물은 어벤져스 {}에 등장하지 않았습니다.".format(series_no))
        else:
            print(df)



    def character_importance_change(self):
        # 분석2: 특정 캐릭터의 중요도 변화
        importance_df = self.get_importance_df(self.graphs)

        for i, row in importance_df.iterrows():
            row = row[row > 0]
            if sum(row.sort_values(ascending=False).index == self.character) == 0:
                total = len(row.sort_values(ascending=False).index)
                print("어벤져스 {}에서 {}의 중요도: [0/{}] (등장 X)".format(i + 1, self.character, total))
            else:
                ranking = (row.sort_values(ascending=False).index == self.character).argmax() + 1
                total = len(row.sort_values(ascending=False).index)
                print("어벤져스 {}에서 {}의 중요도: [{}/{}]".format(i+1, self.character, ranking, total))
        #importance_df[[self.character]].plot(kind="bar", figsize=(9, 7))
        #plt.show()


    def script(self):

        Utils.Loading()
        Utils.Borderline()
        print("선택하신 등장 인물은 [{}] 입니다.\n".format(self.character))

        choice = 0
        while choice != 4:
            print("어떤 것을 확인하시겠습니까?\n")
            print("1. 인물 기본 정보")
            print("2. 다른 인물들과의 상호작용")
            print("3. 인물의 중요도 변화")
            print("4. 뒤로가기")
            try:
                choice = int(input(":"))
            except:
                choice = int(input(":"))

            if choice == 1:
                Utils.Borderline()
                print(self.info_dict[self.character])
                print()
                input("아무키나 누르세요.")
                Utils.Borderline()

            elif choice == 2:
                Utils.Borderline()
                series = int(input("기준이 되는 어벤져스 시리즈를 입력하세요 (1~4)\n"))
                df = self.character_interactions(series)
                print(df)
                print()
                input("아무키나 누르세요.")
                Utils.Borderline()

            elif choice == 3:
                Utils.Borderline()
                self.character_importance_change()
                print()
                input("아무키나 누르세요.")
                Utils.Borderline()


            elif choice == 4:
                pass

            else:
                print("잘못된 입력입니다.")






################################################################################################
################################################################################################

class Analysis_bySeries(Utils):
    """각 시리즈별 네트워크 분석 자료"""

    def __init__(self, series_no):
        self.series_no = series_no
        self.edges = self.get_edge_df()
        self.graphs = [nx.from_pandas_edgelist(self.edges[self.edges.series == i],
                                               source='Source', target='Target',  edge_attr=['weight']) for i in range(1, 5)]
        if self.series_no == "1":
            self.series_name = "어벤져스 (2012)"
        elif self.series_no == "2":
            self.series_name = "어벤져스: 에이지 오브 울트론 (2015)"
        elif self.series_no == "3":
            self.series_name = "어벤져스: 인피니티 워 (2018)"
        elif self.series_no == "4":
            self.series_name = "어벤져스: 엔드게임 (2019)"


    def character_interactions(self):
        """상위 n개의 상호작용"""
        top_n = input("상위 몇개의 상호작용을 보시겠습니까?")
        while not top_n.isdigit():
            print("숫자를 입력해주세요.")
            top_n = input("상위 몇개의 상호작용을 보시겠습니까?")

        relationships = sorted(self.graphs[int(self.series_no)-1].edges(data=True), key=lambda x: x[2]['weight'], reverse=True)[0:int(top_n)]
        for i in range(len(relationships)):
            print("{}. {} & {} ({})".format(i+1, relationships[i][0], relationships[i][1], relationships[i][2]["weight"]))



    def key_characters(self):
        """상위 n개의 핵심인물"""
        top_n = input("상위 몇개의 캐릭터를 반환하시겠습니까?")
        while not top_n.isdigit():
            print("숫자를 입력해주세요.")
            top_n = input("상위 몇개의 캐릭터를 반환하시겠습니까?")

        top_characters = self.get_importance_df(self.graphs).T[int(self.series_no) - 1].sort_values(ascending=False)[0:int(top_n)].index

        print("{}의 핵심인물 상위 {}명:".format(self.series_name, top_n))
        for i in range(len(top_characters)):
            print("{}. {}".format(i+1, top_characters[i]))



    def script(self):
        Utils.Loading()
        Utils.Borderline()

        print("선택하신 시리즈는 <{}> 입니다.\n".format(self.series_name))

        choice = 0
        while choice != 4:
            print("어떤 것을 확인하시겠습니까?\n")
            print("1. 등장 인물들 간의 상호작용")
            print("2. 핵심 등장인물")
            print("3. 등장인물 그룹핑")
            print("4. 뒤로가기")
            try:
                choice = int(input(":"))
            except:
                choice = int(input(":"))

            if choice == 1:
                Utils.Borderline()
                self.character_interactions()
                print()
                input("아무키나 누르세요.")
                Utils.Borderline()

            elif choice == 2:
                Utils.Borderline()
                self.key_characters()
                print()
                input("아무키나 누르세요.")
                Utils.Borderline()

            elif choice == 3:
                pass

            elif choice == 4:
                pass

            else:
                print("잘못된 입력입니다.")







