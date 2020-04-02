###ELSE-IF STATEMENT

##Here, the string Bob is assigned to name the integer 3000 is assigned to Agent
#and so now we're at the ifstatement. This condition is checked and it's false
#so it skips that block.

##Then this Elif statement has its condition checked. It's also false so we skip
#that and then here this is the first true condition that we found.

##So the execution enters inside of this block prints that out and that it just
#skips all of the otherconditions.

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age <12:
    print('You are not Alice, Kiddo')
elif age > 2000:
    print('Great!')
elif age > 100:
    print('Sorry you are not Alice')
