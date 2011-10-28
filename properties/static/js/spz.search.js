/**
 * @namespace static module with search page functionality
 */
spz.search = {
    init: function() {
        spz.search.initMap();
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
    }
};
$(document).bind('spz:initialized', spz.search.init);
