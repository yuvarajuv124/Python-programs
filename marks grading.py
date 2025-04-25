telugu = int(input('Enter telugu marks: '))
english = int(input('Enter english marks: '))
hindi = int(input('Enter hindi marks: '))
maths = int(input('Enter maths marks: '))
science = int(input('Enter science marks: '))
sum = telugu+english+hindi+maths+science
if(telugu>=35 and english>=35 and hindi>=35 and maths>=35 and science>=35):
    print("Student has passed")
    if(sum>=420):
        print('Student got A grade')
    elif(sum>=350):
        print('Student got B grade')
    elif(sum>=270):
        print('Student got C grade')
    elif(sum>=175):
        print('Student got D grade')
else:
    print('Student has failed')