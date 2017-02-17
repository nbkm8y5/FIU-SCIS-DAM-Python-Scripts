// FIX THE ERROR OF THUMBNAILS BEING SAVED WITH DIFFERENT FILE NAMES

import * as Jimp from 'jimp';
import * as fs from 'fs';
import * as path from 'path';
console.log("Image Thumbnail Program");

function willGetRelativePathsFromFile(): Promise<string> {
    return new Promise((resolve, reject) => {
        fs.readFile('./data.txt', 'utf8', (err, dataString) => {
            if (err) reject(err);
            else resolve(dataString);
        });
    });
}

export async function getRelativePathArray(): Promise<string[]> {
    let tempString: string = '';
    let dataStringArray: string[] = [];
    tempString = await willGetRelativePathsFromFile();
    try {
        dataStringArray = tempString.toString().split('\n');
    } catch (error) {
        console.log('getRelativePathArray() ERROR');
        console.log(error);
    }
    return dataStringArray;
};

getRelativePathArray()
    .then(array => {
        array.forEach((item, index) => {
            console.log(item);

            // Jimp.read(item).then(lenna => {
            //     lenna.quality(50)
            //         .scale(0.1)
            //         .write("/disk/assets/thumbnails/thumbnail-" + path.basename(item)); // save
            //     console.log("Number: " + index);
            //     console.log(path.basename(item) + " done");
            // }).catch(err => {
            //     console.error(err);
            // });
            
        });
    });