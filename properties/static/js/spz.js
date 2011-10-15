/**
 * @namespace global namespace for slickpadz
 * @requires jquery
 */
var spz = {
    /**
     * main method invoked on DOM ready
     */
    init: function() {
        spz.bindEvents();
        $(document).trigger('spz:initialized');
    },
    /**
     * binds events to their handlers
     */
    bindEvents: function() {
        $(document).bind('spz:initialized', spz.initMap);
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
$().ready(spz.init);
