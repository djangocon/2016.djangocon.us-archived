'use strict';

var $ = require('jquery');
global.jQuery = $;
require('bootstrap');

$(window).resize(function(e) {
  var windowWidth = $(window).width();
  if ( windowWidth > 1300 && windowWidth < 1600 ) {
    $('.sheet').each(function(index,el){
      var step = $(el).attr('data-degree') / 300;
      var distance = windowWidth - 1300;
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
  // var theta = $(window).scrollTop() % Math.PI;
  // $('#leftgear').css({ transform: 'rotate(' + theta + 'rad)' });
  // $('#rightgear').css({ transform: 'rotate(-' + theta + 'rad)' });
});