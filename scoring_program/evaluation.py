#!/usr/bin/env python
import sys
import os.path

# as per the metadata file, input and output directories are the arguments
[_, input_dir, output_dir] = sys.argv

# unzipped submission data is always in the 'res' subdirectory
# https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
submission_path = os.path.join(input_dir, 'res', 'answer.txt')
if not os.path.exists(submission_path):
    sys.exit('Could not find submission file {0}'.format(submission_path))
with open(submission_path) as submission_file:
    submission = submission_file.read()

# unzipped reference data is always in the 'ref' subdirectory
# https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
with open(os.path.join(input_dir, 'ref', 'truth.txt')) as truth_file:
    truth = truth_file.read()

# the scores for the leaderboard must be in a file named "scores.txt"
# https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
with open(os.path.join(output_dir, 'scores.txt'), 'w') as output_file:
    score = 1 if truth == submission else 0
    output_file.write("correct:{0}".format(score))
