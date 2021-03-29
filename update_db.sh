#! /bin/sh
mv $1 'sde.sqlite'
sqlite3 'data.sqlite' "attach 'sde.sqlite' as sde; replace into main.invTypes select * from sde.invTypes;"
mv 'sde.sqlite' $1
