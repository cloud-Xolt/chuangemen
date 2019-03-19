myApp.controller('VideoMenuController', ['$scope', "apiService",
    "$uibModal",
    function ($scope, apiService, $uibModal) {

        apiService.video.type.list({
            page: 1,
            size: 1000
        }).then(function(data){
            $scope.allVideoType = data.results;
        });

        $scope.isNew = function (data) {
            if (data){
                dateTime = new Date(Date.parse(data.replace(/-/g, "/")));
                dateTime = dateTime.setDate(dateTime.getDate()+3);
                dateTime = new Date(dateTime);
                today = new Date();
                if (dateTime > new Date()){
                    return true;
                }
            }
            return false;

        };

        // 分页
        $scope.paginationConf = {
            currentPage: 1,
            itemsPerPage: 15,
            totalItems: -1,
            pagesLength: 10,
            perPageOptions: [15, 30, 50, 100],
            onChange: function () {
                if ($scope.paginationConf.totalItems) {
                    $scope.getVideoName($scope.thisType);
                }
            }
        };

        $scope.myKeyup = function(e){
            console.log(2222)
            if(e.keyCode==13){
                $scope.getVideoName();
            }
        };

        $scope.getVideoName = function (typePk, page) {
            $scope.thisType = typePk;
            if(!page){
                page = $scope.paginationConf.currentPage;
            }

            apiService.video.video.list({
                video_type__id: typePk,
                search: $scope.videoFilter,
                page: page,
                size: $scope.paginationConf.itemsPerPage
            }).then(function(data){
                $scope.video_name_map = data.results;
                $scope.paginationConf.totalItems = data.count;
            });

        };

    }
]);

myApp.controller('VideoShowController', ['$scope', "apiService",
    "$stateParams", '$state',
    function ($scope, apiService, $stateParams, $state) {

        if (!$stateParams.videoId){
            window.location="#/videos";
        }else {
            apiService.video.video.get($stateParams.videoId
            ).then(function(data){
                $scope.videoDes = data;

                apiService.video.anthology.list({
                    video__id: $scope.videoDes.id
                }).then(function(data){
                    $scope.videoSource = data.results;
                    $scope.play($scope.videoSource[0].id);
                });
            });

            $scope.play = function (videoId) {
                $state.go("videos-show.player",
                    {"episodeId": videoId, "imageUrl": $scope.videoDes.poster});
            };

        }
    }
]);
