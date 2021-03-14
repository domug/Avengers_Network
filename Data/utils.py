import pandas as pd
import re

def get_script_by_scene(path):
    """각 scene별로 스크립트 반환
    
    Returns
    ----------
    list
        script of each scenes
    """
    with open(path, "r") as file:
        script = file.read()
    script_by_scene = script.split("#")
    
    return script_by_scene




def make_weight_df(script_by_scene):
    """가중치 데이터프레임 정의
    
    Returns
    ----------
    DataFrame
        weight dataframe
    """
    df = pd.DataFrame(columns=["Source", "Target", "Type", "weight"])  # 노드간 엣지 가중치를 저장할 데이터프레임
    
    for scenes in script_by_scene:
        
        # 특정 씬의 등장인물들을 발화 순서대로 기록
        characters = []
        for sent in scenes.split("\n"):
            speaker = re.findall(r"[\w\W]+:", sent)
            if speaker:
                characters.append(speaker[0].replace(":", "").upper())


        # 데이터프레임에 엣지 가중치 추가
        for i in range(len(characters) - 1):
            target1 = characters[i]
            target2 = characters[i+1]

            filter1 = (df.Source == target1) & (df.Target == target2)
            filter2 = (df.Source == target2) & (df.Target == target1)

            # 노드가 데이터프레임에 없을시 새로 추가
            if len(df[filter1 | filter2]) == 0:
                dict1 = {"Source": target1, 
                         "Target": target2,
                         "Type": "Undirected",
                         "weight": 0}     
                df = df.append(dict1, ignore_index=True)


            # 해당 노드 간에 가중치 추가
            filter1 = (df.Source == target1) & (df.Target == target2)
            filter2 = (df.Source == target2) & (df.Target == target1)
            index = df[filter1 | filter2].index
            df.iloc[index, 3] += 1
            
    return df




def preprocess(df, series_no:int):
    """추가적인 전처리를 위한 함수
    
    Returns
    ----------
    DataFrame
        fully preprocessed dataframe of edge weights
    
    """
    
    # 1. 중복 행 처리
    df_unique = df.iloc[df[["Source", "Target"]].drop_duplicates().index, :]
    df_duplicates = df[df[["Source", "Target"]].duplicated()]

    for index, row in df_duplicates.iterrows():
        source = row.Source
        target = row.Target
        weight = int(row.weight)

        add_index = df_unique[(df_unique.Source == source) & (df_unique.Target == target)].index
        df.iloc[add_index, 3] += weight


    final_df = df.iloc[df[["Source", "Target"]].drop_duplicates().index, :]
    
    
    # 2. 노드명이 공란인 행 제거
    empty_index = []
    for index, row in final_df.iterrows():
        if (row.Source == "") or (row.Target == ""):
            empty_index.append(index)

    final_df.drop(empty_index, axis=0, inplace=True)
    
    
    # 3. 노드 간 방향성을 제거
    del_index = []
    for index, row in final_df.iterrows():
        source = row.Source
        target = row.Target
        rev_df = final_df[(final_df.Source == target) & (final_df.Target == source)]

        if len(rev_df) > 0:
            row.weight += int(rev_df.weight)
            del_index.append(rev_df.index[0])

    final_df = final_df.drop(del_index, axis=0)
    final_df = final_df.sort_values(by=["weight"], ascending=False).reset_index(drop=True)
    final_df["series"] = series_no
    
    return final_df


