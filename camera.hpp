#ifndef CUSTOMCAMERA_H
#define CUSTOMCAMERA_H
#include <cmath>
#include "vector.hpp"

namespace Custom {
    class Camera {
        public:
            constexpr const Point& pos() const {return m_pos;}

            constexpr double viewportWidth() const {return m_viewportWidth;}
            constexpr double viewportHeight() const {return m_viewportHeight;}

            constexpr int screenWidth() const {return m_screenWidth;}
            constexpr int screenHeight() const {return m_screenHeight;}

        private:
            Point m_pos {0, 0, 0};
            int m_screenWidth {960};
            int m_screenHeight {540};
            
            double m_viewportDistanceFromCamera {1};
            double m_viewportHeight {1};
            double m_viewportWidth {m_viewportHeight/m_screenHeight * m_screenWidth};
    };
}

#endif
