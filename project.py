import random
TRUTH_FILE = "truth.txt"
DARE_FILE = "dare.txt"

def main():
    while True:
        choice = input('Enter Truth or Dare: \n')
        if choice.lower() == 'truth':
            print(truth())
        elif choice.lower() == 'dare':
            print(dare())
        else:
            print('Invalid choice, Try again.')
        print()
        print("Next player.")

    # function to get truth sentence from a file
def truth():
    list_of_truth = []
    with open(TRUTH_FILE) as truth_sen:
        for line in truth_sen:
            sen = line.strip()
            list_of_truth.append(sen)
    rand_truth = random.choice(list_of_truth)
    return rand_truth

    # function to get dare sentence from a file
def dare():
    list_of_dare = []
    with open(DARE_FILE) as dare_sen:
        for line in dare_sen:
            sen = line.strip()
            list_of_dare.append(sen)
    rand_dare = random.choice(list_of_dare)
    return rand_dare
if __name__ == '__main__':
    main()
