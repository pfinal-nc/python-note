<?php
    /**
     * Created By ${pROJECT_NAME}.
     * User: pfinal
     * Date: 2019/8/12
     * Time: 下午12:39
     * ----------------------------------------
     */
    $result = file_get_contents(__DIR__.'/config.py');
    if (@$_POST['ip']) {
        $ips = '';
        if (count($_POST['ip']) > 0) {
            foreach ($_POST['ip'] as $ip) {
                if ($ip) {
                    $ips .= "'".$ip."',\n";
                }
            }
            $result = preg_replace('/PROXIES\s+=\s+(.*)/s', "\nPROXIES = [\n".$ips."\n]", $result);
            file_put_contents(__DIR__.'/config.py', $result);
        }
    }
    $proxies_list = [];
    $res = preg_match('/PROXIES\s+=\s+(.*)/s', $result, $matches);
    if ($res) {
        $proxies_list = explode(',', str_replace(["\n", "\r", "\r\n", "[", "'", ",]"], '', $matches[1]));
    }
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>爬虫面板</title>
    <link href="https://cdn.bootcss.com/twitter-bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.bootcss.com/jquery/2.2.3/jquery.min.js"></script>
</head>
<body>
<div class="container">
    <br>
    <div class="panel panel-default">
        <div class="panel-body" style="background-color:#1677b3;color:#ffffff">
            <h2><i>允典爬虫面板</i><i style="font-size: 0.1rem;color:#000"> ( Author:pfinal )</i></h2>
        </div>
    </div>
    <div class="panel panel-danger">
        <div class="panel-heading">代理设置</div>
        <div class="panel-body">
            <form class="form-inline" METHOD="post" action="">
                <div class="form-group">
                    <label for="exampleInputEmail1">代理ip:</label>
                    <?php if (count($proxies_list) > 0) { ?>
                        <?php foreach ($proxies_list as $item) { ?>
                            <input type="text" class="form-control" name="ip[]" placeholder="请输入代理IP和端口"
                                   value="<?php echo trim($item, "'"); ?>">
                        <?php } ?>
                    <?php } ?>
                </div>
                <button type="submit" class="btn btn-primary">更新</button>
            </form>
        </div>
        <div class="panel-footer">
            代理地址: <a href="http://h.zhimaruanjian.com/getapi/">获取代理</a>
        </div>
    </div>
    <div class="panel panel-danger">
        <div class="panel-heading">开始执行</div>
        <div class="panel-body">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <button onclick="run(this)" class="btn btn-primary btn-xs">开始执行</button>
                </div>
                <div class="panel-body">
                    <div class="panel panel-default">
                        <div class="panel-body" id="log" style="background-color:#000000;color:#ffffff">

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script>

    function get_log() {
        $.ajax({
            type: 'post',
            url: 'http://127.0.0.1:9000',
            dataType: 'json',
            data: {date: new Date()},
            success: function (data) {
                if (data.code == 200) {
                    $("#log").empty().append('<pre><p style="color:green">' + data.result + '</p></pre>')
                }
            }
        })


    }

    function run(obj) {
        //alert(123)
        $.ajax({
            type: 'get',
            url: 'http://127.0.0.1:9000',
            success: function (data) {
                if (data.code == "200") {
                    setInterval(function () {
                        get_log()
                    }, 15000)
                }
            }
        })
    }

</script>
</body>
</html>
