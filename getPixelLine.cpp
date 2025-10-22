inline constexpr Line getPixelLine(int pixelX, int pixelY, const Custom::Camera& camera) {

    double xDistanceFromCenter {camera.viewportWidth()/camera.screenWidth() * -(pixelX - camera.screenWidth()/2)};
    double yDistanceFromCenter {camera.viewportHeight()/camera.screenHeight() * -(pixelY - camera.screenHeight()/2)};

    return {camera.pos(), {xDistanceFromCenter, yDistanceFromCenter, 1}};
} // get vector from origin to pixel's equivalent location on viewport
