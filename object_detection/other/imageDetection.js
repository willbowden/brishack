const tf = require('@tensorflow/tfjs-node');
const cocoSsd = require('@tensorflow-models/coco-ssd');
const image = require('./image.jpg');

async function detectObjects(imagePath) {
  const imageBuffer = await tf.node.decodeImage(imagePath);
  const model = await cocoSsd.load();
  const predictions = await model.detect(imageBuffer);
  return predictions;
}

(async () => {
  const predictions = await detectObjects(require('./image.jpg'));
  console.log(predictions);
})();

