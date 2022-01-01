def main():
    #print("Enter the alphabet : ")
    u_inp = input().lower().strip()

    alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for idx,val in enumerate(alpha):
        if val==u_inp:
            print(val,idx+1)
        
    if u_inp not in alpha:
        print("invalid input")

    def remain():
        print("\ncontinue? [y/n]")
        re_inp = input().lower().strip()
        
        if re_inp=="y":
            print("\n")
            main()
        elif re_inp=="n":
            exit()
        else:
            remain()

    remain()



        
        

    

main()
