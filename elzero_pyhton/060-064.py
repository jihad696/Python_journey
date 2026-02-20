# def get_score(**scores):
#     for sub, score in scores.items():
#         print(f"{sub} => {score}")


# # get_score(Math=90, Science=80, Language=70)

# # get_score(Logic=70, Problems=60)


# # =============================================
def get_people_scores(name="", **scores):
    if not name and not scores:
        print("You Have No Scores To Show")
    elif name and scores:
        print(f"Hello {name} This is your Score Table:")
        for sub, score in scores.items():
            print(f"{sub} => {score}")
    elif name and not scores:
        print(f"Hello {name} You Have No Scores To Show")
    elif not name and scores:
        for sub, score in scores.items():
            print(f"{sub} => {score}")


# get_people_scores()
# get_people_scores("Ahmed")
# get_people_scores(Math=90, Science=80)
# get_people_scores("Osama", Math=90, Science=80)


# ===========================================
scores_list = {"Math": 90, "Science": 80, "Language": 70}

def get_the_scores(name="", **scores):
    if name and not scores:
        print(f"Hello {name} You Have No Scores To Show")
    elif name and scores:
        print(f"Hello {name} This Is Your Score Table:")
        for subject, score in scores.items():
            print(f"- {subject} => {score}")
    else:
        for subject, score in scores.items():
            print(f"- {subject} => {score}")

get_the_scores("Osama", **scores_list)   
#============================================================



