#ifndef SPHERE_H
#define SPHERE_H
#include <raylib-cpp.hpp>

struct Sphere {
        Point center {0.0, 0.0, 0.0};
        double radius {1};
        raylib::Color color {RED};
};

#endif
