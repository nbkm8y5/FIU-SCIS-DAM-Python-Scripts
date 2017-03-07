// FIX THE ERROR OF THUMBNAILS BEING SAVED WITH DIFFERENT FILE NAMES

import * as Jimp from 'jimp';
import * as fs from 'fs';
import * as path from 'path';
console.log("Image Thumbnail Program");
let dataStringArray: string[] = [];

let contents = fs.readFileSync('./thumbDataBeingAdded.txt', 'utf8');
dataStringArray = contents.split('\n');

dataStringArray.forEach((item, index) => {
    // console.log("Index " + index);
    // console.log(item);
    // console.log(path.basename(item));
    // console.log("/disk/assets/thumbnails" + item.replace("disk/assets/", ""));
    // console.log("/disk/assets/thumbnails" + path.dirname(item).replace("disk/assets/", ""));
    if (!fs.existsSync("/disk/assets/thumbnails" + path.dirname(item).replace("disk/assets/", ""))) {
        fs.mkdirSync("/disk/assets/thumbnails" + path.dirname(item).replace("disk/assets/", "")); //LOOPING
    }
    Jimp.read(item).then(image => {
        let tempImageString = "/disk/assets/thumbnails" + item.replace("disk/assets/", "");
        // console.log(tempImageString);
        if (image.bitmap.width > 3000 || image.bitmap.height > 3000) {

            // console.log(tempImageString);
            image
                .scale(.075)
                .quality(50)
                .write(tempImageString);
            console.log("Number: " + index);
            console.log(tempImageString + " done");
        } else if ((image.bitmap.width > 1000 && image.bitmap.width <= 2999) || (image.bitmap.height > 1000 && image.bitmap.height <= 2999)) {
            image
                .scale(.25)
                .quality(50)
                .write(tempImageString);
            console.log("Number: " + index);
            console.log(tempImageString + " done");
        } else {
            image
                .quality(50)
                .write(tempImageString);
            console.log("Number: " + index);
            console.log(tempImageString + " done");
        }
    }).catch(err => {
        console.error(err);
    });
});