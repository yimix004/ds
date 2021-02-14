def DisplayName():
    ''' This function is to display names '''
    print("My name is Yimika")
    return;

DisplayName.__doc__

def show_name(firstname, lastname):
    ''' This function is to display name '''
    print(firstname, ',' ,lastname)
    
show_name(firstname='Akinsola', lastname='Akinwale')

def d_Name(firstname, lastname='Oni'):
    ''' Display first and last name '''
    print(firstname, ',', lastname)

d_Name(firstname='Yimika')

def displaynames(*names, lastname):
    '''display all names plus last name '''
    print(names, ',', lastname)

displaynames('Yimika', 'David', lastname='Oni')

def myf(n):
    return lambda a: a * n

multiply= myf(2)
print(multiply(4))