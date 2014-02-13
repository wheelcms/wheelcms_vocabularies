app.controller('VocabCtrl', function($scope) {
    $scope.newvocabulary = {};
    $scope.deleted = [];

    $scope.vocabularies = [
        {identifier:"foo.bar",
         data:"{bla bla bla}"},
        {identifier:"arg.bar",
         data:"{bla flop bla}"},
        {identifier:"frap.flop.pip",
         data:"{asdfasdf asdfsd sdasdf}"}

    ];

    $scope.addVocabulary = function() {
        $scope.vocabularies.push($scope.newvocabulary);
        $scope.newvocabulary = {};
    };

    $scope.removeVocabulary = function(id) {
        $scope.deleted.push($scope.vocabularies[id].identifier);
        $scope.vocabularies.splice(id, 1);
        console.log($scope.deleted);
    };
});
