ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true
        });
    var geolocation = ymaps.geolocation;


    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    //objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.objects.options.set('iconLayout', 'default#image');
    objectManager.objects.options.set('iconImageHref', 'static/img/Beer_icon.png');
    objectManager.objects.options.set('iconImageSize', [35, 35]);
    objectManager.clusters.options.set('iconLayout', 'default#image');
    objectManager.clusters.options.set('iconImageHref', 'static/img/Beer_icon.png');
    myMap.geoObjects.add(objectManager);

    $.ajax({
        url: "main"
    }).done(function(data) {
        objectManager.add(data);
    });

    geolocation.get({
        provider: 'yandex',
        mapStateAutoApply: true
    }).then(function (result) {
        // Красным цветом пометим положение, вычисленное через ip.
        result.geoObjects.options.set('preset', 'islands#redCircleIcon');
        result.geoObjects.get(0).properties.set({
            balloonContentBody:  'Центр'
        });
        myMap.geoObjects.add(result.geoObjects);
    });

    geolocation.get({
        provider: 'browser',
        mapStateAutoApply: true
    }).then(function (result) {
        // Синим цветом пометим положение, полученное через браузер.
        // Если браузер не поддерживает эту функциональность, метка не будет добавлена на карту.
        result.geoObjects.options.set('preset', 'islands#blueCircleIcon');
        myMap.geoObjects.add(result.geoObjects);
    });

    res.geoObjects.each(function (geoObject) {
                        geoObject.options.set({
                            
                            preset : 'twirl#trainIcon'
                            
                            , iconImageHref: 'static/img/Beer_icon.png' // картинка иконки
                            , iconImageSize: [30, 42] // размеры картинки
                            , iconImageOffset: [-3, -42] // смещение картинки
                            
                        });
                    });

}


