const pptxgen = require('pptxgenjs');
const html2pptx = require('./html2pptx');
const path = require('path');

async function createPresentation() {
    console.log("Starting presentation generation...");

    // Create new presentation
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9'; // Matches our 720pt x 405pt HTML
    pptx.author = 'Antigravity';
    pptx.title = 'Greenland: The Arctic Jewel';

    // List of slides
    const numSlides = 11;

    for (let i = 1; i <= numSlides; i++) {
        const slidePath = path.join(__dirname, 'slides', `slide${i}.html`);
        console.log(`Processing ${slidePath}...`);

        try {
            await html2pptx(slidePath, pptx);
        } catch (err) {
            console.error(`Error processing slide ${i}:`, err);
        }
    }

    const outFile = 'Greenland_Presentation.pptx';
    await pptx.writeFile({ fileName: outFile });
    console.log(`Presentation saved to ${outFile}`);
}

createPresentation().catch(err => {
    console.error("Fatal error:", err);
    process.exit(1);
});
