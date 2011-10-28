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
    }
};
$(document).ready(spz.init);
