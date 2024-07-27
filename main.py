import os
from random import randrange, shuffle


def main():
    print("\n=====================================")
    print("# Listing out today's 4 problems!")
    print(">>> Time limit: 120 minutes")
    print("=====================================\n")

    # reading the problems txt files
    easy_problems = []
    medium_problems = []
    hard_problems = []

    # getting the paths of each problems file
    script_path = os.path.dirname(os.path.abspath(__file__))
    problems_dir = os.path.join(script_path, "problems")
    easy_problems_file = os.path.join(problems_dir, "easy.txt")
    medium_problems_file = os.path.join(problems_dir, "medium.txt")
    hard_problems_file = os.path.join(problems_dir, "hard.txt")

    with open(easy_problems_file, "r") as file:
        easy_problems = file.read().splitlines()
        shuffle(easy_problems)
    with open(medium_problems_file, "r") as file:
        medium_problems = file.read().splitlines()
        shuffle(medium_problems)
    with open(hard_problems_file, "r") as file:
        hard_problems = file.read().splitlines()
        shuffle(hard_problems)

    final_problems = []
    # picking one problem from each category
    final_problems.append(easy_problems[randrange(len(easy_problems))])
    final_problems.append(medium_problems[randrange(len(medium_problems))])
    final_problems.append(hard_problems[randrange(len(hard_problems))])

    # adding one extra problem from a random category
    random_category = randrange(3)
    if random_category == 0:
        picked_problem = easy_problems[randrange(len(easy_problems))]
        while picked_problem in final_problems:
            picked_problem = easy_problems[randrange(len(easy_problems))]
        final_problems.append(picked_problem)
    elif random_category == 1:
        picked_problem = medium_problems[randrange(len(medium_problems))]
        while picked_problem in final_problems:
            picked_problem = medium_problems[randrange(len(medium_problems))]
        final_problems.append(picked_problem)
    else:
        picked_problem = hard_problems[randrange(len(hard_problems))]
        while picked_problem in final_problems:
            picked_problem = hard_problems[randrange(len(hard_problems))]
        final_problems.append(picked_problem)

    # Finally printing out the problems in a shuffled manner
    shuffle(final_problems)
    for i, problem in enumerate(final_problems):
        print(f"Problem {i + 1}: {problem}")


if __name__ == "__main__":
    main()
