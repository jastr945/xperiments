// Extracting articles using Wikipedia's API

$.ajax({
    url: 'http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Science_fiction_genres&cmlimit=200',
    data: {
        format: 'json'
    },
    dataType: 'jsonp',
    type: 'get',
}).done(function (data) {
    $("#mainContainer").append(JSON.stringify(data));
});


$.ajax({
    url: 'http://en.wikipedia.org/w/api.php?format=xml&action=query&prop=extracts&titles=Gothic_science_fiction&redirects=true',
    data: {
        format: 'json'
    },
    dataType: 'jsonp',
    type: 'get',
}).done(function(data) {
    var pageNumber = "3311692";
    $("#mainContainer").append(JSON.stringify(data["query"]["pages"][pageNumber]["extract"]));
});


$.ajax({
    url: 'http://en.wikipedia.org/w/api.php?format=xml&action=query&prop=extracts&titles=Steampunk&redirects=true',
    data: {
        format: 'json'
    },
    dataType: 'jsonp',
    type: 'get',
}).done(function(data) {
    var pageNumber = "27684";
    $("#mainContainer").append(JSON.stringify(data["query"]["pages"][pageNumber]["extract"]));
});
