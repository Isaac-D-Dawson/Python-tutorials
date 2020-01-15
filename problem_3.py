#Isaac!! I need your help!! right we have to use a new computer
#to continue with our lectures, we have got it working
#however it when I click on the VLC file called python_tut.xspf
#in the new computer the file gives an error it says
#'you input can't be opened:'
#So it turns out that the new computer has labled the 'python hard drive' as 'F'
#but the python_tut.xspf file lables the 'python hard drive' as 'D'
# I need you go into the and change the data so that it reads F: instead of D:
# 

#Once your done please email it to me :)

#you'll need to inspect the python_tut.xspf file for more intel 

#Thanks Isaac! :)

with open(r"python_tut_fix.xspf", "r") as targ:
    #print(targ.read())
    #print(targ.readlines().index("<location>file:///D"))
    with open(r"python_tut_fixed.xspf", "w") as result:
        for i in targ.readlines():
            curr_line = [j for j in i]
            try:
                d_index = curr_line.index("D")
                if curr_line[d_index] == "D":
                    curr_line[d_index] = "F"
                #result.write(curr_line)
                print(d_index)
            except:
                pass
            finally:
                print(curr_line)
                result.writelines(curr_line)
        
