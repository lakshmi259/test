#!/u01/app/oracle/jun2/middleware/wls12c/oracle_common/common/bin/wlst.sh
connect('weblogic','weblogic1','t3://192.168.0.148:9094')
deploy(appName='benefits',path='/u01/app/oracle/jun2/middleware/applications/benefits.war',targets='admin_test')
startApplication('benefits')
disconnect()
exit()






