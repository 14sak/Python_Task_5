from one.text_num import extractNums
from one.getUserInput import getUserInput as INPUT
from two.date_format import Date_format
from two.get_userIN import getDate

def main(): 
    user_data = INPUT()
    output = extractNums(user_data)
    print(f'Extracted numbers from string={output}')

    print('---')
    UserDate=getDate()
    output2=Date_format(UserDate['input'])
    print(f'Corrected date format = {output2}')


if __name__ == '__main__':
    main() 
