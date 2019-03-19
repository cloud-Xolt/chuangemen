myApp.directive('samVideo', function() {
    return {
        restrict: 'AE',//属性或控件方式,
        replace: true,
        scope: {
            video: "=",//来自服务器的视频参数可以放在这
            videocb: "=" //回调函数写在这
        },
        template: '<div id="videoPlayer" style="height: 100%;"></div>',
        link: function (scope, iElement, iAttrs) {
            if (scope.video) {//判断是否包含视频路径等参数

                var ckplayer = window["ckplayer"];//html引入ckplayer.js文件后window中可查看到ckplyer的dom
                var videoObject = {
                    // autoplay: true,//自动执行
                    container: "#videoPlayer",//绑定容器id
                    debug: false, //是否开启调试模式
                    drag: 'start', //拖动的属性
                    html5m3u8: false, //PC平台上是否使用h5播放器播放m3u8
                    // preview: { //预览图片
                    //     file: ['material/mydream_en1800_1010_01.png', 'material/mydream_en1800_1010_02.png'],
                    //     scale: 2
                    // },
                    // flashplayer: true,//强制flash
                    // loaded: 'loadedHandler', //当播放器加载后执行的函数，设定一些监听，官方js中的写法
                    // loaded: scope.videocb.videocallback(scope.videocb),//此处是重点回调
                    // loop: true, //播放结束是否循环播放
                    mobileCkControls:true,//是否在移动端（包括ios）环境中显示控制栏
                    poster: scope.video.img_url, //封面图片
                    // seek: 0, //默认跳转的时间
                    autoplay:false,//自动播放
                    live:true,
                    variable: "player",//初始函数
                    // video: "CK:" + scope.video.video_url,//加密后强制变为flash方式，无法在移动端观看视频，移动端不支持flash。
                    video: scope.video.video_url //来自服务器的视频地址
                };

                scope.player = new ckplayer(videoObject);

            }

        }
    }
 });
