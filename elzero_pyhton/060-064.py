def get_score(**scores):
    for sub, score in scores.items():
        print(f"{sub} => {score}")


get_score(Math=90, Science=80, Language=70)

get_score(Logic=70, Problems=60)

#=============================================
