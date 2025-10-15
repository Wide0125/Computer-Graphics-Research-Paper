bool rayIntersectWithSphere(const Line& ray, const Sphere& sphere) {
    const auto a {dotProduct(ray.direction, ray.direction)};
    const auto b {2 * dotProduct(ray.origin - sphere.center, ray.direction)};
    const auto c {dotProduct(ray.origin - sphere.center, ray.origin - sphere.center) - pow(sphere.radius, 2)};
    return pow(b, 2) - (4 * a * c) >= 0 and -b/a >= 0 and c/a >= 0;
    // solve for t to see if the ray intersects with sphere, use discriminant to see if t exists
}
