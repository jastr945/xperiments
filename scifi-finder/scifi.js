// Using jquery-csv plugin to parse the csv file and extract articles' names
$.ajax({
    url: "scifi_genres.csv",
    async: false,
    success: function (csvd) {
        data = $.csv.toArrays(csvd);
    },
    dataType: "text",
    complete: function () {
      var i;
      for (i = 1; i < data.length; ++i) {
        $("#mainContainer").append(data[i][1]);
    }
  }
});

// Using Wikipedia's API to extract several articles from the 'Science_fiction_genres' category
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
