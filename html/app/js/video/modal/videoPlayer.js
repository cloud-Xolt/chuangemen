myApp.controller('VideoPlayController', ['$scope', "apiService",
    '$stateParams', function ($scope, apiService, $stateParams) {

        apiService.video.anthology.get($stateParams.episodeId).then(function(data){
            //参数的定义回调
            //定义视频对象，可以来自服务器
            $scope.videoDetails = {
                content: "测试",
                create_date: 1534316308000,
                img_url: $stateParams.imageUrl, //封面图片
                title: data.video,

                // 视频地址
                // video_url: [
                    //         ['http://ivi.bupt.edu.cn/hls/cctv1.m3u8', 'video/m3u8', '中文标清', 0],
                    //         ['rtmp://58.200.131.2:1935/livetv/cctv1hd', 'video/mp4', '中文高清', 0],
                    //         ['http://img.ksbbs.com/asset/Mon_1703/eb048d7839442d0.mp4', 'video/mp4', '英文高清', 0],
                    //         ['http://img.ksbbs.com/asset/Mon_1703/d30e02a5626c066.mp4', 'video/mp4', '英文超清', 0]
                    //     ]
                video_url: data.path
            };
        });


        //回调参数，里面定义了一个回调函数，然后由directive回调的时候回传ckplayer对象own，并使用$timeout延迟加载以确保不为null
        // $scope.videocb = {
        //     videocallback: function (own) {
        //         if (this.timeout) {
        //             this.$timeout.cancel(this.timeout);
        //         }
        //         this.timeout = this.$timeout(x => {
        //
        //             // console.log("timeout player = ", this.videocb["player"], own.player);
        //             own.player.addListener('ended', this.endedHandler); //监听播放结束
        //
        //         }, 0);
        //     }
        // };

        //监听是否结束播放，使用lambda表达式可以使用整个controller的this
        // endedHandler = () => {
        //     console.log("播放结束2", this);
        // }


    }

]);
