var random_images_array = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
];

path = 'imágenes/img_index/'; 
var num = Math.floor( Math.random() * random_images_array.length );
var img = random_images_array[ num ];
if (img === "1.png") {
    var img_conf = 'fija1';
}
if (img === '2.png') {
    var img_conf = 'fija2';
}
if (img === '3.png') {
    var img_conf = 'fija3';
}
if (img === '4.png') {
    var img_conf = 'fija4';
}
var imgStr = '<img src="' + path + img + '" alt="cute static image"' + 'class=' + img_conf + '>';

document.write(imgStr); document.close();
