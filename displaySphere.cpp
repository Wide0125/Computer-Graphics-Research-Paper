inline void displaySphere(const Custom::Camera& camera, const Sphere& sphere) {
    for (int pixelY {0}; pixelY < camera.screenHeight(); ++pixelY) {
        for (int pixelX {0}; pixelX < camera.screenWidth(); ++pixelX) {
            if(rayIntersectWithSphere(getPixelLine(pixelX, pixelY, camera), sphere)) {
                DrawPixel(pixelX, pixelY, sphere.color);
            }
        }
    }
}
