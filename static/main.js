/**
 * Created by tmatheesha on 6/14/2017.
 */
(function () {

    angular.module('TextAnnApp',[])
        
        .controller('TextAnnController',['$scope','$log','$http','$timeout',
            function ($scope,$log,$http,$timeout) {
                $scope.getResults = function () {

                    $log.log("test");

                    var userInput = $scope.url;

                    $http.post('/start', {"url": userInput}).
                    success(function (results) {
                        $log.log(results);
                        getAnnalysed(results);
                    }).
                    error(function (error) {
                        $log.log(error);
                    });
                };
                    

                function getAnnalysed(jobID) {

                    var timeout = "";

                    var poller = function () {
                        //fire another request
                        $http.get('/results/',+jobID).
                        success(function (data, status, header, config) {
                            if (status === 202) {
                                $log.log(data, status);
                            } else if (status === 2000) {
                                $log.log(data);
                                $scope.inautheticTextAnn = data;
                                $timeout.cancel(timeout);
                                return false
                            }

                            timeout = $timeout(poller, 2000);

                        });

                    };
                    poller();
                };

            }

        ]);
    
    
}());