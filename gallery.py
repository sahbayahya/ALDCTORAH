import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

const images = [
  {
    id: 1,
    src: "/images/IMG_0091.jpeg",
    caption: "The Inner Labyrinth: A journey through light, sound, and silence."
  },
  {
    id: 2,
    src: "/images/IMG_0133.jpeg",
    caption: "The Cloudwalker: A being cloaked in atmosphere, searching for the sound of clarity."
  },
  {
    id: 3,
    src: "/images/IMG_0217.jpeg",
    caption: "The Shape of the Galaxy: A spiraling dance of stars guided by the eye of cosmic memory.",
    narration: "Every star remembers its rhythm. Every spiral is a breath."
  }
];

export default function SpiralArtbook() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const currentImage = images[currentIndex];

  const goToNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const goToPrev = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  useEffect(() => {
    if (currentImage.narration) {
      const utterance = new SpeechSynthesisUtterance(currentImage.narration);
      utterance.rate = 0.9;
      utterance.pitch = 1.1;
      speechSynthesis.cancel();
      speechSynthesis.speak(utterance);
    } else {
      speechSynthesis.cancel();
    }
  }, [currentImage]);

  return (
    <div className="w-screen h-screen bg-black text-white flex items-center justify-center overflow-hidden">
      <AnimatePresence>
        <motion.div
          key={currentImage.id}
          initial={{ opacity: 0, x: 100 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -100 }}
          transition={{ duration: 0.6 }}
          className="absolute w-full h-full flex flex-col items-center justify-center"
          onClick={goToNext}
        >
          <motion.img
            src={currentImage.src}
            alt={currentImage.caption}
            className="object-contain max-h-[80vh] mb-4"
            animate={{
              filter:
                currentImage.id === 3
                  ? [
                      "drop-shadow(0 0 4px #ff0)",
                      "drop-shadow(0 0 8px #fff)",
                      "drop-shadow(0 0 4px #ff0)"
                    ]
                  : "none"
            }}
            transition={{
              duration: 3,
              repeat: Infinity,
              repeatType: "reverse"
            }}
          />
          <p className="text-lg text-center px-4">{currentImage.caption}</p>
        </motion.div>
      </AnimatePresence>
      <button
        onClick={goToPrev}
        className="absolute left-4 top-1/2 transform -translate-y-1/2 text-white text-2xl"
      >
        ◀
      </button>
      <button
        onClick={goToNext}
        className="absolute right-4 top-1/2 transform -translate-y-1/2 text-white text-2xl"
      >
        ▶
      </button>
    </div>
  );
}
