def calculateArea(L,W):
    return L*W


if __name__ == "__main__": # direct calling 
    import sys
    inputL = eval(sys.argv[1])
    inputW = eval(sys.argv[2])
    A = calculateArea(inputL,inputW)
    print(A)
    
  




