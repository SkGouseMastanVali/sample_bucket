# simple_bucket
just practice repo

test repo to perform some simple operations through CMD.

####################
1. Login to your github account
2. Create a new repo using UI
   (create new repo-->repo name (test)-->public-->initialise README.Md file--->create Repo)
3. Clone your repo (test) from git to the local machine
  (open your created repo (test) and clone it; copy the repo url link)
4. Open the gitbash and select the location where you want to clone the repo by using CD command
5. Now write the command "git clone 'your repo url'"
6. Use "ls" command to view your repo and by using "cd" command move into your repo and "ls", to see all the files in the repo (only README.Md file will be avaialble as of now)
7. Now select the file (abc.py) which you want to dump into your repo and make sure the file need to be in your local repo (test).
8. Now write "git status" in gitbash terminal, i will show you the latest modifications,chages,branch etc info
9. Now you can add your abc.py file to the git,use the command "git add abc.py"
10. Now your abc.py file is in stagging area, and waiting to being commit.
11. Use "git status" command , to check the status of new updations in your repo
12. now commit(save) your file by using "git commit" command and you can also give message to that commit like this "git commit -m 'abc.py file added' "
13. Still the file is in your local machine only,not dumped into the git server.
14. Now use "git log" command to see the log of commit history
15. Once again check the status of your repo , to know whether is there any file in stagging area or anything is happening "git status"
16. Now use "git push" command , it will push all the files to your git server(cloud)
17. -----For checking----
18. Do some changes in your local abc.py file and hit "git status" command in gitbash, it will tell you that changes that occured
19. You can again add updated abc.py file to git by using "git add abc.py", once done again check the status
20. Use "git difftool HEAD" , to see the difference between your previous file data and updated file data
21. use "git commit -m 'added abc.py updated file'"
22. hit "git push"
23. 
