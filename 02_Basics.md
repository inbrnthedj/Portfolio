Some basic things

### Github Branches
Creates a copy of the main branch and allows check and verification 
if can be inserted in the main branch. Code is usually branched while 
new features are being developed. Branches can be merged when it has 
been checked and verified. In this case, each branch's code is 
identified as a "Feature Tip"
- **Commit Changes**: used when the developer is convinced that the code can be added to the main branch. Don't end the Commit message with a period (don't know why yet). Description is best to have less than 50 characters
- **Pull Request**: used when we need others to review our proposed changed/commit. The pull request can follow any commits, even if code is unfinished and can target specific users. By default, if you make a change on a branch you do not own, it's considered as a pull request and not a commit. Details of the approval of a pull request will be present in log files.

Note that the Main branch is the only deployed code and changes are not released until:
1. Commited
2. Pull command is issued
3. Code is reviewed and approved
4. Approved code is merged into the main branch
