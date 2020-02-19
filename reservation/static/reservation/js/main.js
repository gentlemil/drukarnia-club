var logic = function (currentDateTime) {
    // 'this' is jquery object datetimepicker
    if (currentDateTime.getDay() == 6) {
        this.setOptions({
            minTime: '11:00'
        });
    } else
        this.setOptions({
            minTime: '8:00'
        });
};
jQuery('#datetimepicker_rantime').datetimepicker({
    onChangeDateTime: logic,
    onShow: logic
});