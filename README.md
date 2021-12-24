# sample_bucket
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
6. Use "ls" command to view your repo and by using "cd" command move into your repo and "ls", to see all the files in the repo (only README.Md file will be avaialble for now)
            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ ls
            README.md

8. Now select the file (final.py) which you want to dump into your repo and make sure the file need to be in your local repo (test).
9. Now write "git status" in gitbash terminal, i will show you the latest modifications,chages,branch etc info
            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ git status
            On branch main
            Your branch is up to date with 'origin/main'.
            nothing to commit, working tree clean

11. Now you can add your final.py file to the git,use the command "git add final.py"
            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ git add final.py
13. Now your final.py file is in stagging area, and waiting to being commit.
14. Use "git status" command , to check the status of new updations in your repo and also view the file by using "ls" command
            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ ls
            README.md  final.py 
            
            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ git status
            On branch main
            Your branch is up to date with 'origin/main'.

            Changes to be committed:
              (use "git restore --staged <file>..." to unstage)
                    new file:   final.py


16. now commit(save) your file by using "git commit" command and you can also give message to that commit like this "git commit -m 'final.py file added' "

            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ git commit -m 'final.py file added'
            [main 841210d] final.py file added
             1 file changed, 0 insertions(+), 0 deletions(-)
             create mode 100644 final.py

18. Still the file is in your local machine only,not dumped into the git server.
19. Now use "git log" command to see the log of commit history

               gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
               $ git log
               commit 841210d08fd17ea930a7b73371a2ad88333c6a82 (HEAD -> main)
               Author: SkGouseMastanVali <gousemastan7867@gmail.com>
               Date:   Fri Dec 24 16:55:19 2021 +0530

                   final.py file added

               commit 1014444f9b523810c85c1e0a571439317165ba9f (origin/main, origin/HEAD)
               Author: SkGouseMastanVali <gousemastan7867@gmail.com>
               Date:   Tue Dec 21 16:26:46 2021 +0530

                    This is my project file and commiting to test the git commands through
                    gitbash

               commit 787be94cc3fbdd3d89a1e4228ea0138c60f52230
               Author: SkGouseMastanVali <46440821+SkGouseMastanVali@users.noreply.github.com>
               Date:   Tue Dec 21 16:10:02 2021 +0530

                   Update README.md

               commit 413aa831e4fa0f6ccfd5bde21890361009fd3c50
               Author: SkGouseMastanVali <46440821+SkGouseMastanVali@users.noreply.github.com>
               Date:   Tue Dec 21 16:09:11 2021 +0530

                   Initial commit

21. Once again check the status of your repo , to know whether is there any file in stagging area or anything is happening "git status"

            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ git status
            On branch main
            Your branch is ahead of 'origin/main' by 1 commit.
              (use "git push" to publish your local commits)

            nothing to commit, working tree clean

23. Now use "git push" command , it will push all the files to your git server(cloud)

            gmvsh@DESKTOP-A48UB5N MINGW64 ~/desktop/tasks/git/sample_bucket (main)
            $ git push
            Enumerating objects: 7, done.
            Counting objects: 100% (7/7), done.
            Delta compression using up to 8 threads
            Compressing objects: 100% (4/4), done.
            Writing objects: 100% (5/5), 690 bytes | 690.00 KiB/s, done.
            Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
            To https://github.com/SkGouseMastanVali/sample_bucket.git
               22c5d73..061c81e  main -> main



25. -----For checking----
26. Do some changes in your local abc.py file and hit "git status" command in gitbash, it will tell you that changes that occured
27. You can again add updated abc.py file to git by using "git add final.py", once done again check the status
28. Use "git difftool HEAD" , to see the difference between your previous file data and updated file data
29. use "git commit -m 'added final.py updated file'"
30. hit "git push"

