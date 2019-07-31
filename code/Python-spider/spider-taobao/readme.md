#  执行后台任务

nohup python -u main.py > test.log 2>&1 &

# 查看后台任务

ps -aux | grep python

# 关闭 

kill 