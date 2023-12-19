// Kullanıcının konum bilgilerine erişim isteği
navigator.geolocation.getCurrentPosition(onSuccess, onError);

function onSuccess(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // Burada konumu kullanarak harita ve toplanma alanlarını göstermek için bir API'yi çağırabilirsiniz.
    // Örneğin: getCollectionAreas(latitude, longitude);

    // Aşağıda sadece konumu alıp konsola yazdık.
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
}

function onError(error) {
    console.error(`Konum bilgisine erişim hatası: ${error.message}`);
}

// Örnek: Google Maps API kullanımı
function getCollectionAreas(latitude, longitude) {
    const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: latitude, lng: longitude },
        zoom: 12
    });

    // Burada toplanma alanlarını haritaya ekleyebilirsiniz.
    // Örneğin: Markers eklemek için google.maps.Marker sınıfını kullanabilirsiniz.
}