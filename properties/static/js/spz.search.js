/**
 * @namespace static module with search page functionality
 */
spz.search = {
    init: function() {
        spz.search.initMap();
        spz.search.initSliders();
        spz.search.zebraStripe($('#data-grid'));
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
    },
    initSliders: function() {
        var $rentSlider = $("#rent-range-slider");

        $rentSlider.slider({
            range: true,
            min: 0,
            max: 5000,
            step: 10,
            values: [100, 500],
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
