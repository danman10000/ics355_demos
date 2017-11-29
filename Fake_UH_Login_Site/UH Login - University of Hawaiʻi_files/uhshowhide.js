jQuery(document).ready(function() {
  jQuery("#eye").click(function () {
    if (jQuery("#password").attr("type") == "password") {
        jQuery("#password").attr("type", "text");
    } else {
        jQuery("#password").attr("type", "password");
    }
})});
