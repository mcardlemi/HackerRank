# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    
    groupSize = input()
    rooms = input().split()
    roomSet = set(rooms)
    for i in list(roomSet):
        rooms.remove(i)
    
    print(roomSet.difference(set(rooms)).pop())
