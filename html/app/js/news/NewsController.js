myApp.controller('NewsList',
    ['$scope', 'apiService', function ($scope, apiService) {

    $scope.refresh = function () {
        apiService.news.get({
            search: $scope.news_filter,
            page: $scope.paginationConf.currentPage,
            size: $scope.paginationConf.itemsPerPage
        }).then(function(data){
            $scope.news_items = data.results;
            $scope.paginationConf.totalItems = data.count;

        });
    };

    $scope.paginationConf = {
        currentPage: 1,
        itemsPerPage: 15,
        totalItems: -1,
        pagesLength: 10,
        perPageOptions: [15, 30, 50, 100],
        onChange: function () {
            if ($scope.paginationConf.totalItems) {
                $scope.refresh();
            }
        }
    };

    // 根据条件查询新闻条目
    $scope.NewsSearch = function () {
        $scope.news_filter = "根据新闻标题查询...";
        // $scope.NewsFilter = apiService.news.list();
        // console.log($scope.NewsFilter);
    };
    // $scope.NewsSearch();

}]);