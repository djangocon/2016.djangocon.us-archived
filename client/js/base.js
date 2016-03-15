'use strict';

var $ = require('jquery');
global.jQuery = $;
window.jQuery = window.$ = $;
require('bootstrap');

$(document).ready(function() {

  function rotateSheets(initial) {
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

  function positionSheets(initial) {
    if (initial) {

      var intWidth = $(window).innerWidth();
      var intHeight = $(window).innerHeight();

      var x = intWidth / 2;
      var y = intHeight / 2;

      $('.sheet').each(function(index,el){
        var orientation = $(el).attr('data-orientation');
        if ( orientation === 'left' ) {
          $(el).css({
            'left': (x - $(el).width()/2) + 'px',
            'top': 200 + 'px'
          });
        } else if ( orientation === 'right' ) {
          $(el).css({
            'right': (x - $(el).width()/2) + 'px',
            'top': 200 + 'px'
          });
        }
      });

    } else {

      var windowWidth = $(window).width();
      var intWidth = $(window).innerWidth();
      var intHeight = $(window).innerHeight();

      var x = intWidth / 2;
      var y = intHeight / 2;

      if ( windowWidth > 1300 ) {

        var distance = (windowWidth - 1300) / 2;

        $('.sheet').each(function(index,el){
          var destX = parseInt($(el).attr('data-posx'));
          var orientation = $(el).attr('data-orientation');
          console.log(orientation)
          if ( orientation === 'left' ) {
            if (windowWidth >= 1900) {
              var posX = destX;
            } else {
              var elWidth = $(el).width()/2;
              var path =  650 - elWidth - destX;
              var stepX = path / 300;
              var posX = 120 + path - stepX * distance;
            }
            $(el).css({
              'left': posX + 'px',
              'top': 200 + 'px'
            });
          } else if ( orientation === 'right' ) {
            if (windowWidth >= 1900) {
              var posX = destX;
            } else {
              var elWidth = $(el).width()/2;
              var path =  650 - elWidth - destX;
              var stepX = path / 300;
              var posX = 120 + path - stepX * distance;
            }
            $(el).css({
              'right': posX + 'px',
              'top': 200 + 'px'
            });
          }

        });

      } else {

        $('.sheet').each(function(index,el){
          var orientation = $(el).attr('data-orientation');
          if ( orientation === 'left' ) {
            $(el).css({
              'left': (x - $(el).width()/2) + 'px',
              'top': 200 + 'px'
            });
          } else if ( orientation === 'right' ) {
            $(el).css({
              'right': (x - $(el).width()/2) + 'px',
              'top': 200 + 'px'
            });
          }
        });

      }
    }
  }

  $(window).resize(function(e) {
    rotateSheets();
    positionSheets();
  });

  rotateSheets(true);
  positionSheets(true);

});