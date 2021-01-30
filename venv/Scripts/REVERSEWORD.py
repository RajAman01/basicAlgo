def reverse(sentance):
    word = sentance.split(' ')
    reverseSentance = ' '.join(reversed(word))
    return reverseSentance
if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print (reverse(input))
