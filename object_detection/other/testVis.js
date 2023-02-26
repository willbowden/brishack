// * TensorFlow Stuff
import * as tf from "@tensorflow/tfjs-node";
import coco_ssd from "@tensorflow-models/coco-ssd";

// * Server Stuff
import busboy from "busboy";

let model = undefined;
(async () => {
  model = await coco_ssd.load({
    base: "mobilenet_v1",
  });
})();

// * Create a Busboy instance
async function getObjects() {
    const bb = busboy({ headers: req.headers });
    bb.on("file", (fieldname, file, filename, encoding, mimetype) => {
    const buffer = [];
    file.on("data", (data) => {
        buffer.push(data);
    });
    file.on("end", async () => {
        // * Run Object Detection
        const image = tf.node.decodeImage(Buffer.concat(buffer));
        const predictions = await model.detect(image, 3, 0.25);
        const result = JSON.stringify(predictions);
        return result;
    });
    });
    req.pipe(bb);
}

export default getObjects;