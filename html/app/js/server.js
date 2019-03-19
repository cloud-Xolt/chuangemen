myApp.service('apiService', ['$http', '$q',
    function ($http, $q) {

        // 请求url的前缀
        var api_prefix = '/api/v1/';

        function success(resp) {
            var config = resp.config;
            var msg = resp.data;

            config.deferred.resolve(msg);
        }

        // 新闻模块API请求
        this.news = {

            // 获取所有新闻列表
            get: function (params) {
                var deferred = $q.defer();
                $http({
                    method: 'GET',
                    url: api_prefix + 'news/',
                    params: params,
                    deferred: deferred,
                }).then(function (resp) {
                    success(resp);
                }, function (resp) {
                });

                return deferred.promise;
            },

        };

        // 视频模块API请求
        this.video = {

            // 获取所有视频种类
            type: {
                list: function (params) {
                    var deferred = $q.defer();
                    $http({
                        method: 'GET',
                        url: api_prefix + 'video_type/',
                        params: params,
                        deferred: deferred,
                    }).then(function (resp) {
                        success(resp);
                    }, function (resp) {
                    });

                    return deferred.promise;
                },
                get: function (pk, params) {
                    var deferred = $q.defer();
                    $http({
                        method: 'GET',
                        url: api_prefix + 'video_type/' + pk + "/",
                        params: params,
                        deferred: deferred,
                    }).then(function (resp) {
                        success(resp);
                    }, function (resp) {
                    });

                    return deferred.promise;
                },
            },

            video: {
                list: function (params) {
                    var deferred = $q.defer();
                    $http({
                        method: 'GET',
                        url: api_prefix + 'video/',
                        params: params,
                        deferred: deferred,
                    }).then(function (resp) {
                        success(resp);
                    }, function (resp) {
                    });

                    return deferred.promise;
                },
                get: function (pk, params) {
                    var deferred = $q.defer();
                    $http({
                        method: 'GET',
                        url: api_prefix + 'video/' + pk + "/",
                        params: params,
                        deferred: deferred,
                    }).then(function (resp) {
                        success(resp);
                    }, function (resp) {
                    });

                    return deferred.promise;
                },
            },

            anthology: {
                list: function (params) {
                    var deferred = $q.defer();
                    $http({
                        method: 'GET',
                        url: api_prefix + 'video_anthology/',
                        params: params,
                        deferred: deferred,
                    }).then(function (resp) {
                        success(resp);
                    }, function (resp) {
                    });

                    return deferred.promise;
                },
                get: function (pk, params) {
                    var deferred = $q.defer();
                    $http({
                        method: 'GET',
                        url: api_prefix + 'video_anthology/' + pk + "/",
                        params: params,
                        deferred: deferred,
                    }).then(function (resp) {
                        success(resp);
                    }, function (resp) {
                    });

                    return deferred.promise;
                },
            },

        };
    }]);
