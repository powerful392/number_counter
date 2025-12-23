import googletrans
import sys
translator = googletrans.Translator()
language = input("please choose your language, type en or english for english, pe or persian for persian")
list_of_numbers = []
message0 = "چندتا عدد میخوای وارد کنی، به عدد وارد کن\n"
translated0 = translator.translate(message0, src="fa", dest="en").text
if language.lower().strip() == "en" or language.lower().strip() == "english":
    while True:
        try:
            few = int(input(translated0))
            break
        except ValueError:
            few = int(input("please just enter number"))
    message1 = "عدد رو وارد کن\n"
    translated1 = translator.translate(message1, src="fa", dest="en").text
    for few1 in range(few):
        while True:
            try:
                number = int(input(translated1))
                break
            except ValueError:
                number = int(input("please just enter number"))
        list_of_numbers.append(number)
elif language.lower().strip() == "pe" or language.lower().strip() == "persian":
    while True:
        try:
            few = int(input("چندتا عدد میخوای وارد کنی، به عدد وارد کن\n"))
            break
        except ValueError:
            few = int(input("لطفاً فقط عدد وارد کن\n"))
    for few1 in range(few):
        try:
            number = int(input("عدد رو وارد کن\n"))
        except ValueError:
            number = int(input("لطفاً فقط عدد وارد کن\n"))
        list_of_numbers.append(number)
else:
    print("invalid language, please restart the program again")
    print("زبان نامعتبر لطفاً برنامه را دوباره اجرا کنید")
    sys.exit()
convert_tuple = tuple(list_of_numbers)
result = sum(convert_tuple)
print(result)