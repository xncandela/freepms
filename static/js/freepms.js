// Cascade Dropdown


$(document).ready(function () {
    console.log('Freepms.js cargado')
    const options = {year: 'numeric', month: 'numeric', day: 'numeric'};

    $(".exselect").each(function (index, element) {
        console.log('Inicio')
        console.log(index, '-', element)

        $('#' + element.id).trigger('change')
        // element.trigger('change')
    })

    $('.exselect').change(function (selector) {
        console.log('Change')
        console.log(selector)
        dataset = selector.target.dataset
        console.log(dataset)

        valor = selector.target.value
        console.log(valor)

        if ('cascadeSelect' in dataset) {
            console.log('ok')

            cascadeselect = dataset['cascadeSelect']
            url = location.origin + dataset['url']
            filtro = {}
            if ('filtro' in dataset) {
                filtro[dataset['filtro']] = valor
            } else {
                filtro[selector.target.name + '_id'] = valor
            }

            $.get(url, filtro).done(
                function (data, status) {
                    console.log(data, status);

                    $('#' + cascadeselect).html(data);
                })
        }

    })

})

