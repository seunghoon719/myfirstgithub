def std_weight(height, gender):
    if gender =='woman':
        std = height*height*0.0001*21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, std))
    else:
        std = height*height*0.0001*22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, std))


std_weight(170, 'woman')
