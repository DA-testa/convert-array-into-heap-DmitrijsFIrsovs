# python3


def build_heap(info):
    a = len(info)
    swaps = []
    for i in range(a, -1, -1):
        j=i
        while True:
            lc = j * 1 + 1
            if lc >= a:
                break
            if lc + 1 < a and info[lc+1] < info[lc]:
                lc = lc + 1
            if info[j] < info[lc]:              
                swaps.append((j, lc))
                info[j], info[lc] = info[lc] , info[j]
                j = lc
            else:
                break
    return swaps                
                
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

 
    


def main():
    option = str(input())
    if "I" in option:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        return
    if "F" in option:
        file_name = str(input())
        file_name = "tests/" + str(file_name)
        with open(file_name, 'r') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
        assert len(data) == n            
        swaps = build_heap(data)
        print(len(swaps))
        return    
  


if __name__ == "__main__":
    main()
