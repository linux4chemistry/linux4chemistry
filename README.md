How to deploy on OpenShift
--------------------------

    $ rhc create-app l4c python-2.7 cron-1.4
    $ cd l4c
    $ git remote add upstream \
      https://github.com/linux4chemistry/linux4chemistry.git
    $ git pull -s recursive -X theirs upstream master
    $ git push 

