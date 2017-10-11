// Extracting articles using Wikipedia's API

$.ajax({
    url: 'http://en.wikipedia.org/w/api.php?format=xml&action=query&prop=extracts&titles=Blade_runner&redirects=true',
    data: {
        format: 'json'
    },
    dataType: 'jsonp',
    type: 'get',
}).done( function ( data ) {
    var pageNumber = "3746";
    $("#mainContainer").append(JSON.stringify(data["query"]["pages"][pageNumber]["extract"]));
});
