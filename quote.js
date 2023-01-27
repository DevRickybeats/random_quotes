// quote.js
$("#new-quote-btn").on("click", function () {
    $.ajax({
        url: '/quote',
        type: 'GET',
        success: function (response) {
            var quote = response.quote;
            $("#quote").text(quote);
        }
    });
});
