# Task: Write a program using function to return your name into TitleCase
# documentation link for title() function "https://docs.python.org/3/library/stdtypes.html#str.title"
f_name=input("Enter your First Name\n")
l_name=input("Enter your Last Name\n")

def titlecase(fname,lname):
    if fname == "" or lname=="":
        return f"Please provide valid inputs"
    return f"Result: {fname.title()} {lname.title()}"

print(titlecase(f_name,l_name))
