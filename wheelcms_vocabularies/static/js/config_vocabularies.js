app.controller('VocabCtrl', function($scope) {
    $scope.newvocabulary = {};
    $scope.deleted = [];
    $scope.vocabularies = [];

    $scope.init = function(vocabularies) {
        $scope.vocabularies = vocabularies;
    };

    $scope.addVocabulary = function() {
        $scope.vocabularies.push($scope.newvocabulary);
        $scope.newvocabulary = {};
    };

    $scope.removeVocabulary = function(id) {
        $scope.deleted.push($scope.vocabularies[id].identifier);
        $scope.vocabularies.splice(id, 1);
    };
});
