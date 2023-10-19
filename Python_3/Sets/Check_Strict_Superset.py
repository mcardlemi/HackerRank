# Enter your code here. Read input from STDIN. Print output to STDOUT
# need to ask someone why this needs the for loop regarding C. Also frustrating because it seems the solution is just to have superset?
if __name__ == '__main__':
    A = set(input().split())
    n = int(input())
    B = set([])
    C = B
    for i in range(n):
        B.update(set(input().split()))
    for i in list(A):
        C.discard(i)
    if A.issuperset(B) and len(A-B) >0:
        print(True)
    else:
        print(False)
    
            
