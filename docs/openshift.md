$ rhc app create devl4c diy-0.1 cron-1.4
Password: ********

$ cd devl4c
$ git remote add upstream -m master git://github.com/linux4chemistry/linux4chemistry.git
$ git pull -s recursive -X theirs upstream master
$ git push

