numberCard = document.querySelector('.number-card')


numberCard.addEventListener("input", function (event) {
    let value = event.target.value.replace(/\D/g, "");
    let formattedValue = value.match(/.{1,4}/g)?.join(" ") || "";

    event.target.value = formattedValue;
});

expireDate = document.querySelector('.expire-date')

expireDate.addEventListener("input", function (event) {
    let value = event.target.value.replace(/\D/g, "");
    if (value.length > 2) {
        value = value.slice(0, 2) + '/' + value.slice(2);
    }
    event.target.value = value;
});
