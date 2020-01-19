for i in range(1, 12):
    print("No. {} SQUARED IS {} AND CUBED IS {:4}".format(i,i**2,i**4));
    print("CALCULATION COMPLETE");
    print("tru again\n")

#

print("please guess a numnber between 1 and 10\n");
guess=int(input());
if(guess!=5):
    if(guess<5):
        print("please guess higher");
    else:
        print("please guess lower")
    guess=int(input());
    if guess==5:
        print("well done");
    else:
        print("game over");
else:
    print("congrats! you guessed it on first time");

# using if with strings activity
tree1=int(input("plese enter tree1\n"));
tree2=int(input("plese enter tree2\n"));
if(tree1==tree2):
    print("Trees are equal");
else:
    print("trees are different");