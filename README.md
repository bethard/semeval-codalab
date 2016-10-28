

See these descriptions and tutorials on codalab:
- https://www.youtube.com/watch?v=mU1yEEMrMvY
- Competition Roadmap: https://github.com/codalab/codalab-competitions/wiki/User_Competition-Roadmap
- Quickstart: https://github.com/codalab/codalab-worksheets/wiki/Quickstart
- Running a Competition: https://github.com/codalab/codalab-competitions/wiki/User_Running-a-Competition


This particular example competition looks for submissions with the text "Hello World!". If it finds
it, it gives it a score of 1, otherwise a score of 0. Follow the steps below to customize it. You
may want to upload the competition with minimum (or no) editing first, just to get a feel of how a
competition bundle works.

Editing the sample bundle for your task:

- Edit competition.yaml to customize it for your task.
  - Edit the title and description.
  - Change the name of the logo file to your logo file.
  - Give suitable title for phase 1. (Replace "First phase" with title of phase.) You can add more phases, and edit details, through the graphical interface, after you upload the competition.
  - Edit start date as appropriate.
  - Change "correct" to the name of the evaluation metric for the phase, for example, fscore, accuracy, etc.
  - Change "numeric_format" for the required digits after the decimal point. For example, using 2 will show two digits after the decimal.

- Copy your logo image file into the competition directory.

- The directory "reference_data" has the gold answers file truth.txt. Update it with the gold answers for your task. 
- Zip the files in the "reference_data" directory into reference_data.zip. reference_data.zip should be placed in the competition directory.

- Edit the evaluation script (evaluation.py) in scoring_program directory.
  - If you change the name of your evaluation script, then change it in the metadata file as well.
  - If your script is not in python, then update the "metadata" file appropriately. For example, for perl, use "command: perl $program/evaluation.pl $input $output".
  - The evaluation script takes two commandline arguments, the input directory and the output directory. These pertain to where your competition files will be stored in the codalab system, and so largely you do not have to worry about them.
  - Do not change the names of the files scores.txt, truth.txt, answer.txt. If you do make sure, you take care of the dependencies.
  - "truth_file" is the variable for the gold answers file, submission_answer_file is for the submission file: change the script so that it reads and evaluates the submission appropriately for your task. (Edit the body of the script to compare data obtained from the submission with the data in truth.txt.)
  - Add format checking to the evaluation script. Make sure that the submission_answer_file has data in the right format.
  - The evaluation script should print the result in the file scores.txt: <metric name>:<score>
    For example, "correct:1" or "f-score:0.74".
  - Print additional details to STDOUT. 
- Zip the files in the scoring_program directory into scoring_program.zip. scoring_program.zip should be placed in the competition directory.

  
To upload the competition bundle:
- zip the files to create the bundle (not the directory holding the files)
Here is what I did on my machine: zip -r -X competition-bundle.zip *
- Go to codalab competitions website:
https://competitions.codalab.org/competitions/
Register (create an account), sign in.
- click on "My Competitions"
- click on the "Competitions I'm Running" tab
- click on "create competition" and upload the competition bundle


Once the competition has uploaded successfully:
- Note the secure url the system provides below the task title. This is the competition url that can be shared with others.
- Explore admin features at the top such as "Edit" and "Submissions". (Note that the edit button takes a few seconds to load the page.)
- Edit the task further as appropriate. Click on the "Allow teams" checkbox. Add details to various webpages. Add additional phases if needed.
- Upload a submission. It has to be a zipped file.
  - A sample answer file and its zipped form is provided in the "submission" directory.
  - Click on "participate". Click on "Submit / View Results".
  - Enter suitable description for each submission in the text box provided.
  - Click on the "Submit" button to upload the file.
This should execute the evaluation script on the submission and store the results.  Unfortunately,
codalab has some bugs currently (which may be fixed by the time you read this). So be patient, and
upload the submission a few times if it does not succeed initially. The system should run
successfully after a few uploads.  If system shows status as "submitting", then wait a few seconds,
and click on the refresh button. A successful execution of the evaluation script will result in
a status of "Finished".
Here are some errors that one may get due to no fault of theirs:
(a) some times the system says: can't open the evaluation script, permission denied
(b) some times the system says: OSError: [Errno 39] Directory not empty
(c) some times the system just says submitted; and does not finish executing the evaluation script
(d) some times the system stalls with the status "submitting".
We have informed codalab developers of the bug.
  - Explore various files generated on running the evaluation script. For example, text sent to STDOUT will be available in "View scoring output log". Add submission to leaderboard. Click on "Results" to see the leaderboard.

