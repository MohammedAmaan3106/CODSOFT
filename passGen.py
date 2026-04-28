import random  

print("-------------------PASSWORD GENERATOR-------------------")  

characters_for_Easy = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                        'n','o','p','q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_']  


characters_for_Medium = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                        'n','o','p','q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                        '0','1','2','3','4','5','6','7','8','9','_']  


characters_for_Hard = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                        'n','o','p','q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                        '!','@','$','%','^','&','*','~','#','?','/','|','=',
                        '0','1','2','3','4','5','6','7','8','9','_']  

generate = []  

password_len = int(input("Enter The Password Length You Want: "))  

if (password_len <= 0):  
    print("Invalid Input!, Try Again")  
    exit() 
     
else:  
    complexity = input("Enter The Password Complexity(Easy/Medium/Hard): ")  
    complexity = complexity.lower()  

    if complexity == "easy":  
        for i in range(password_len):  
            generate.append(random.choice(characters_for_Easy))  

    elif complexity == "medium":  
        for i in range(password_len):  
            generate.append(random.choice(characters_for_Medium))  

    elif complexity == "hard":  
        for i in range(password_len):  
            generate.append(random.choice(characters_for_Hard))  

    else:  
        print("Invalid Complexity! , Try Again")  
        exit()  

print(f"Your Generated Password: {''.join(generate)}")  

print("-------------------Thank You-------------------")