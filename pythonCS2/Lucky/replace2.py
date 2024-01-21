def replace2(text,target,replacement):
    result = ''
    for t in text:
        if t == target:
            t = replacement
        result += t
    return result



t1 = "Your natural leadership skills will shine, and you'll find success in unexpected places. Embrace the challenges that come your way, as they will only make you stronger. Remember to take some time for self-care to maintain your unstoppable energy."
t2 = replace2(t1,'.','.\n')
print(t2)