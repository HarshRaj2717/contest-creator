# contest-creator

Just pick up random questions from a list (with a balanced difficulty) to form a contest

## Usage

> Tested on Python >= 3.10

For contest with LeetCode questions: `python main.py`

For contest with CodeForces questions: `python main.py -cf`

By default, for CodeForces - ratings 1100, 1200, and 1300 are used. Run `python problems/codeforces/extract_problems.py` to get other ratings are needed.

