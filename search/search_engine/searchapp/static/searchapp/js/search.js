'use strict';

// removing placeholder from the search tab on focus and bringing it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
          .attr('placeholder','');
}).blur(function(){
   $(this).attr('placeholder', $(this).data('placeholder'));
});


// requesting data from Elasticsearch using a jQuery AJAX call; returning matching results into a div

$('#search').submit(function(e) {
  e.preventDefault();
  var searchterm = $('.form-control').val();
  $.ajax({
    url: 'http://localhost:9200/articles/_search',
    type: 'GET',
    username: 'elastic',
    password: 'changeme',
    crossDomain: true,
    dataType: 'json',
    data: {
        query:{match:{_all:searchterm}},
        pretty: true,
        fields: 'title'
    },
    success: function(data) {
      data = JSON.stringify(data);
      console.log(data);
      $('#result').append(data);
    }
  });
});

//test
// $('#search').submit(function(e) {
//   e.preventDefault();
//   var searchterm = $('.form-control').val();
//   $('#result').html(searchterm);
// });
