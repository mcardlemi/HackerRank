# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ =='__main__':
    T = input()
    for i in range(int(T)):
        junk = input()
        A = set(input().split())
        junk = input()
        B = set(input().split())
        if A.issubset(B):
            print(True)
        else:
            print(False)
        
    
    
