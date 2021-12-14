import phonenumbers
import os
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

def main():
    ch_input = input("Enter your no, with country code: \n")

    ch_number = phonenumbers.parse(ch_input,'CH')

    num_check = phonenumbers.is_possible_number(ch_number)

    def rerun():
        print("Try again [y/n] : ")
        re_in = input().strip().lower()

        if re_in == "y":
            os.system("cls")
            main()
        elif re_in == "n":
            exit()
        else:
            rerun()


    if num_check == True:
        print("************COUNTRY**************")
        print(geocoder.description_for_number(ch_number,"en"))

        ch_carrier = phonenumbers.parse(ch_input,'RO')
        print("\n************SERVICE PROVIDER***************")
        print(carrier.name_for_number(ch_carrier,'en'))

        ch_time = phonenumbers.parse(ch_input,"GB")
        print("\n************TIME ZONE****************")
        print(timezone.time_zones_for_number(ch_time))


    else:
        print("Your entered the invalid num!!\n")
        rerun()
    
    


main()
