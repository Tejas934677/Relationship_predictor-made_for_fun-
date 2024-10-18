for i in range(20) :

    def meaning(result):

        full = {
            'F': 'FRIENDSHIP',
            'L': 'LOVE',
            'A': 'AFFECTION',
            'M': 'MARRIAGE',
            'E': 'ENEMY',
            'S': 'SIBLINGS'
        }
        return full.get(result)
        

    def flames(boy, girl):

        flames = 'FLAMES'

        for i in boy:
            if i in girl:
                girl = girl.replace(i, '', 1)
                boy = boy.replace(i, '', 1)

        flamed_name = boy + girl

    
        length = len(flamed_name)

        while len(flames) != 1:

            if len(flames) >= length:
                out = flames[length - 1]
                flames = flames.replace(out, '', 1)

            else:
                out = flames[(length % len(flames)) - 1]
                flames = flames.replace(out, '', 1)

        

        print( "_" * 45, meaning(flames)   , "_"*45  )

    print("Welcome to the relastionship predictor\n(Not to take this as serious made just for fun )")
    boy = ("raju")
    girl =("ankitha ")
    flames(boy, girl)

    print(f'The both {boy} and  {girl} belong to above this |^|\n \t\t CONGRATS {boy} ' )
        
