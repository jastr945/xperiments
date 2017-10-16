// Using jquery-csv plugin to parse the csv file and extract the names of Wikipedia articles
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
        $(".selectpicker").append('<option data-icon="glyphicon-star">' + data[i][1] + '</option>');
    }
  }
});


// Using Wikipedia API to load an article of user's choice from the select menu
$('.selectpicker').change(function () {
  var textTitle = $('.selectpicker option:selected').text();
  $.ajax({
    url: "http://en.wikipedia.org/w/api.php?format=xml&action=query&prop=extracts&titles=" + textTitle + "&redirects=true",
    data: {
        format: 'json'
    },
    dataType: 'jsonp',
    type: 'get',
    success: function (data) {
      data = $.parseJSON(JSON.stringify(data));
      myobj = data.query.pages;
      $.map(myobj, function(val, i) {
        $(".col-md-12").html("<div id='article'><p>" + myobj[i].extract + "</div></p>");
      });
    }
  });
});
