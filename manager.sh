#!/bin/bash 
### 
# @Author: Youshumin
# @Date: 2019-11-15 12:01:01
 # @LastEditors: YouShumin
 # @LastEditTime: 2020-09-27 11:56:46
# @Description: 
###

workdir=$(cd $(dirname $0); pwd) 
export PYTHONPATH=$PYTHONPATH:${workdir} 
export RUN_ENV=prod
pyenv="${workdir}/.env/bin/python"
start_main(){
    cd $workdir
    ${pyenv} run_server.py --host=0.0.0.0 --port=30001 --debug=True
}

rbac_db_init(){
    cd ${workdir}/dblib/
    ${pyenv} module.py create
    # ${pyenv} module.py create
}

rbac_db_del(){
    cd ${workdir} 
    ${pyenv} module.py drop
}
case "$1" in 
    start)
        start_main
        ;;
    dbinit)
        rbac_db_init
        ;;
    dbdel)
        rbac_db_del
        ;;
    *)
        echo "start, dbinit"
        ;;
esac