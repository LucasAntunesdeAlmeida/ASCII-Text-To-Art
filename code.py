from writer import writer

def main():
    Text = int(input('Input text:'))
    for i in range(6):
        writer(Text, i)

if __name__ == '__main__':
    main()
