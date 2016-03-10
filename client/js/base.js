'use strict';

var $ = require('jquery');
global.jQuery = $;
require('bootstrap');

$(document).ready(function() {

  function positionSheets(initial) {
    var windowWidth = $(window).width();
    if ( windowWidth > 1300 && windowWidth < 1600 || initial === true && windowWidth > 1300 ) {
      $('.sheet').each(function(index,el){
        var step = $(el).attr('data-degree') / 300;
        var distance = windowWidth - 1300;
        if (initial && windowWidth >= 1600) {
          var distance = 300;
        }
        var rotation = step * distance;
        $(el).css({
          'transform': 'rotate(' + rotation  + 'deg)',
          'webkitTransform': 'rotate(' + rotation  + 'deg)',
          'mozTransform': 'rotate(' + rotation  + 'deg)',
          'msTransform': 'rotate(' + rotation  + 'deg)',
          'oTransform': 'rotate(' + rotation  + 'deg)'
        });
      });
    }
  }

  $(window).resize(function(e) {
    positionSheets();
  });

  positionSheets(true);

});