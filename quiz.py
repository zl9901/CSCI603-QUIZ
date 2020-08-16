

def main():
    i = 0
    print(i)
    i+=1
    print(i)
    index = 1
    max=10
    min=1
    while(i<=10 and i>=1):


        i=i+index
        print(i)
        if i==max:
            index=-1
            i-=1
            print(i)
            max-=1
            if max==5:
                break
        if i==min:
            index=1
            i+=1
            print(i)
            min+=1
            if min == 5:
                break

if __name__ == "__main__":
	main()