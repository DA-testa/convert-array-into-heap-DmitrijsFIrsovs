# python3


def build_heap(data):
    a = len(data)
    swaps = []
    for i in range(a, -1, -1):
        j=i
        while True:
            lc = j * 2 + 1
            if lc >= a:
                break
            if lc + 1 < a and data[lc+1] < data[lc]:
                lc = lc + 1
            if data[j] < data[lc]:              
                swaps.append((j, lc))
                data[j], data[lc] = data[lc] , data[j]
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
