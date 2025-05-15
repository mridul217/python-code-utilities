#6. File Compression Simulator
#Problem: Simulate a basic file compression algorithm by removing consecutive duplicate characters in a string and counting their occurrences.

def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        print("i", i)
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] +str(count))
    print(s[-1], str(count))
    print(compressed)
    return ''.join(compressed)

print(compress_string("aaabbccc"))
