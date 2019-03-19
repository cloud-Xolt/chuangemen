var myApp = angular.module("ChuanMen", ["ui.router", "pagination",
    'ui.bootstrap']);

// 导航
myApp.controller('navCtroller', ['$scope', '$location',
    function($scope, $location){

        // 配置默认导航选中
        $scope.tabType = $location.url()? $location.url().slice(1): "news";

        $scope.switchTab = function(type){
            $scope.tabType = type;
        };
}]);

myApp.config(['$stateProvider', '$urlRouterProvider',
    function ($stateProvider, $urlRouterProvider) {

    // RestangularProvider.setBaseUrl("/");
    // $urlRouterProvider.when("", "/news");

    $urlRouterProvider.otherwise('/news')
    $stateProvider
        .state('news', {
            url: '/news',
            templateUrl: 'news/NewsMenu.html',
            controller: 'NewsList'
        })
        .state("videos", {
            url: "/videos",
            templateUrl: function () {
                return  'video/VideoMenu.html';
            },
            controller: "VideoMenuController"
        })
        .state("videos-show", {
            url: "/videos/show",
            params : {videoId: null},
            templateUrl: 'video/VideoShow.html',
            controller: "VideoShowController"
        })
        .state("videos-show.player", {
            url: "/videos/show/player",
            params : {episodeId: null, imageUrl: null},
            templateUrl: 'video/modal/videoPlayer.html',
            controller: "VideoPlayController"
        })

}]);
