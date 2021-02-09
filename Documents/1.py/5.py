#def profile(name, age, lang1, lang2, lang3, lang4,lang5):
#    print(lang1, lang2, lang3, lang4, lang5)

#profile("")


#가변 인자   

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
profile("김태호", 25, "kotlin", "swift")
