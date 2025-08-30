def find_prob(a,b):
    if a==1:
        prob_a=0.2
        if b==1:
            prob_bga=0.85
        elif b==2:
            prob_bga=0.15
        else:
            print("Invalid choice")
            return
        prob_a_and_b=prob_a*prob_bga
        print(f"probability of b given that a happens is:{prob_bga}")
        print(f"probability of both events occuring is: {prob_a_and_b}")
    elif a==2:
        prob_a=0.8
        if b==1:
            prob_bga=0.02
        elif b==2:
            prob_bga=0.98
        else:
            print("Invalid choice")
            prob_a_and_b=prob_a*prob_bga
        print(f"probability of b given that a happens is:{prob_bga}")
        print(f"probability of both events occuring is: {prob_a_and_b}")
    else:
        print("Invalid choice")
        return
print("Lets calculate the probability of both events")
print("person has strep throat? \n1.yes\n2.no")
a=int(input("enter your choice: "))

print("did the person test positive?\n1.yes\n2.no")
b=int(input("enter your choice: "))

print("the probability for event a and b :")
find_prob(a,b)