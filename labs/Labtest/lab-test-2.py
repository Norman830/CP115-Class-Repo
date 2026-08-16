#programmer's name : Norman Danish Bin Rajimin
#problem description : write a code that print students detail,star pattern,how much marks the student wants that uses an appropriate escape character and arithmetix expression

name = str(input("Name:"))                       #asking for the student's name
matric_no = str(input("matric no:"))             #asking for the student unique Matric number
mark1 = int(input("first mark:"))                #asking for the student first mark the student wants before multiplying
mark2 = int(input("second mark:"))               #asking for the student second mark the student wants before multiplying
full_mark = mark1*mark2                          #arithmetic expression/operation needed in the code and the full marks after multiplying

print(f"Name:{name}\t\t\t\tMatric.No:{matric_no}\n\n"                   #print the student's name and matric number
      f"*\t\t\t*\n"                                                     #print the start of the star pattern
      f"**\t\t**\n"                                                     #print the star pattern
      f"***\t***\n"                                                     #print the star pattern
      f"********\n"                                                     #print the star pattern
      f"***\t***\n"                                                     #print the star pattern
      f"**\t\t**\n"                                                     #print the star pattern
      f"*\t\t\t*\n\n"                                                   #print the end of the star pattern
      f"This is my\n\tsecond\n\t\tassignment\n"                         #print of the correct indentation
      f"I want {mark1}x{mark2} marks, which is {full_mark} full marks") #print how many marks the students wants and the fullmarks