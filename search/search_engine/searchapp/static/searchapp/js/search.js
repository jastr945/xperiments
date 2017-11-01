'use strict';

// removing placeholder from the search tab on focus and bringing it back on blur
$('.form-control').focus(function(){
   $(this).data('placeholder', $(this).attr('placeholder'))
          .attr('placeholder','');
}).blur(function(){
   $(this).attr('placeholder', $(this).data('placeholder'));
});


// requesting data from Elasticsearch using a jQuery AJAX call; returning matching results into a div

// $('#search').submit(function(e) {
//   e.preventDefault();
//
//   var data = {
//               "query":{"match":{"title":"cannon"}}
//               };
//   $.ajax({
//     url: 'http://localhost:9200/articles/_search?pretty=true',
//     type: 'POST',
//     contentType: 'application/json',
//     username: 'elastic',
//     password: 'changeme',
//     crossDomain: true,
//     async: true,
//     dataType: 'json',
//     data: JSON.stringify(data),
//     success: function(data) {
//       // console.log(data);
//       console.log("something worked here");
//     },
//     error: function(data){
//       console.log(JSON.stringify(data));
//     }
// });
// });

//test
// $('#search').submit(function(e) {
//   e.preventDefault();
//   var searchterm = $('.form-control').val();
//   $('#result').html(searchterm);
// });
