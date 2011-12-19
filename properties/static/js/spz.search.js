/**
 * @namespace static module with search page functionality
 */
spz.search = {
    init: function() {
        if (screen.width<=400){
            $("html").css('width', "320px");
            $(".data-grid").html('');
        }

        spz.search.initFilters();
        spz.search.initMap();
        spz.search.zebraStripe($('#data-grid'));
    },
    initFilters: function() {
        $("#title-wrapper").click(function(evt) {
            if ($('.filter-panel:visible').length) {
                $('.filter-panel')
                    .slideUp('fast')
                    .animate({ opacity: 0 }, { queue: false, duration: 'fast' });
            } else {
                $('.filter-panel')
                    .css('opacity', 0)
                    .slideDown('fast')
                    .animate( { opacity: 1 }, { queue: false, duration: 'fast' });
            }
        });
        spz.search.initSliders();
        spz.search.initButtons();
    },
    initButtons: function() {
        $("#filter-form .buttons > a").click(function(evt) {
            $(this).toggleClass('selected');
        });
    },
    /**
     * initializes google map
     */
    initMap: function() {
        var latlng = new google.maps.LatLng(40.77274188001071, -73.99772644042969),
            myOptions = {
                zoom: 12,
                center: latlng,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            },
            map = new google.maps.Map($("#map_canvas")[0], myOptions);

            var marker = new google.maps.Marker({
                position: latlng,
                map: map,
            });

            latlng = new google.maps.LatLng(40.74048, -74.00013);
            marker = new google.maps.Marker({
                position: latlng,
                map: map,
            });

    },
    /**
     * rent range slider
    */
    initSliders: function() {
        var $rentSlider = $("#rent-range-slider");

        $rentSlider.slider({
            range: true,
            min: 0,
            max: 5000,
            step: 10,
            values: [100, 4000],
            slide: function(evt, ui) {
                $("#rent-range").html("$"+ui.values[0]+" - $"+ui.values[1]);
            }
        });
        $("#rent-range").html("$"+$rentSlider.slider('values',0)+" - $"+$rentSlider.slider('values',1));
    },
    zebraStripe: function($table) {
        $table.find('tbody > tr:odd').addClass('odd');
    }
};
$(document).bind('spz:initialized', spz.search.init);
